# Styling and responsive layout

[User interface](../templates/README.md) · Updated: 17 October 2026

## Responsibility

[app.css](app.css) provides the app's colours, spacing, cards, forms and narrow-screen layout.

## Current state

One shared stylesheet works: dark background, light text, green accent, flexible card grid. Below 600 px, the important rows stack vertically. Inputs, selects, text areas and buttons are at least 46 px tall, and keyboard focus is visible. The memory screen adds row separators, button groups and a collapsible resolved-history panel.

**Not done:** light theme, a full component library, a measured contrast and accessibility audit, visual checks on multiple devices. Having responsive CSS does not replace these.

## Decisions and reasoning

| Decision | Why? | Consequence / limit |
|---|---|---|
| One CSS file, system fonts | No separate frontend build or external font dependency | As it grows, splitting it per component is worth considering |
| Shared colour variables | The base look can be changed in one place | Theme switching is not implemented yet |
| Larger touch targets and a single-column mobile view | A usable basis for input during training | A real phone test is still needed |
| Few visual elements | Emphasis on recording and on comparing prescription with performance | Analytical charts can come later |

## Verification

Serving the stylesheet over local HTTP has been checked. For visual changes, check the login page, long athlete and exercise names, form errors and set cards on both narrow and wide screens. Keyboard focus must remain visible.

## Next step

A first documented mobile usability and visual check, then fixing the issues it reveals. Tidying up the CSS formatting can be part of a later styling work package.
