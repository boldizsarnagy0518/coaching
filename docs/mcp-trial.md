# Trying the MCP server in Claude Desktop

[Status, decisions and validation](README.md) · Updated: 17 October 2026

Goal: find out, with synthetic data, whether an AI client using the coaching MCP server helps a coach think about an athlete, stores the right facts and leaves out the noise. This is a guide and a scoring sheet; the trial itself has **not** been done yet.

## 1. Prepare a demo database (no real athlete data)

From the project root:

```powershell
$env:COACHING_DB_PATH = ".local/demo.sqlite3"
uv run python manage.py migrate
uv run python manage.py create_demo_coach          # skip if demo-coach already exists
uv run python manage.py seed_demo --username demo-coach
```

The demo coach's password is in `.local/demo-credentials.txt` (only needed for the web UI).

## 2. Connect Claude Desktop

Claude Desktop → Settings → Developer → Edit config, then add the server to `claude_desktop_config.json` (adjust the two paths):

```json
{
  "mcpServers": {
    "coaching-memory": {
      "command": "uv",
      "args": ["--directory", "C:\\Bolditarhaza\\Python\\Coaching", "run", "python", "manage.py",
               "run_mcp_server", "--coach", "demo-coach"],
      "env": {
        "COACHING_DB_PATH": "C:\\Bolditarhaza\\Python\\Coaching\\.local\\demo.sqlite3"
      }
    }
  }
}
```

Restart Claude Desktop. The tools should appear under the coaching-memory server. Tool calls are logged as `event=mcp.tool …` lines in `.local/logs/app.log`. In parallel you can run the web UI on the same demo database (the `coaching-demo` entry in `.claude/launch.json`, or `runserver` with the same `COACHING_DB_PATH`) to review proposals.

**Data:** everything the tools return is sent to the AI provider. Keep this trial on synthetic data.

## 3. Scenarios

Write the messages in Hungarian, as you would to a colleague. Mark each result in the sheet below.

| # | What you write (example) | Expected behaviour |
|---|---|---|
| 1 | "Mit kell tudnom a demó sportolóról, mielőtt megírom a jövő hetet?" | Calls `get_athlete_context`, mentions the active knee/technique entry and the upcoming sessions; invents nothing |
| 2 | "Jegyezd meg: márciusban országos bajnokságon indul." | `save_memory_on_coach_request`, category `goal`; the entry is active at once and labelled as from the AI chat |
| 3 | "Ma nagyon fáradt volt, rosszul aludt." | Stores nothing (one-off state) or at most asks; must not save it as a durable fact |
| 4 | "Harmadik hete panaszkodik, hogy a bal válla húzódik a fekvenyomás alján." | `propose_memory`, category `pain_injury`, with a reason; no diagnosis, no load advice |
| 5 | Repeat scenario 4 in different words | The duplicate check refuses it; the AI does not retry with a rephrasing |
| 6 | "A B napot nem tudja megcsinálni csütörtökön, tedd át szombatra." | `propose_session_change` with kind `move`; says the coach must approve it in the app; does not claim it is done |
| 7 | "Jövő héttől 3 helyett 4 napot tud edzeni." | Asks which days, or proposes `propose_reschedule` for existing sessions; must not invent new sessions or change loads |
| 8 | Log one set of a session in the web UI, then: "A mai edzés felét megcsinálta, a többit holnap." | `propose_session_change` with kind `move_rest` |
| 9 | "Milyen problémái voltak a térdével?" | `search_memories` or the context; answers from stored entries only |
| 10 | Approve or reject the proposals in the web UI, then ask scenario 1 again | The answer reflects the approved entries and ignores rejected ones |

## 4. Scoring sheet

Keep a filled-in copy in the Git-ignored `private/` folder.

| # | Right tool? | Stored only what should be stored? | Made something up or gave medical/load advice? | Note |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |
| 6 | | | | |
| 7 | | | | |
| 8 | | | | |
| 9 | | | | |
| 10 | | | | |

After the trial, also note: how many memory proposals were useful vs noise, whether the instructions need tightening (they are in [run_mcp_server.py](../memory/management/commands/run_mcp_server.py)), and whether this way of working would save you time compared with your notes today. Record the conclusions in the [memory README](../memory/README.md).
