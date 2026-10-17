# Athlete memory and MCP server

[Project overview](../README.md) · Updated: 17 October 2026

## Responsibility

A curated, per-athlete "second memory" for the coach: durable facts such as pain, recurring technique issues, preferences, constraints, typical responses to training, goals and coach decisions. The same rules apply whether an entry comes from the web UI or from an AI chat through the MCP server. Training numbers stay in the [training log](../training/README.md) and are not copied here.

## Current state

| Part | Works | Still missing |
|---|---|---|
| Data model | `AthleteMemory`: category, content, optional exercise and reason, observation date, status, source, creator, reviewer | Free-form tags, attachments, links to a specific session or plan version |
| Coach entry (web) | **Emlékek** page from the athlete page; entries are active immediately | Editing an entry's text (currently: resolve and add a new one) |
| Coach review | Approve / reject AI proposals; resolve and reactivate active entries | Bulk review, notifications |
| Selection rules | Fixed categories, 12–300 characters, near-duplicate rejection, reason required for AI proposals, max 10 pending proposals per athlete | Expiry dates, automatic review reminders for old entries |
| MCP server | Local stdio server for one coach: list athletes, athlete context, search, propose, save on explicit coach request, propose a session move/skip | Remote/hosted access, athlete-side AI, in-app chat |

Main files: [models.py](models.py), [services.py](services.py) (write and review rules), [views.py](views.py), [mcp_tools.py](mcp_tools.py) (tool logic), [run_mcp_server.py](management/commands/run_mcp_server.py) (MCP wiring and AI instructions), [tests.py](tests.py). Screen: [athlete_memory.html](../templates/memory/athlete_memory.html).

## How entries get in

| Path | Source | Status after saving |
|---|---|---|
| Coach types it on the Emlékek page | `coach` | Active |
| Coach tells the AI "remember that…" → `save_memory_on_coach_request` | `ai_coach_request` | Active, labelled as coming from the AI chat |
| AI notices a durable fact on its own → `propose_memory` (reason required) | `ai_proposal` | Proposed; becomes active only after coach approval |

Resolved entries stay visible as history and can be reactivated. Rejected proposals are kept in the database for traceability but are hidden.

## Using the MCP server with an AI client

The server runs locally over stdio and exposes only the given coach's athletes. Example for Claude Desktop (`claude_desktop_config.json`); replace the path and the username:

```json
{
  "mcpServers": {
    "coaching-memory": {
      "command": "uv",
      "args": ["--directory", "C:\\path\\to\\Coaching", "run", "python", "manage.py",
               "run_mcp_server", "--coach", "YOUR_USERNAME"]
    }
  }
}
```

Tools: `list_athletes`, `get_athlete_context` (active memories, pending count, last 5 sessions with prescribed vs actual sets, next 10 planned sessions), `search_memories`, `propose_memory`, `save_memory_on_coach_request`, and `propose_session_change` (move or skip one upcoming session; it becomes a plan change proposal that the coach approves in the app, see the [training module](../training/README.md)). The server's instructions tell the AI what is worth storing and what is not.

**Data protection:** whatever the tools return is sent to the AI provider behind the client. Pain and injury entries can be health data. Use it with real athletes only after informing them and obtaining consent; until then, use synthetic data. See chapter 11 of the [research plan](../eroemelo_ai_kutatas_es_terv.md).

## Decisions and reasoning

| Decision | Why? | Consequence / limit |
|---|---|---|
| Separate `memory` app | Memory is its own responsibility and is reused by the UI and MCP | `training` views count memories for the athlete page |
| Fixed categories, no "other" | Forces each entry to be a specific, durable coaching fact | Something that fits no category is not stored |
| AI proposals need a reason and approval | The AI must not fill the memory with low-value or wrong items | The coach has to review proposals regularly |
| Explicit coach requests are active at once | The coach asked for it; extra approval would be friction | The AI could misuse the tool; entries are labelled by source and can be resolved |
| Near-duplicate check (normalised text, containment, similarity ≥ 0.85) within open entries of the same category | Rephrased repeats should not pile up | Very different wording of the same fact can still get through; this is a heuristic |
| Pending proposal cap (10 per athlete) | An over-eager AI cannot flood the review queue | Further proposals are refused until the coach reviews |
| Resolve instead of delete | History stays visible ("the knee problem in spring") | A final data-protection deletion process is separate work |
| MCP instead of an in-app chat first | The idea can be tried in an existing AI client without building a chat UI or managing API keys | Requires a desktop AI client; not usable by athletes |
| Business rules in `services.py`, thin MCP layer | The web UI and the AI follow exactly the same rules | New write paths must call the services, not the model directly |
| ORM calls wrapped with `sync_to_async` | FastMCP runs tools in an event loop; Django's ORM is synchronous | Tool logic stays testable as plain functions |
| Every tool call goes through `call_tool_safely` | A long-running process needs fresh DB connections, a correlation id, timing and error isolation | Unexpected errors reach the AI only as a generic message with a reference; see [operations](../ops/README.md) |

## Verification

`uv run python manage.py test memory`: 14 tests covering the selection rules, review transitions, coach isolation in views and tools, the athlete-page counter and an end-to-end tool call through the FastMCP server. Last local result: all passed (68/68 in the full suite). MCP error handling is tested in [ops/tests.py](../ops/tests.py).

A manual stdio smoke test with the official MCP Python client (initialize, list tools, call `list_athletes`) succeeded against a temporary local account that was removed afterwards. Trying it in Claude Desktop with real conversations has not been done yet.

## Next step

1. Use it yourself with synthetic or consented data and check whether the AI proposes useful entries and leaves out the noise; tune the instructions and rules based on what you see.
2. Add the memory question to the validation interviews (do coaches lose track of athlete history?).
3. Later: editing entries, an expiry or "review again" date for temporary issues, and an in-app chat that uses the same services.
