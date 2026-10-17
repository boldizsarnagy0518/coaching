# Powerlifting AI App – Phase One Schedule (side project)

Prepared: 17 October 2026. **Version: 2.0** – revised for a side-project pace and the move to Dublin.

Related document: [Research and implementation plan](eroemelo_ai_kutatas_es_terv.md), especially sections 3.4, 4.1 and 12–16.

**What changed compared with 1.0?** Instead of 25 hours per week, the plan assumes 10 + 2 hours per week. The interviews and manual trials have been moved before the move. The week-2 gate has been replaced by a validation gate that also examines a trial of Kaizer and the measured time of manual adjustments. The development phase has grown from 3 weeks (about 60 hours) to 8 weeks (about 80 hours), and the AI part has been moved into a separate phase. As a result, the first internal trial is expected in work week 17 instead of week 8.

## 1. Goal and planning assumptions

**Outcome to reach by the end of phase one:** a prototype fit for internal use. It stores the existing plan and the actual training log, and proposes a verifiable adjustment for a missed or rescheduled session. The coach can accept or reject the change; the athlete sees the approved plan. In addition, there should be documented external interest, a measured manual adjustment time, a competitor test and a set of test cases.

A paid external pilot falls outside this phase. The outcome of this phase is not a finished public service.

### Capacity

- We assume one developer, with your involvement as a coach; the project is a side project.
- **10 hours of concrete tasks + 2 hours of buffer** per week, at most 12 hours in total.
- 17 work weeks: **170 hours of planned tasks + 34 hours of buffer ≈ 204 hours**.
- Of the main plan's 240–400 hour estimate, this is the portion up to the internal trial. Preparing and running the external pilot is further work after that.
- Interviewees' time is not counted in the developer hours; the organising and your participation are.
- Your technical proficiency, especially in frontend and authentication, is not yet known. That is why the development hour estimates are the most uncertain part.

| Actual weekly capacity | Calendar equivalent of the 204-hour budget, without a break for the move |
|---|---|
| 12 hours | 17 weeks |
| 8 hours | About 26 weeks |
| 20 hours | About 10 weeks |

With lower capacity, spread the same work packages over more weeks, but keep the order. Reserve the buffer for bugs, learning and slippage; do not fill it in advance with new features.

### Handling the move

The exact timing of the move is not fixed yet, so I am working with relative weeks.

- **Phase A (weeks 1–5) should take place before the move, in Hungary.** This includes the in-person interviews, the time measurement, the manual trials and the consultation with your own athletes. **At the latest, the validation gate (end of week 3) should be passed before the move.** If that does not fit, the tasks of weeks 4–5 can also be done remotely.
- **Plan a 2–4 week break around the move**, with no work hours. If you still make progress then, it is a bonus, not an expectation.
- **Phases B and C (weeks 6–17) are location-independent.** By then, the athlete and coach trials take place remotely, via video call or a short usability test.
- **Start:** week 0 should begin at least 7 weeks before the move, so that phase A and one week of margin fit in.

## 2. Schedule overview

| Week | Phase | Focus | Tangible weekly outcome |
|---|---|---|---|
| 0 | Preparation | Outreach | At least 8 coach and 6 athlete contacts, appointments |
| 1 | A – Validation (in Hungary) | Problem | Product brief, 10 own cases, first 3 coach interviews |
| 2 | A | Time measurement | Further interviews, at least 5 measured manual adjustments |
| 3 | A | Competitor and gate | Test of Kaizer and one further alternative, **validation gate** |
| 4 | A | Coaching logic | Rule catalogue, 20 detailed cases |
| 5 | A | Manual process | Manual walk-through of 5 cases, external review, draft data schema |
| — | The move | Break | 2–4 weeks, no planned work |
| 6 | B – Technical foundation | Technical spike | One athlete's complete data path, **technical gate** |
| 7–8 | B | Database and access | Plan versions, coach–athlete permissions |
| 9–10 | B | Logging and import | Mobile log, CSV import/export, partial session |
| 11 | B | Usability trial | Two remote usability trials, bug fixing, 30 cases |
| 12–14 | B | Plan adjustment | Rule-based proposal, before/after view, approval |
| 15–16 | C – AI and internal trial | Limited AI | Structuring free-text requests, two coach trials |
| 17 | C | Wrap-up | Bug fixing, 50 cases, **internal trial gate**, re-estimation |

**Rationale for the order:** first we check whether the adjustment process is valuable and time-consuming, and whether the closest competitor does not already solve it. Then we pin down the coaching rules and the data. The AI plugs into a process that can already be verified. This way it is clear whether an error stems from data handling, a rule or language interpretation.

## 3. Weekly tasks and acceptance criteria

### Week 0 – Outreach (about 3 hours, not counted in the budget)

Write to at least 8 coaches and 6 athletes, asking for a specific appointment. Do not contact only your own clients: at least 4 coaches should be independent of you. The starting list can be the first row of your own coach table described in section 4.2 of the main plan.

### Phase A – Validation before the move

#### Week 1 – Clarifying the problem

| Task | Planned time |
|---|---|
| One-page product brief: target group, change situation, expected outcome | 2 hours |
| Interview outline, note-taking and time-measurement template | 2 hours |
| Writing up 10 of your own cases, in a form that does not allow personal identification | 3 hours |
| First 3 coach interviews, with notes taken directly | 3 hours |
| **Total + buffer** | **10 + 2 hours** |

**Deliverables:** product brief, 10 cases (original plan, what changed, what decision you made, why), 3 sets of interview notes.

**The week is done when:** you can name the first supported situation, for example "a session was missed, and the athlete can train on other days". You also recognise the problem in at least one external coach's own story.

#### Week 2 – Interviews and time measurement

| Task | Planned time |
|---|---|
| A further 3 coach and 3 athlete interviews | 6 hours |
| Measuring the full time of at least 5 manual plan adjustments (with yourself and external coaches) | 3 hours |
| Summarising recurring problems and objections | 1 hour |
| **Total + buffer** | **10 + 2 hours** |

**How to measure time:** from opening the adjustment request until a verified plan that can be handed to the athlete. Looking things up, checking and informing the athlete are included. For each case, record the coach, the type of situation, the minutes, and roughly how many times per month such a case occurs.

**Deliverables:** a summary of 6 coach and 3 athlete interviews; at least 5 measured manual adjustments.

#### Week 3 – Competitor test and validation gate

| Task | Planned time |
|---|---|
| Trying out Kaizer with the same 3 powerlifting cases | 3 hours |
| One further alternative (e.g. RTS Training Lab or the current spreadsheet method) on the same cases | 2 hours |
| Simple demo with an old and an adjusted plan | 2 hours |
| Draft pilot offer and offering a concrete next trial | 2 hours |
| Decision note for the gate | 1 hour |
| **Total + buffer** | **10 + 2 hours** |

**Competitor test cases:** (1) a missed session, and the athlete can train on another day; (2) a partially completed session; (3) swapping a competition-lift variation, for example touch-and-go bench press instead of paused. Use the evaluation sheet from section 3.3. If you cannot actually use a product, mark this; reading the documentation is not a usability test.

**Validation gate – all three conditions must be met** (own target thresholds, can be refined after measurement):

1. **Demand:** at least 2 mutually independent external coaches show a similar problem and commit to a concrete next trial.
2. **Time cost:** the median of the measured manual adjustments is **at least 10 minutes**, and for the coaches concerned such a case occurs **at least 5 times per month**. Rationale: 5 × 10 minutes per month = 50 minutes, 30% of which is 15 minutes. It is hard to charge a monthly fee for a smaller time saving than that.
3. **Differentiation:** Kaizer (or the other alternative) handles at least one of the three cases visibly worse than the planned process. This could be mixing up variations, duplication, non-transparent changes or a lack of coach control over the plan. You can also describe this in one sentence.

**If the gate is not passed:**

| Missing condition | Action |
|---|---|
| Demand | New problem discovery in part of week 4; do not start development |
| Time cost | Turn towards the weekly coach summary (main plan 5.1), or keep it as your own internal tool |
| Differentiation | Narrow down to a powerlifting-specific situation that the competitor handles poorly; if there is none, stop the external-product direction |

Passing the gate is permission for further experimentation, not proof of market success.

#### Week 4 – Coaching rules

| Task | Planned time |
|---|---|
| Writing up decision rules and prohibited automatic operations | 6 hours |
| Expanding the case set to 20 detailed examples | 4 hours |
| **Total + buffer** | **10 + 2 hours** |

**Every rule needs:** a triggering event, required data, permitted change, prohibition, clarifying question and approving role. For example, for a partially completed session, completed sets cannot be moved as work to be done again. Separate shared constraints from the coach's personal methodological preferences.

#### Week 5 – Manual process and handover before the move

| Task | Planned time |
|---|---|
| Manual walk-through of at least 5 cases with the proposed process | 4 hours |
| External coach review and recording of discrepancies | 2 hours |
| Draft data schema and roles | 2 hours |
| Pre-move wrap-up: contact details, participants committed to remote trials | 2 hours |
| **Total + buffer** | **10 + 2 hours** |

**The week is done when:** you can carry the change through in five different cases and can say which step can be automated. There are at least 2 coaches and 2 athletes who commit to the later remote usability trial. Recognising missing data or a complaint report can also be a correct outcome; not every request has to end in a new plan.

### Break for the move (2–4 weeks)

No planned work. If you do find time, only do things that later decisions will not make redundant. Examples include reading the documentation of the chosen technology or putting together a synthetic test data set.

### Phase B – Technical foundation

#### Week 6 – Technical spike

| Task | Planned time |
|---|---|
| Technical spike of at most 8 hours | 8 hours |
| Finalising the feature list, dependencies and next tasks | 2 hours |
| **Total + buffer** | **10 + 2 hours** |

**Path of the technical spike:** one synthetic athlete → one plan → one logged set → result read back from the database, on a phone. Try a familiar Python solution; build a second version only if you hit a concrete obstacle.

**Technical gate:** the complete data path, the scope of supported adjustments and the acceptance criteria are in place. If the spike does not work even with the buffer, simplify the interface or the technology, and **update the estimate for weeks 7–14** before moving on.

#### Weeks 7–8 – Storage, plan versions and access

| Task | Planned time |
|---|---|
| Core database entities and reproducible schema changes | 6 hours |
| Plan versions and change history | 4 hours |
| Login and coach–athlete access | 7 hours |
| Permission and plan-history checks | 3 hours |
| **Total + buffer (two weeks)** | **20 + 4 hours** |

**Deliverables:** the basic structure of coach, athlete, relationship, exercise, plan and actual session. Updating the plan creates a new version; earlier completed work does not change.

**Done when:** it has been verified with two separate test coaches that they cannot read or modify each other's athletes. The backend must also reject the forbidden request; a different screen is not enough. This is first-round evidence, not a full security audit. Work with synthetic data; arrange the use of real personal data separately, as described in section 11 of the main plan.

#### Weeks 9–10 – Logging and plan entry

| Task | Planned time |
|---|---|
| Phone-optimised set logging | 8 hours |
| Handling partial sessions, resubmission and save status | 4 hours |
| One documented CSV import format, with preview and export | 4 hours |
| Displaying the current plan and actual completed work | 4 hours |
| **Total + buffer (two weeks)** | **20 + 4 hours** |

**Deliverables:** a program can be loaded, a session can be logged, and the saved data comes back when reopened. The interface distinguishes planned, completed, skipped and partially completed work. Resubmission does not duplicate sets; a failed save is not shown as successful.

**If it slips:** first simplify the convenience features of the import. Reliable saving and the actual training history must stay.

#### Week 11 – Remote usability trial

| Task | Planned time |
|---|---|
| Two short remote usability trials with athletes (video call, on their own phone) | 2 hours |
| Fixing the bugs found | 4 hours |
| Expanding the case set to 30 cases | 4 hours |
| **Total + buffer** | **10 + 2 hours** |

**The week is done when:** the participant records a session without continuous explanation. Measure speed, but set the final target value based on the outcome of the trial.

**Optional, out of the buffer:** getting to know 1–2 Dublin powerlifting coaches or a gym community. This is not selling yet, just an initial look at the later English-speaking market.

#### Weeks 12–14 – Rule-based adjustment and approval

| Task | Planned time |
|---|---|
| Rule-based processing of missed and rescheduled sessions | 10 hours |
| Handling the proposal, approval and new plan version | 7 hours |
| Before/after view and an explanation generated from the rule actually applied | 7 hours |
| Checking the core flows, version conflicts and 5 reference situations | 6 hours |
| **Total + buffer (three weeks)** | **30 + 6 hours** |

**Deliverables:** a concrete, verifiable proposal from a structured request. After approval, the new plan appears; on rejection, the approved plan remains available unchanged.

**Done when:** at least five reference situations work; there is no automatic duplication of already completed sets; an old approval arriving for a plan that has changed in the meantime triggers a new check. Violating a coaching constraint blocks the proposal from being issued.

Full 3→4-day replanning and exercise substitution are left for the next phase.

### Phase C – Limited AI and internal trial

#### Weeks 15–16 – AI interpretation and coach trial

| Task | Planned time |
|---|---|
| Structuring free-text requests and a short explanation | 6 hours |
| Validating AI output, follow-up questions and error handling | 6 hours |
| Two supervised, remote coach usability trials | 4 hours |
| Summarising time, cost and correction data | 4 hours |
| **Total + buffer (two weeks)** | **20 + 4 hours** |

**Deliverables:** for example, the sentence "I can train on Sunday instead of Friday" becomes a structured request. The system uses the existing rule process and shows how it understood the request. If a date is ambiguous or data is missing, it asks a follow-up question. The model on its own cannot rewrite the approved plan.

Before the API integration, there must be server-side secret management, a configured cost limit and orderly use of test data. If these are missing, the process can be tested with stub responses; in that case the AI part cannot yet be considered complete.

**Comparing the time measurements:** in the two coach trials, measure the full time of the adjustment in the same way as in week 2. This is the first comparison with the manual baseline. Because of the small sample, it is indicative, not proof.

#### Week 17 – Wrap-up and internal trial gate

| Task | Planned time |
|---|---|
| Fixing the most serious bugs | 5 hours |
| Extending the case set to 50 cases (35 development, 15 held out) | 3 hours |
| Re-estimating the next phase and a decision note | 2 hours |
| **Total + buffer** | **10 + 2 hours** |

**Internal trial gate:** the complete process works; the full time of an adjustment is shorter than the week-2 manual baseline; there is no known, open critical access or forbidden-modification bug. The small trial does not prove an effect on athletic performance or long-term retention.

If the AI does not add meaningful value compared with the structured form, develop the working logging and adjustment process further in the next phase. Keep AI quality improvement visible as a separate task.

## 4. Weekly work rhythm

| Work block | Time | Content |
|---|---|---|
| Week kick-off | 0.5 hours | One weekly outcome, concrete tasks and obstacles |
| Two to three focus blocks | 8.5 hours | Interviews, planning or development according to the weekly table |
| Review and weekly wrap-up | 1 hour | Walk-through, done/not done, actual hours |
| Buffer | 2 hours | Slippage, unexpected bugs, learning |

This is one possible split of the same 10 + 2 hours per week; planning and review are not extra time. A focus block should be at least 3 hours, because in development short, fragmented time loses a lot of its efficiency.

Only one main work package should be in progress at a time.

### Short weekly log

```text
Week:
Weekly goal:
Completed outcome / location:
Acceptance criterion met? With what evidence?
Planned / actual hours:
Buffer used:
External feedback:
Open bugs and obstacles:
Decision: continue / narrow down / retry
One main outcome for next week:
```

## 5. Handling slippage

| Situation | Action |
|---|---|
| A task slips by a few hours | Use the weekly buffer and write down the reason |
| The full buffer is used up for two weeks in a row | Re-estimate the remaining tasks; do not treat the week-17 deadline as unchanged |
| The validation gate does not fit in before the move | Do not skip the gate: make up the missing interviews remotely, and do not start development until then |
| No capacity for weeks after the move | Extend the break; continue the plan by weekly hours, not calendar dates |
| An interviewee is unavailable | Proceed with your own cases, but leave the demand condition open |
| Frontend needs more work | Simplify the layout and convenience features; save status must stay unambiguous |
| Too many different coaching methods come up | Narrow down to one chosen target profile and set of settings |
| There is a permission or forbidden-modification bug | Fixing it comes before expansion and before using external data |
| No noticeable time saving | Examine data entry and the review burden; do not try to cover it up with more AI features |

**Can be dropped first:** detailed charts, multiple import formats, visual polish, extra AI conversation, additional adjustment situations. **Core to preserve:** correct logging, permissions, plan versions, coaching constraints and approval.

## 6. Phase completion checklist

- [ ] We have documented for whom, and in what concrete situation, the tool is useful.
- [ ] All three conditions of the validation gate (demand, time cost, differentiation) have been met, with evidence.
- [ ] The evaluation sheet for the test of Kaizer and one further alternative is available.
- [ ] There are at least 5 measured manual adjustment times, with assisted times compared against them.
- [ ] The rule catalogue and the initial set of 50 cases are available.
- [ ] A program can be imported, and actual completed work can be logged.
- [ ] Access for separate coach accounts has been verified.
- [ ] The proposal for missed and rescheduled sessions can be compared with the old plan.
- [ ] Approval creates a new plan version, preserving past completed work.
- [ ] The system validates AI output; in case of an error, logging continues to work.
- [ ] There is no known, open critical bug in the supported process.
- [ ] The next phase (frequency change, exercise substitution, backup and restore, external pilot preparation) has been re-estimated based on the outcome of the trial.

## 7. Link to the research

This schedule is an execution breakdown of the existing research material. It does not contain new market prices or efficacy claims; the sources for the coaching and technological rationale can be found in the main document.

| Scheduling decision | Where the rationale is in the main plan |
|---|---|
| Coach-first launch and external interviews | Sections 4 and 13 |
| Time measurement as a critical assumption | Sections 4.1 and 15 |
| Kaizer test and differentiation | Sections 3.3 and 3.4 |
| Rules, missing data and review | Sections 6–7 |
| Database, versions and AI task split | Sections 8–9 |
| Data handling and feature boundaries | Section 11 |
| Work hours and overall project pace | Section 12 |
| Test cases and measurement gates | Section 13 |

The weekly hour breakdown and the gate target values (for example the time-cost threshold of 10 minutes and 5 cases per month) are my own planning proposals. They should be updated based on actual effort and measurements.
