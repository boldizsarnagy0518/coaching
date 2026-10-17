# Status, decisions and validation

[Project overview](../README.md) · Updated: 17 October 2026

## Responsibility

Keep the working product, the planned features and the not-yet-proven business assumptions clearly apart. The module READMEs, next to the code, show the local state and the reasoning behind decisions.

## Current state

| Document | Role |
|---|---|
| [Implementation status](implementation-status.md) | Short summary of what is done and what comes next |
| [Validation worksheet](validation-template.md) | Empty template for interviews, time measurement and the competitor trial |
| [MCP trial in Claude Desktop](mcp-trial.md) | Setup with a demo database, ten scenarios and a scoring sheet; not yet carried out |
| [CSV and Google Sheets](data-transfer/README.md) | Data transfer options, limits and the plan for a private connection |
| [Current schedule](../elso_szakasz_utemterv.md) | 17 work weeks, 10 + 2 hours per week, moving break and gates |
| [Research and product plan](../eroemelo_ai_kutatas_es_terv.md) | Sources, alternatives, pricing and professional hypotheses |

Market validation is still open. Writing code does not replace the interviews, the time measurement or actually trying Kaizer. The technical prototype was brought forward at the user's explicit request.

## Decisions and reasoning

| Decision | Why? | Consequence / limit |
|---|---|---|
| One README per module | When opening the code, it is visible where we are and why it was built this way | Must be maintained with every relevant feature change |
| One central index | The project stays easy to overview as a whole | Details are not copied into every document |
| Separate fact, plan and hypothesis | Nothing should look finished or proven when it is not | Every status claim needs verification evidence |
| Relative work weeks | Weekly capacity and the moving date can change | Calendar deadlines are agreed separately |
| English documentation, Hungarian UI | Code and docs stay readable for any developer or tool; users see their own language | UI strings and docs are maintained in different languages |

## Documentation rule for further development

1. Every new module with its own responsibility gets a `README.md`. Empty packages or individual files do not need their own description.
2. It contains: **responsibility; current state; what is missing; decision, reason and consequence; verification; next step; date of update**.
3. Rewrite the current state to match the code. When an earlier decision changes, briefly keep what replaced it and why.
4. Do not describe a proposed next step as a finished feature. The existence of a test command does not prove a successful run; record the result that was actually verified.
5. Details live primarily in the module README. Update the root index and the implementation summary only when the overall project state changes.
6. Code, tests and their documentation go into the same change. Use relative links so they also work on GitHub.
7. Never write personal data, passwords or API keys into documentation. A filled-in worksheet containing personal data belongs in the Git-ignored `private/` folder.

### README template for a new module

```markdown
# Module name

Updated: DD Month YYYY

## Responsibility
Which task does it handle, and which other part does it connect to?

## Current state
What actually works? What is missing or limited?

## Decisions and reasoning
| Decision | Why? | Consequence / limit |
|---|---|---|

## Verification
Command, test or manual check; last verified result.

## Next step
The next concrete work package and the open decision.
```

## Verification

For documentation changes, check that the text matches the code, that relative links resolve and review the Git diff. A purely textual change does not require new application tests.

## Next step

Collect real validation data and record the gate decision.
