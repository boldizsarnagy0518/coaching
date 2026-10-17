"""Run a local stdio MCP server that exposes one coach's athletes and memory to an AI client."""
from asgiref.sync import sync_to_async
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from mcp.server.fastmcp import FastMCP
from mcp.types import ToolAnnotations

from memory import mcp_tools

INSTRUCTIONS = f"""You assist a powerlifting coach. This server gives access to the coach's athletes,
their recent training log and a curated per-athlete memory.

Before discussing an athlete, call get_athlete_context and use the active memories.

Memory must stay small and useful. Only store durable, coaching-relevant facts that will matter
in later weeks: pain or injury, a recurring technique issue, a preference, a schedule/equipment
constraint, a typical response to training, a goal or competition, or a coach decision with its reason.
Do NOT store small talk, one-off moods, numbers already in the training log, guesses, or anything
the coach did not confirm or clearly state. Never diagnose; record what was reported.

Use save_memory_on_coach_request only when the coach explicitly asks you to remember something.
Otherwise, if you notice a fact that clearly meets the rules above, call propose_memory with a reason;
the coach reviews proposals in the app. If a tool reports a duplicate, do not retry with a rephrasing.

For schedule changes (missed session, different training days), use the upcoming_sessions from
get_athlete_context and call propose_session_change. Never claim a change is applied: the coach
approves it in the app after seeing the before/after view. Do not change loads or exercises.

Categories: {mcp_tools.CATEGORIES}."""

READ_ONLY = ToolAnnotations(readOnlyHint=True, openWorldHint=False)
WRITE = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=False)


def build_server(coach):
    """Create the FastMCP server with every tool bound to ``coach``."""
    server = FastMCP("coaching-memory", instructions=INSTRUCTIONS)

    def run(func, *args, **kwargs):
        # Django ORM calls must run outside the event loop thread.
        return sync_to_async(func, thread_sensitive=True)(coach, *args, **kwargs)

    @server.tool(annotations=READ_ONLY)
    async def list_athletes() -> list[dict]:
        """List the coach's athletes with their ids."""
        return await run(mcp_tools.list_athletes)

    @server.tool(annotations=READ_ONLY)
    async def get_athlete_context(athlete_id: int) -> dict:
        """Active memories, pending proposal count and the last sessions (prescribed vs actual) of one athlete."""
        return await run(mcp_tools.get_athlete_context, athlete_id)

    @server.tool(annotations=READ_ONLY)
    async def search_memories(query: str, athlete_id: int | None = None, include_resolved: bool = True) -> list[dict]:
        """Search active (and optionally resolved) memories by words in content, exercise or reason."""
        return await run(mcp_tools.search_memories, query, athlete_id, include_resolved)

    @server.tool(annotations=WRITE)
    async def propose_memory(athlete_id: int, category: str, content: str, reason: str,
            exercise: str = "", observed_on: str | None = None) -> dict:
        """Propose a durable fact for the coach to approve. Requires a reason why it matters later.

        content: one specific statement, max 300 characters. observed_on: ISO date (YYYY-MM-DD), default today.
        """
        return await run(mcp_tools.propose_memory, athlete_id, category, content, reason, exercise, observed_on)

    @server.tool(annotations=WRITE)
    async def save_memory_on_coach_request(athlete_id: int, category: str, content: str,
            exercise: str = "", observed_on: str | None = None) -> dict:
        """Save a fact immediately as active. Only when the coach explicitly asked to remember it."""
        return await run(mcp_tools.save_memory_on_coach_request, athlete_id, category, content, exercise,
            observed_on)

    @server.tool(annotations=WRITE)
    async def propose_session_change(athlete_id: int, session_id: int, kind: str, reason: str,
            new_date: str | None = None) -> dict:
        """Propose moving (kind="move", new_date YYYY-MM-DD) or skipping (kind="skip") one upcoming session.

        Only unlogged sessions can change. Nothing is applied until the coach approves it in the app.
        """
        return await run(mcp_tools.propose_session_change, athlete_id, session_id, kind, reason, new_date)

    return server


class Command(BaseCommand):
    help = "Run the coaching-memory MCP server over stdio for one coach account."

    def add_arguments(self, parser):
        parser.add_argument("--coach", required=True, help="Username of the coach whose data is exposed.")

    def handle(self, *args, **options):
        try:
            coach = get_user_model().objects.get(username=options["coach"], is_active=True)
        except get_user_model().DoesNotExist as exc:
            raise CommandError("Unknown or inactive coach username.") from exc
        # stdout carries the MCP protocol; never print anything else to it.
        build_server(coach).run("stdio")
