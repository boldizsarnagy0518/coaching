# Styling and responsive layout

[User interface](../templates/README.md) · Updated: 17 October 2026

## Responsibility

[app.css](app.css) defines the look of every screen: colour tokens for light and dark mode, type, spacing, lists, the set table, forms and status messages.

## Current state

**Visual direction: a coach's training logbook, not a marketing page.** Paper-and-ink colours, one signal colour (competition-plate red) used only for things that need attention, condensed signage-like headings, and lists and tables instead of card grids. Light mode by default, dark mode follows the operating system.

| Element | How it looks | Why |
|---|---|---|
| Colours | Off-white paper, near-black ink, muted grey text, red only for pending items, warnings and conflicts, green only for "done" | One meaningful accent; colour signals state instead of decorating |
| Type | Headings in Bahnschrift (Windows) / DIN Alternate (Apple), falling back to condensed system fonts; body in the system UI font; tabular figures for dates, weights and reps | A deliberate, gym-signage character without a web-font download; numbers line up in columns |
| Layout | Page header with a heavy rule, then lists and rows (athletes, plans, sessions, changes); the session page is a real table of prescribed vs actual sets | Coaches scan and compare; rows are denser and easier to compare than cards |
| Surfaces | Small 6 px radius, thin borders only where needed, no shadows, no gradients | Restraint; fewer visual effects that carry no meaning |
| Attention | Red left rule and red tags for pending proposals and changes; the dashboard says how many items wait | The next decision is the most visible thing on the screen |
| Spacing | A fixed 4–48 px spacing scale in CSS variables | Consistency across screens instead of per-screen tuning |
| Mobile | 44 px touch targets, rows stack below 600 px, the set table drops the index and RPE columns and uses a compact log button; no horizontal scrolling at 375 px | Logging happens on a phone in the gym |

**Not done:** a manual light/dark switch, a measured contrast audit with a tool, a real-device test (only emulated widths were checked).

## Decisions and reasoning

| Decision | Why? | Consequence / limit |
|---|---|---|
| Avoid the common "AI-generated" defaults: purple/blue gradients, an unchosen default font, three-card grids, uniform rounded cards with soft shadows, uppercase "eyebrow" labels, slogan copy | Research on generic AI-built UIs lists exactly these tells (sources below) | The app looks plainer, closer to a tool than to a landing page |
| Signal colour taken from the domain (competition-plate red) | A palette derived from the product reads as chosen, not default | Red must stay reserved for attention, otherwise it loses meaning |
| System font stack with a condensed display face instead of Google Fonts | No external request (privacy, offline gym use) and no font files to maintain | Headings look slightly different per operating system |
| Tabular figures instead of a monospace font for numbers | Alignment without the "code" look (tried monospace first; it looked like a developer tool) | Depends on the system font supporting tabular figures (Segoe UI, SF and Roboto do) |
| Concrete copy ("2 tétel vár rád", "Naplózás") instead of slogans | Specific text tells the coach what to do; slogans were the other main tell | Every new screen needs its own concrete wording |
| Readable, commented CSS instead of one minified line | Easier to maintain by hand | Slightly larger file; no build step needed |

Sources used for the direction: [925 Studios on AI design tells](https://www.925studios.co/blog/ai-slop-design-tells), [vibecodekit on generic AI UI](https://vibecodekit.dev/ai-slop-design), [Nielsen Norman Group on visual design principles](https://www.nngroup.com/articles/principles-visual-design/), and a [data-dense / fitness logging design note](https://claudskills.com/skills/data-dense-design/SKILL.md). These are practitioner guides, not formal research; the choices above are my own application of them.

## Verification

Checked in the browser on the demo database at 375 px (light and dark) and 1280 px: dashboard, plan, session table, memory page, change preview. The session table fits 375 px without horizontal scrolling (measured `scrollWidth` = `clientWidth`). No console errors. The template tests still pass (81/81 in the full suite).

## Next step

Show the screens to one or two coaches during the interviews and note where they hesitate; check contrast with a tool; try it on a real phone in the gym.
