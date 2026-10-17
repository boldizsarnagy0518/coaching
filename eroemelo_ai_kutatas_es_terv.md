# Powerlifting AI Application – Research and Implementation Plan

Research date: 16 October 2026. Prices are public list prices verified on that date; region, tax and sales channel may cause differences at checkout. Prices, time requirements and target values for your own product are planning assumptions, not proven market results.

**Document version: 2.1 – expanded decision and implementation document.** Version 2.0 examines the professional evidence, the counterarguments to the target-group choice, the development alternatives and the economics in more detail. Based on a more detailed work breakdown, it also revises the pilot effort estimate; the estimate in Chapter 12 is authoritative.

**The 2.1 change:** a supplementary online check on 16 October 2026. A one-page summary and the closest competitor found, Kaizer (Chapter 3.4), were added. The time-saving assumption is flagged as a critical, unmeasured risk. The first step of a Hungarian market survey and a pilot study on the acceptance of AI-generated training plans were added. The pricing, technical and scheduling sections did not change.

### How to read the conclusions

The document uses four different levels of evidence:

| Type | What does it mean? | What is it suitable for? |
|---|---|---|
| Verified product information | Official product page, price list or documentation | Comparing published features and business offers |
| Scientific result | An identifiable study with a known sample and method | A narrowly scoped exercise-physiology conclusion |
| My own planning proposal | An engineering/business decision derived from the sources and your situation | Choosing a starting solution |
| Hypothesis to validate | Not yet measured demand, price sensitivity, retention or time saving | Designing the next experiment |

A feature that exists according to the sources is not necessarily good quality or available in every plan. Conversely, a feature not found in the public documentation cannot be treated as a proven gap. I did not purchase the competitors described, nor did I run a multi-week controlled product test with them.

The scientific part is a targeted literature review, not a pre-registered systematic review. For several studies, the public abstract was the accessible evidence; where the full text was also available, I used it as well. I do not derive universal training rules from short, small-sample studies. The market part is based on vendor sources and one large subscription data report, not on a Hungarian customer survey.

**Reading path:** for the business decision, Chapters 1–5 and 10; for the professional logic, 6–7; for technical implementation, 8–9; for execution, 12–16; for source criticism, Chapter 17 is the most useful.

### One-page summary

**Recommendation:** a narrow, paid pilot of a plan adjustment assistant for powerlifting coaches that works with human approval. I do not recommend a standalone AI coach at this stage.

**The three most important, still unproven assumptions of the concept:**

1. Coaches spend meaningful time on plan adjustments, and an assistant reduces this even including the review. There is currently no independent measured data on this (Chapter 15).
2. There are enough Hungarian coaches who would pay for a separate tool. I found no public Hungarian market size data (Chapter 4.2).
3. Powerlifting-specific depth differentiates the product from the existing adaptive coaching tools with approval workflows (Chapter 3.4).

**Main risks:** a close competitor already exists (Kaizer); professional coaching software is available at a low price (RTS: 20 athletes for 79 USD/month); an AI-generated training plan on its own is easy to replace.

**The next two weeks:** write up 10 of your own adjustment cases; at least 4 coach interviews, measuring the adjustment time in minutes; try Kaizer and 2–3 other competitors on the same cases; finally, a go/no-go decision (Chapter 16.1).

**Condition for moving forward:** at least three coaches independent of you pay for the pilot and measurably save time (Chapter 13).

## 1. Recommended decision

The first thing worth validating is **an assistant that supports powerlifting coaches by adjusting existing training plans**. You can be its first user, followed by a few external coaches. The athlete logs on a simple mobile interface; the coach receives a reviewable change proposal that they can accept or edit.

The offer: "Based on the athlete's actual sessions and changing schedule, it prepares the next plan adjustment, shows the reason for it, and preserves the coach's programming principles."

This is a market hypothesis to be tested. The research did not prove that no competitor has such a sub-feature. The opportunity must be sought in solving this particular workflow better, and proven with a real usage trial.

The initial technical solution should be your own web application, your own database and an AI API paid for by the provider. MCP can later be a connection interface to the same system. A regular customer should not have to manage a developer key or a separate AI subscription.

## 2. What do we know about your background?

In this conversation you confirmed your three years of coaching experience. The available shared history shows the Python/MCP-based Business Central project and your AI-assisted development workflow. The "Erőbecslés konviban" conversation also shows your own powerlifting practice.

I found the "Claude profil összeállítása" conversation, but in the available tool the profile's response text appeared only as a content reference. I therefore do not consider the full shared memory as read. The history does not prove independent frontend, security or production operations expertise. Your weekly time budget, starting budget, current number of clients and external tester circle are still unknown.

Your relevant advantage is the combination of understanding coaching decisions and a practical interest in technical implementation. A small, supervised pilot is a realistic starting point. A standalone AI coach that handles every situation, with native mobile apps, video analysis and a custom-trained model, is a substantially larger undertaking.

### 2.1. How can your experience be put to use?

Three years of coaching practice becomes a development advantage if you can turn recurring decisions into concrete cases. For example: what signals made you change an athlete's weekly frequency; when an exercise swap was a preference and when a pain-related restriction; what data was missing for a good decision. A testable rule set and reference data can be built from this.

Your own method is an adequate starting point at first. Once external coaches are involved, however, you need to separate the professionally prohibited solution, the given coach's preference and an otherwise acceptable alternative. Two coaches making different decisions does not necessarily mean an error. The system must also handle the user coach's method and decision-making authority.

| Area | What the context supports | Next check |
|---|---|---|
| Understanding coaching decisions | You have three years of experience | Can you write down the conditions and reasoning of the decision for 20 real cases? |
| AI-assisted development | There is a shared Python/MCP project history | Can you debug, modify and test a small feature? |
| Product development | You have a concrete athlete problem statement | Can an unfamiliar coach go through the whole process without help? |
| Production operations and data security | Not enough context | Handling permission errors, backup-restore and service outages |
| Sales | Network and client count unknown | Can you reach 10 suitable interviewees and 3 external paying testers? |

**My own assessment:** the main risk is probably assembling and operating the complete service: proper logging, data quality, professional review, support and customer acquisition. A prototype built quickly with AI solves only part of these. At the same time, a working pilot can be a valuable professional and development portfolio result on its own, even if it never becomes a large software business.

## 3. Competitors and prices

The features below are the vendors' documented claims. I did not carry out a multi-week hands-on comparison in every product, and I do not treat marketing claims as independent evidence of effectiveness.

| Product | Main purpose and documented capability | Verified price | Implication for your own product |
|---|---|---|---|
| JuggernautAI | Powerlifting/powerbuilding, program that adjusts based on feedback | 34.99 USD/month or 349.99 USD/year | The general adaptive powerlifting app already faces strong competition. [Pricing](https://www.juggernautai.app/pricing) |
| Sheiko Gold | Planning that responds to daily readiness, variable frequency, exercise swaps | US App Store: 19.99 USD/month | Several elements of your listed adaptation ideas already appear on the market. [Product](https://sheikogold.com/), [price](https://apps.apple.com/us/app/sheiko-gold-powerlifting-ai/id1475890027) |
| Fitbod | Personalization based on training history, goal, equipment and recovery | Web: 15.99 USD/month; 95.99 USD/year | For a broader strength-training audience you would also compete with a versatile product. [FAQ](https://fitbod.me/faqs/) |
| Boostcamp | Training programs, logging, analysis | Free base; Pro 14.99 USD/month or 59.99 USD/year | A plan and a log on their own are hard to price as premium. [Pro](https://www.boostcamp.app/pro) |
| TrainHeroic | Coach program building and athlete management | 5 athletes: 17.99; 15: 34.99; 25: 44.99 USD/month | The coach administration interface is also an established category. [Prices](https://www.trainheroic.com/coach/) |
| MyStrengthBook | Individual programming and coaching business | PULL: 3.99 USD/client/month; PUSH: 20% revenue share | Per-athlete pricing and distribution through coaches are relevant models. [Prices](https://mystrengthbook.com/pricing-coaching) |
| Everfit | Coaching platform, AI that structures workouts from text, client communication | Free base up to 5 clients; Pro with monthly billing 29 USD/10, 49 USD/20 clients | The "AI for coaches" claim on its own is not differentiating either. [Prices](https://everfit.io/pricing/), [AI](https://help.everfit.io/en/articles/9373485-introducing-ai-workout-builder) |
| RTS Training Lab | Powerlifting programming, analysis of athlete responses, professional support | 10 athletes: 49; 20: 79; 30: 99 USD/month | A direct professional benchmark for coaching decision support. [Product and prices](https://rtslab.reactivetrainingsystems.com/) |
| Kaizer | Coaching platform; by its own claim it recalculates load and reps after every logged session, the final decision is the coach's | I found no central price; it mentions country-specific pricing | The closest competitor found for the proposed workflow; see 3.4. [Its own comparison article](https://kaizer.app/en/blogs/best-personal-trainer-software-2026) |

A separate JuggernautAI campaign page shows a different price; here I used the central pricing page. I do not record Sheiko's annual price as a single definite amount: the App Store description and its purchase list show different annual amounts. I also looked for the Evolve Training App, but found no consistently verifiable current central monthly fee, so I did not include an uncertain price in the table.

For many coaches, the real alternative is their existing spreadsheet and messaging app, possibly a general AI assistant. Your own product must also earn back the cost of switching or of an extra tool. Initial import/export can reduce this, but automatic integration with a third-party platform may only be promised after actual API access has been verified.

### 3.1. What can we learn from the different competitor groups?

**JuggernautAI and Sheiko Gold:** the professional method and the trust associated with it are an important part of the offer. My conclusion is that your initial application needs decision principles that can be presented credibly. The user must understand by what method they receive a proposal. Sheiko's public description explicitly mentions variable schedules and exercise swaps; these on their own cannot be positioned as a unique innovation. [JuggernautAI](https://www.juggernautai.app/pricing), [Sheiko Gold](https://sheikogold.com/)

**Fitbod and Boostcamp:** an easy-to-use log and access to the program are a customer expectation in their own right. The planning conclusion is that the quality of the interface the athlete sees matters even if the coach pays. If set logging is inconvenient, there will be little data, and adaptation will also be weak. [Fitbod](https://fitbod.me/faqs/), [Boostcamp](https://www.boostcamp.app/pro)

**TrainHeroic, MyStrengthBook and Everfit:** the coaching workflow consists of many interconnected features. Replacing a full platform means significant development and switching cost. That is why for the first pilot I recommend supporting one designated program and one narrow adjustment process. Everfit's documented AI workout builder also structures free-text program descriptions; free-text input can therefore be a useful base feature, but it is weak as a standalone market advantage. [TrainHeroic](https://www.trainheroic.com/coach/), [MyStrengthBook](https://mystrengthbook.com/pricing-coaching), [Everfit AI](https://help.everfit.io/en/articles/9373485-introducing-ai-workout-builder)

**RTS Training Lab:** the product offers programming, trend tracking and adjustment based on athlete responses, together with a professional community. My own conclusion: serious, domain-based competition exists in the coach target group as well. We cannot consider the "decision support" category empty. [RTS](https://rtslab.reactivetrainingsystems.com/)

### 3.2. Comparable coach cost: 20 active athletes

The calculation below is derived from the price lists above, without discounts or any taxes. It does not claim that the plans are functionally equivalent.

| System | Published monthly base price for serving 20 athletes | Calculation |
|---|---:|---|
| TrainHeroic | 44.99 USD | 25-seat plan required |
| Everfit Pro | 49 USD | 20-client plan, monthly billing |
| MyStrengthBook PULL | 79.80 USD | 20 × 3.99 USD |
| RTS Training Lab | 79 USD | 20-athlete plan |

This justifies two separate price tests. If your app replaces an existing system, it will be compared with the price of the full platform. If it is a complementary tool, it must create value on top of the existing subscription. The same monthly fee of 15,000–25,000 HUF can come across very differently in these two situations. The interview should therefore also record current software costs and the intended mode of use.

### 3.3. Plan for the actual competitor test

The next research step should be trying 3–4 selected products on the same cases; one of them should be Kaizer (Chapter 3.4). The study can be carried out separately, with authorized access; the table below is a test plan, not a completed comparison.

| Test scenario | What to measure? | What counts as a good result? |
|---|---|---|
| Entering a four-day plan | Time, manual corrections, lost fields | The coach's method and exercise variations are preserved |
| Skipping a session | Rescheduling time, required manual steps | The change is transparent, no work is duplicated |
| Switching to three training days | Change in distribution and load | It is clear what was kept and why |
| Exercise swap | Handling of history and load | Data of the variations is not mixed without review |
| Missing RPE data | Does the system ask or assume? | The uncertainty is visible |
| Pain report | Automatic and human steps | No unjustified, confident load prescription is made |
| Coach overrides a proposal | Traceability and later use | The decision and its scope are preserved |
| Leaving the system | Data extraction and portability | The athlete's log remains accessible as an export |

Evaluation sheet: product version, plan, test date, input case, elapsed time, manual modifications, uncertain result, supporting screenshot. A missing feature is only marked as missing after a trial or clear documentation.

### 3.4. Supplementary check: the closest competitor and differentiation

The 2.1 check focused on the coaching workflow. Its main question: does a tool already exist that proposes plan adjustments based on athlete feedback and has the coach approve them? Most sources are vendor blogs or comparison sites; some of these are marketing material written by competitors. The items below are therefore claims to be tested, not proven facts.

| Product | Claim found | Type of source |
|---|---|---|
| Kaizer | Recalculates e1RM, load and reps after every logged session; the final decision is the coach's. The article does not detail the approval process. | Own blog. [Source](https://kaizer.app/en/blogs/best-personal-trainer-software-2026) |
| RTS Training Lab | Mentions adjustment based on athlete responses and monitoring metrics; does not mention AI. According to the description, the adjustment decision is the coach's. The log is free for athletes. | Official product page. [Source](https://rtslab.reactivetrainingsystems.com/) |
| TrueCoach, Everfit, TrainHeroic | According to comparison articles, AI is used at most for plan or text generation. TrainHeroic has rule-based RPE autoregulation. | Third party, partly competitors. [Trainerfu](https://www.trainerfu.com/blog/everfit_alternatives/), [Everfit blog](https://blog.everfit.io/everfit-vs-trainerize-vs-truecoach) |
| JuggernautAI, Titans Grip, Strength Coach AI | Adaptive programming directly for the athlete; I found no coach interface or approval process. | Reviews, store description. [GGR](https://garagegymreviews.com/juggernautai-review), [Titans Grip](https://www.titans-grip.com/blog/best-powerlifting-app-2026/) |

**Conclusion:** according to its own description, Kaizer already offers the "adjusts based on feedback, the coach decides" pattern. Professional recommendations also point in this direction: for meaningful changes and pain reports, coach approval should remain. [Coaching Portal](https://coachingportal.io/blog/ai-fitness-coaching-trends) This does not refute the concept, but the four capabilities in Chapter 5 are not sufficient differentiation on their own.

**Possible bases for differentiation** (my own planning proposal, to be validated):

- **Powerlifting-specific logic:** separating competition-grip variations, the source and reliability of RPE/RIR data, peaking for competition, handling missed work according to the block goal. A general coaching platform typically does not model this in detail.
- **Incorporating the coach's own method:** the programming logic is not given by a built-in formula (e.g. an NSCA table); it is defined by the coach's rules and prohibitions.
- **Transparent diff view and reasoning:** the coach sees what changed and because of which rule.
- **Hungarian language and personal onboarding:** an initial access advantage, but easy to copy on its own.

**To do:** Kaizer must be tried with the test plan in Chapter 3.3, on the same powerlifting cases. If it also performs well on powerlifting cases, your own product must be positioned more narrowly, or rather turned toward the weekly coach summary (Chapter 5.1).

## 4. Coaches or athletes?

| Direction | Who pays and why? | Starting advantage | Biggest difficulty | Assessment |
|---|---|---|---|---|
| Coach assistant | Coach; time saving, clearer decisions | You can start from your own coaching routine, can be validated with few buyers | Different methods, resistance to switching, professional control | I would test this first |
| Standalone adaptive app for regularly training athletes | Athlete; usable plan and fast adaptation | Clear, daily problem | Existing apps, retention, trust, customer acquisition | Good as a second step |
| App for the merely curious | Beginner; orientation, motivation | Broader theoretical audience | Uncertain training habits and willingness to pay | Too broad as a starting target group |
| AI-assisted own coaching | Your own client; personal coaching service | A real workflow can be tested even with little development | Revenue remains tied to your time | The best first experimental round if you have clients |

I would describe the first external coach target group as follows: works with 10–30 active powerlifting/strength athletes, adjusts plans regularly, pieces the situation together from several data sources, and is willing to try a new tool. This is a research target profile, not a verified market size.

If you later choose the athlete direction, the segment "has been training regularly for at least a few months, knows the basic lifts, but their schedule changes" is more concrete than the general curious user. The Hungarian language and close relationships can give good initial access; the Hungarian language on its own is an easily copied advantage.

### 4.1. Why is starting with coaches advantageous, and when would it still be a bad decision?

The following arguments favor starting with coaches: you can provide reference cases from your own experience; the coach evaluates the proposal, so errors are recognized early; the time saving can be converted into financial value; a few clients are enough for a first usage sample. These are planning arguments, not proven Hungarian market data.

**Critical, unmeasured assumption:** for the time-saving argument I found no independent measurement of how many minutes coaches spend on plan adjustments. Figures like "10+ hours of administration per week" come from companies selling coaching software and refer to administration as a whole, not specifically to plan adjustment. [Example of a vendor claim](https://www.trainerfu.com/blog/how-ai-fitness-coaching-saves-trainers-10-hours-per-week/) The pricing and value-proposition logic of Chapter 10 largely rests on this, so the first measurement goal of the interviews should be to record it in minutes.

The counterarguments are just as important. The coach may be satisfied with their current system. Adjustment may seem like one of their most valuable professional tasks, which they do not want to hand over. A new application can initially cause extra administration. If every client wants a completely different method, the application can easily turn into a custom development service.

| What you find in the research | Consequence |
|---|---|
| Coaches show a recurring, time-consuming problem and are willing to bring in data | The coach assistant can be continued |
| Coaches mainly want an overview and would not hand over programming | Narrow down to an analysis and summary product |
| Athletes are already actively looking for a solution, but coaches are not interested | A narrow athlete pilot may be justified |
| Only your clients use it, no external coach pays | Can be monetized indirectly as an internal coaching tool |
| Every coach asks for a separate feature set | A unified target profile or product boundary is missing |
| The main problem is the lack of basic data | The logging and feedback process must be solved first |

### 4.2. A verifiable outreach plan instead of market size

I found no verified, sufficiently narrow public data from which the number of Hungarian powerlifting coaches able to pay could be reliably calculated. A general global fitness market size does not replace this. For initial planning, the number of reachable customers must be built bottom-up.

Example scenario: from 40 relevant coaches, 20 conversations, of which 8 demos, 5 pilots and 3 paid continuations. These are experimental planning numbers, not expected conversions. The list can be assembled from personal contacts, gyms, coaching courses and professional communities. At every stage, record separately why someone dropped out.

If thirty paying coaches is the next business goal, and in the actual process 10% of properly approached coaches become subscribers, roughly 300 suitable prospects are needed. The 10% here is purely a calculation assumption. This makes it visible that, besides development, customer acquisition also requires regular time.

**First step toward surveying the Hungarian market:** the 2.1 check also found no public data on the number of competitors, clubs or coaches of the Hungarian powerlifting federation(s). Note: Hungarian competitions are organized by several bodies. A suggested starting point is your own spreadsheet containing at least 40 relevant coaches. Possible sources: result lists of domestic competitions and the clubs listed there, Hungarian lifter data in [OpenPowerlifting](https://www.openpowerlifting.org/), contacting the federations directly, gyms specializing in powerlifting, and coaching courses and communities. Each row should include the source, the estimated number of athletes, the tool currently used and the means of contact. If not even 40 relevant coaches can be identified, that in itself is a strong signal of a narrow market.

### 4.3. What do subscription app data say?

RevenueCat's 2026 report analyzes data from more than 115 thousand apps, typically for a 2025 period. In the AI category, the 12-month retention median of monthly subscriptions is 6.1%, in the non-AI category 9.5%. The sample contains apps that use RevenueCat and meet an activity/revenue threshold; not the whole app market, and not Hungarian powerlifting SaaS products specifically. The correlation does not prove that AI causes the lower retention. [Report and methodology](https://www.revenuecat.com/state-of-subscription-apps)

My own conclusion: the initial key metric should be returning usage and paid renewal. Creating the first training plan is only the first moment of value. The second and third moments of value are handling everyday changes, the coach's time saving and the continuous usability of the history.

An annual fee can bring money up front, but it can mask a decline in actual usage. For this reason, paying status, logged sessions and completed coach reviews must be measured separately.

## 5. What should make it valuable?

I would build the differentiation on four interconnected capabilities:

1. It takes in the coach's existing program and rules.
2. It handles the work actually done separately from the prescribed plan.
3. It proposes only the necessary changes, while preserving the original goal.
4. It shows the difference between the old and new plan, the data, the reasoning and the uncertainty.

Example: "Friday's session was missed, I can go on Sunday, and from next week four days fit in." The assistant identifies the missed session, examines the upcoming sessions and the goal of the block, then prepares an adjustment proposal. On a single screen the coach can see which exercise moves where and how the load changes.

The measure of success should be that reviewing and correcting the proposal together take less time than manual re-planning. A good textual explanation on its own does not prove this.

### 5.1. Three product variants for the same problem

| Variant | What does the product do? | Why could it be good? | Why could it be insufficient? |
|---|---|---|---|
| Weekly coach summary | Highlights missed sessions, deviations and athletes needing attention | Relatively easy to verify, smaller intervention | Rewriting is still left to the coach |
| Plan adjustment assistant | After the summary, prepares a concrete change | Directly targets the time cost of the workflow | Requires reliable data and a precise professional framework |
| Standalone athlete planner | Issues the next session directly | Less daily coach involvement, broader reach | More autonomous decisions, larger quality and support burden |

I would build development from the first variant toward the second. That way the system is already testable while you are still making the adjustments by hand. The third variant only has a strong foundation if, with the second, it is already known in which cases the proposals can be trusted.

### 5.2. What should the interface show?

Coach main view: which athlete needs attention, what changed, what data is missing, and which plan adjustment is awaiting approval. It should not simply show lots of charts; the interface should make the next required decision visible.

Athlete main view: today's session, next set, previous relevant performance, quick logging and a "my situation changed" button. Short input options: different day, less time, missing equipment, exercise preference, pain report. Free text should be an optional addition.

Adjustment card: affected days and exercises; previous/new prescription; data used for the decision; unknown factors; coach rule; approve/edit/reject. The explanation should be generated from the rule and data actually applied. We should not let the model invent, after the fact, a professional reason that was not part of the decision.

## 6. What does a "continuously learning" application mean?

It is worth handling three different levels separately.

**Persistent memory:** stores plans, completed sets, RPE, schedule, preferences and coach decisions. This is database management, not model training.

**Per-person adaptation:** updates the performance estimate and the parameters of the next proposals. For example, it tracks the difference between target RPE and actual RPE, the completion rate and the per-exercise trend. Rules and statistics are sufficient for this initially. A single bad day does not prove a lasting decline; nor should conclusions with false precision be drawn from missing data.

**Developing the whole product:** you evaluate the accepted, edited and rejected proposals, then improve versioned rules or models. Coach acceptance may indicate process quality, but does not prove better sporting results. Long-term outcomes and different athlete groups must be examined separately.

The MVP needs the first two levels. Training your own language model and automatic, live self-rewriting are not justified. Model fine-tuning can be considered later, with high-quality data collected on a proper legal basis and a separate evaluation set.

Autoregulation is a professionally researched approach. In an eight-week study with 21 trained men, strength improved with both RPE-based and percentage-based loading; the difference between groups was not significant. This supports the usability of RPE, but does not prove the superiority of an AI application, and cannot automatically be generalized to every athlete. [Helms et al., 2018](https://pubmed.ncbi.nlm.nih.gov/29628895/)

### 6.1. A more detailed literature base and limitations

**Frequency and volume.** Saric et al. assigned 27 trained men to three or six sessions per week for six weeks, with equal training volume. Both groups got stronger; no significant group difference in strength gains was found. This is a short study limited to male participants, not a rule that defines an individual optimum. [Saric et al., 2019 – public abstract](https://pubmed.ncbi.nlm.nih.gov/30363041/)

My product design conclusion: a change in the number of days should primarily be handled as a scheduling and load-distribution problem. The weekly amount of work should be a separate decision. The research does not prove that any frequency is interchangeable for every powerlifter, or that volume can be packed into short sessions without limit.

**Accuracy of RIR estimation.** In a study with 58 participants, estimates were more accurate closer to failure and in later sets. Under the studied conditions, sex and training history showed no significant effect on the error. The tasks included biceps curls, triceps pushdowns and seated rows; this limits direct generalization to competition deadlifts. [Remmert, Laurson and Zourdos, 2023 – abstract](https://pubmed.ncbi.nlm.nih.gov/37036795/)

My product design conclusion: a self-reported RPE/RIR value is a useful signal, but not an instrumented measurement. The system stores who entered it, which set it refers to, and whether it is an actually entered or an estimated value. Set RPE and session RPE should be separate fields.

**It is not guaranteed that accuracy improves merely with time.** In a six-week bench press study with nine trained men, the absolute RIR estimation error did not improve significantly. Because of the small sample, this is not a definitive answer either, but it justifies not taking the assumption "more logs = automatically better measurement" for granted. [Remmert et al., 2023 – publisher's abstract](https://journals.sagepub.com/doi/10.1177/00315125231189098)

**A newer, partly different result.** A ten-week study from 2025 was completed by 31 trained participants. With a variable RIR target and a constant 1 RIR, no significant difference was found in changes in strength and muscle size; the variable group's average session RPE was lower. Certain RIR estimates improved within the variable group, but the between-group difference in the change in accuracy was not significant. Participants also received feedback and partial supervision. [Martikainen et al., 2025 – full text](https://link.springer.com/article/10.1007/s42978-025-00338-8)

My own conclusion from the two accuracy studies: it is worth providing education and feedback, but the system should not automatically raise the reliability of a data point merely based on the number of weeks of use. User-specific, verifiable consistency must be measured.

**Fatigue and proximity to failure.** In 24 trained women and men, in a six-set bench press protocol, Refalo et al. measured greater acute fatigue with execution closer to failure. The study concerned one specific exercise and a short recovery period. [Refalo et al., 2023 – full text](https://link.springer.com/article/10.1186/s40798-023-00554-y)

My product design conclusion: besides the weight × reps × sets completed, the subjective difficulty of the load may also be relevant. A universal 48-hour rest rule for every athlete and every exercise cannot be derived from this. The application should not claim objectively measured recovery from data that are only indirect signals.

### 6.2. Conclusions on how personalization should work

Proposed first state model per exercise: last relevant performances; prescribed and actual difficulty; completed/planned work; missing data; variation; last update; coach restrictions. "Readiness" should initially appear as several separate observations, not as an unexplainable 0–100 score.

For an athlete with little data, the starting plan is provided by the coach or an approved template. The goal of the first weeks is recording and recognizing large deviations. Even with more data, uncertainty should only narrow where truly comparable sets exist. Changes in the exercise, rep range, execution and conditions can reduce comparability.

For e1RM estimation, the version of the formula or method and the source set must be stored with every value. The e1RM trend should not be displayed as a measured competition maximum. After an exercise swap, a new data series or an explicitly marked link is needed; paused and touch-and-go bench press are not the same data point.

To prove personalization, compare the system against a simple baseline: the coach's original plan and pre-defined adjustment rules without personal history. If adding the history does not improve the usability of decisions or the time required, the extra complexity is not yet justified.

### 6.3. How should the product improve from coach decisions?

Selectable reasons on rejection: incorrect data; unsuitable exercise; change too large; methodological preference; missing context; correct proposal, but wrong timing. These are different errors requiring different fixes. A bare "accepted/not accepted" label is not enough.

When correcting, the coach should be able to mark whether it applies only to that occasion, the athlete, the block or their own method. A one-off exception must not be automatically applied to all future sessions. I would introduce a global rule change as a controlled release, run against a test set.

The purpose of using data for research or model development must be defined separately. Just because someone uploads their training log to the service does not justify using it for every future training purpose. For the coach's own templates and paid third-party programs, usage rights must also be clarified.

## 7. Adapting to the situations you raised

The following are proposed product behaviors; the specific load limits are determined by coach protocol and testing.

| Event | Task of the system | Important limitation |
|---|---|---|
| Switching from 3 to 4 days per week | Distributing existing work, taking available time and rest days into account | The extra day does not automatically mean one-third more load |
| A session is missed | Mark it as missed; examine what is justified to move or drop | All missed work should not automatically pile up |
| A session is shifted | Rechecks the following days based on actual dates | The calendar week is not necessarily the same as the physiological load unit |
| Exercise swap | Pre-approved alternatives based on goal, equipment, movement variation and restriction | It should not blindly copy the weight or e1RM of one variation to another |
| RPE higher than expected | Records the deviation; prepares a proposal based on rules | One data point is not enough for a new long-term profile |
| Pain/injury report | Flagging, stopping automatic load increases for the affected area, human review | Does not diagnose; does not automatically declare a substitute exercise safe |
| Longer break | Fresh assessment and a coach return plan | It should not automatically continue with the last working weights |

Initially, every professional adjustment should go to approval. Later, within limits set by the coach, some simple changes can be automated, but every change should be logged and reversible.

### 7.1. Case study: switching from three days to four

Illustrative situation: instead of Monday–Wednesday–Friday, Monday–Tuesday–Thursday–Saturday fits. The application first clarifies from when the change applies, how many minutes are available, and whether it is a one-off or a lasting adjustment. It then distinguishes the main lifts, the accessory work and the priorities set by the coach.

Proposed processing: it only affects future sessions; it redistributes work within a designated planning window; it checks the rest and load limits set by the coach; it shows which day changed. If the plan does not fit under the given conditions, it should flag this and ask for a decision on the elements that can be dropped. Filling the weekly calendar must not take precedence over the coach's limits.

### 7.2. Case study: missed and partial session

"The session was missed" and "I only did the main lift" are two different events. In the former, the status of the planned session changes; in the latter, the completed sets must be kept, and only the remaining work needs to be evaluated. Moving a partially completed session in full would cause duplication.

Acceptance criterion: an already completed set appears once in the totals; dropped and moved work can be distinguished; the athlete's next view shows the same approved plan version as the coach's.

### 7.3. Case study: exercise swap and pain

First, the reason for the swap should be structured data: equipment occupied, equipment missing, personal preference, coach decision or complaint. Missing equipment and pain are not the same decision path. For the former, a pre-approved substitution list can help; for the latter, the system should record the report and route it to human review.

The product cannot conclude that a movement is pain-free or appropriate merely because it works a similar muscle group. A restriction given by a professional is separate data, with a validity period and source. This feature boundary makes it possible to handle injury reports in the pilot while the person responsible for rehabilitation decisions remains clear.

### 7.4. Change levels

| Level | Example | Initial approval |
|---|---|---|
| Data recording | Athlete corrects a mistyped rep count | Confirmation and change log |
| Scheduling proposal | The next session would move to a new day | Coach |
| Professional adjustment | Load, volume or exercise would change | Coach |
| Restricted case | Pain, longer break, contradictory data | Human review, an appropriate professional if needed |

Automation should be expanded case family by case family. Well-functioning calendar rescheduling does not prove that post-injury load decisions can also be automated.

## 8. API, your own key or MCP?

An API is one technical route for calling a model. An API key is an authentication tool. MCP is a protocol through which an AI client can access data and operations. The subscription is a separate business decision from these. [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture)

| Solution | Payment model | User experience | Recommendation |
|---|---|---|---|
| Own app + provider API key | The client pays you; you pay for AI usage | Simple sign-in, own interface | I would choose this for the first paid product |
| Own app + client's API key | Software fee to you, usage fee to the AI provider | Managing keys, billing, limits | At most for a technical pilot or a specific business need |
| MCP for an existing AI client | Own service fee and AI access under the client's terms | The user works from an AI client | Good as an advanced coach feature or for your own prototype |
| Using a ChatGPT plan in your own app | Requires a separately supported integration and authorization | Potentially convenient, but access-dependent | Do not base the initial business model on this |

Even with MCP, Codex is not conceptually required: the chosen client must support the connection. The cost of the client model is borne by its access model; your backend and any separate model calls of yours still cost money. MCP on its own does not start scheduled analysis and does not provide a model subscription. Scheduling must be provided by your own application or a supported feature of the client.

OpenAI's current documentation already describes a Sign in with ChatGPT option that, in open-source, locally running applications, uses the user's ChatGPT plan for authorized requests. For paid or remotely hosted apps it indicates a separate expression-of-interest process. So it is not accurate to say that subscription-linked usage is never possible; however, it must not be relied on as a generally available SaaS foundation. [Official overview](https://developers.openai.com/siwc/token-sharing-open-source), [limitations](https://developers.openai.com/siwc/token-sharing-open-source/preview-limitations)

## 9. Technical first version

Proposed architecture: phone-optimized web interface → Python backend → PostgreSQL database, rule engine and AI service. MCP can later expose verified operations of the backend. There should not be separate business logic in MCP and in the application.

For Python, FastAPI/Pydantic is a reasonable starting point with structured inputs; the final framework should depend on your actual proficiency. Supabase is one possible managed PostgreSQL and authentication solution; its Pro plan currently starts at 25 USD/month. [FastAPI](https://fastapi.tiangolo.com/features/), [Supabase](https://supabase.com/pricing)

Simple web forms may be sufficient for the first coach prototype. For the athlete version, fast set logging, large touch targets and reliable saving matter more than a flashy chat. The first pilot should have at least a local draft and safe resubmission; full offline sync can be a later development. A native iOS/Android app is not needed for the first validation.

Minimum data: user and coach–athlete permissions; athlete profile; exercise catalog and variations; plan versions; planned sessions; completed sessions and sets; short status reports; adjustment events; proposals and approvals; AI usage and decision log.

The AI can interpret the natural-language request and write the explanation. The numerical plan should be produced or verified by the rule engine. Besides type checking, professional checks are also needed: a response being valid JSON does not mean it cannot be a bad training plan.

The flow of an adjustment: request → structured event → load current state → proposal → rule check → before/after view → approval → new plan version. An approval arriving for an old plan version requires rechecking; a log submitted twice should not create a duplicate session.

A new plan should not rewrite completed training history. The LLM should not get free SQL or administrator access. The API key should stay on the server. In case of a model failure, logging and the already approved plan should keep working.

### 9.1. Technology alternatives and reasons for the choice

| Architecture | When is it a good choice? | Extra burden | Recommendation |
|---|---|---|---|
| Simple Python web prototype | Own use, manual supervision, internal decision experiment | Later development of the mobile log and permissions | For early proof of operation |
| Django + PostgreSQL + simple web interface | One developer, many data-handling screens, administration | Separate design of the API and rich mobile interaction | Strong alternative for a Python-centric start |
| FastAPI + separate mobile-friendly frontend + PostgreSQL | API-centric system, later MCP and multiple clients | Two technology layers, more integration points | I would choose this if you can also handle the frontend |
| Managed database/authentication + own application | Handing over part of the operations tasks | Provider cost, correct handling of settings and permissions | Can be practical for a pilot |
| Native or shared-codebase mobile app | Proven mobile usage, justified device integration | Release, app store and platform testing work | To be reassessed after evidence of retention |

Django provides built-in data model and administration capabilities; this can reduce the initial assembly work of a single-developer data-handling application. However, the admin interface is not a finished athlete product interface. The choice assessment above is my own conclusion from the documented capabilities. [Django overview](https://docs.djangoproject.com/en/5.2/intro/overview/)

The earlier FastAPI recommendation is therefore not an exclusive decision. In a two-day technical trial, it is worth building the full path of one athlete, one plan and one logged set with the solution you are more familiar with. The version that is easier to modify and debug may matter more than the theoretically more elegant architecture.

### 9.2. Data model – what needs to be stored separately and why?

| Entity | Important data | Reason |
|---|---|---|
| Coach–athlete relationship | Role, permission, start/end | Data access should not depend on the athlete ID supplied by the client |
| Athlete profile | Goal, availability, equipment, experience | Lasting circumstances are kept separate from a single session note |
| Exercise and variation | Identifier, execution, equipment, related alternatives | Mixing up different variations can be avoided |
| Plan version | Block, goal, author, version, validity | It is traceable what was in effect at the time of a given session |
| Planned session/set | Date, target reps, load, target RPE | The prescription can be analyzed on its own |
| Completed session/set | Actual time, weight, reps, RPE, status | The actual work is not lost when re-planning |
| Status report | Source, time, type, validity | An old report is not treated as current forever |
| Change request | Reason, requested dates, affected plan version | The trigger of the decision can be reconstructed later |
| Proposal and decision | Diff, rule version, approver, reason for edit | Quality and coach overrides become measurable |
| Technical run | Model version, duration, token usage, error code | Cost and the origin of errors can be understood |

The first import should be a documented custom CSV schema, with a sample file and field validation. "Understands any Excel/PDF plan flawlessly" is a separate project: one cell can contain several exercises, a percentage, RPE, a note or a formula. After import, a preview of the interpreted plan should be mandatory. A back-reference to the original file can help with debugging, within the retention rules.

### 9.3. The precise division of tasks between the AI and the rule engine

**Language tasks:** interpreting the athlete's request, recognizing missing information, summarizing coach notes, explaining the approved adjustment. **Computational tasks:** set totals, load changes, dates, unit conversion, version management and checking professional limits.

In the first version, plan proposals are based on coach-approved operations: moving, permitted swap, adjustment within a given range. The model can request these in a structured way; the application decides whether they can be executed. The content of a free-text log is data, not an instruction that modifies the application's permissions.

Structured model output helps with format validation, but the official documentation also indicates that it can still contain content errors. Therefore, after schema validation, business and professional checks are needed. [Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs)

Proposed internal operations: `get_athlete_state`, `record_training_event`, `propose_plan_change`, `validate_plan_change`, `approve_plan_change`, `export_training_history`. The names are design examples. Approval should be an operation with separate permissions; a proposal prepared by the AI must not be able to approve itself.

### 9.4. Memory, search and model replacement

Training sets and plans should come from structured database queries. For longer coach notes, document search may be justified later, but initially a short summary assigned to the athlete and the most recent relevant events may be sufficient. Sending the entire life history with every request is costly and harder to verify.

Every summary should reference the timestamp of the underlying data. New, approved information can override an old preference, but the system must know why it changed. Health restrictions must not lose valid conditions during compression.

I would put model calls behind a small service layer of your own, so that replacing the provider or model does not affect the whole product. This does not require multi-provider operation on day one. The selection must be made based on your own Hungarian-language case set, latency, billed usage and error rate.

### 9.5. Permissions and operations

Every read and write should verify the athlete–coach relationship on the server side. Supabase's row-level security can help, but administrative/service-role access can bypass these rules. Placing the key correctly is not enough on its own: the backend's permissions must also be tested. [Supabase RLS](https://supabase.com/docs/guides/database/postgres/row-level-security)

Required operational behaviors: processing a doubly submitted event once; rechecking an expired proposal; unambiguous handling of time zones and kg/lb; save status after a network error; working export; tested data restore; availability of the approved plan in case of a model failure.

Preserving the change log and deleting personal data must not be contradictory. On deletion, personal content and linkable identifiers must be handled according to the defined procedure; retaining technical events is only justified in an appropriate, non-personally-linkable or lawfully retained form.

## 10. AI cost and pricing

The example below assumes short-context standard text usage, without discounts. Assumption per athlete: 60 requests per month, on average 5,000 input and 1,000 billed output tokens per request; a total of 300,000 and 60,000 tokens. Billed reasoning tokens must also be counted in the output budget.

| Example model | Input/output USD / 1 million tokens | Example monthly cost | Five times the usage |
|---|---|---|---|
| GPT-6 Luna | 0.10 / 0.50 | 0.06 USD | 0.30 USD |
| GPT-6.1 Sol | 2 / 10 | 1.20 USD | 6 USD |

This is model usage only, not the full application cost and not a sports-science suitability test. Retries, longer context, tools, other processing modes and additional analyses can increase the bill. Before choosing a model, quality must be measured on your own case set. [API pricing](https://developers.openai.com/api/docs/pricing)

Simple log entry does not necessarily need a model call at all. The rule engine, a concise state summary and re-planning only on events can reduce cost. There should be per-user usage metering, limits and a predictable budget. "Unlimited AI" at launch is a poorly plannable commitment.

**Proposed price tests, not a final price list:**

| Offer | Test price | What should it include? |
|---|---|---|
| External coach four-week pilot | 9,900 HUF + applicable VAT, up to 10 athletes | Onboarding, limited working tool, regular feedback |
| Coach basic | 14,900 HUF + applicable VAT / month, up to 10 active athletes | Planning, log, proposals, athlete access included |
| Coach larger plan | 24,900 HUF + applicable VAT / month, up to 25 active athletes | The same workflow with a larger allowance; measure margin separately |
| Later standalone athlete product | Testing gross price points of 3,990 and 5,990 HUF/month | Adaptive plan and log; personal human coaching is a separate service |

A monthly fee suits continuous adaptation. I would introduce an annual plan after gaining retention experience, for example for the price of 10 months. A one-time fee can work for a template or program; for a continuous AI service, a lifetime offer would commit to unlimited future cost. The coach and their athlete should not pay twice for the same base feature.

Measure the price against the time saving too. For example, four hours saved per month at an assumed time value of 6,000 HUF/hour means 24,000 HUF of value. This is a calculation example, not a claim about coaches' actual hourly rates. If the tool only saves ten minutes, the value proposition is different.

**Conservative margin example:** 14,900 HUF monthly net fee; on average 10 active athletes per coach; 600 HUF variable technical cost budget per athlete; an estimated value of 3,000 HUF of support work per coach; 40,000 HUF monthly fixed technical cost. These are my own planning assumptions, not vendor offers.

| Paying coaches | Monthly net revenue | Remainder after the above items |
|---|---|---|
| 10 | 149,000 HUF | 19,000 HUF |
| 30 | 447,000 HUF | 137,000 HUF |
| 50 | 745,000 HUF | 255,000 HUF |

Development, customer acquisition, accounting, taxes, payment fees and other business costs have not yet been deducted from the remainder. This is not a profit forecast. In the example, at least seven coaches are needed to cover the listed items. The working time lost or gained with thirty clients can also be significant. Unit economics must be verified on the number of active athletes and the actual support time.

### 10.1. Which pricing unit suits the product?

| Model | What speaks for it? | What speaks against it? | Initial decision |
|---|---|---|---|
| Monthly fee with an athlete allowance | Predictable bill; the coach ties the value to the client base served | A coach using the full allowance may be more expensive than average | I would test this first |
| Fee per active athlete | Cost and revenue can grow together | Variable monthly bill; active status must be precisely defined | Suitable for a later overage fee |
| Unlimited athletes at a fixed price | Simple offer | Support and usage of large clients can eat up the margin | To be avoided in the pilot |
| AI credits or tokens | Can be aligned with direct model cost | Coaches do not think in tokens; it can inhibit useful usage | Good for internal cost measurement, weak as main pricing |
| Annual prepayment | Earlier cash inflow, less monthly payment friction | For an early product, a long commitment and refund questions | Only after proven usage |
| One-time license | Easy-to-understand one-time purchase | Hosting, AI and support are ongoing costs | Not recommended for this service |

The meaning of an active athlete must be fixed in the offer: for example, a profile that has a live program and logging access in the given billing period. Retention and reactivation of an archived profile are handled by a separate rule. Archiving should not involve data loss, but the plan limit should not be ambiguous either.

I would treat the 10- and 25-athlete plans as **price tests**. The trial should include a concrete service description and a payment option. Stronger evidence than the question "how much would you pay?" is whether the coach actually subscribes after seeing the workflow. The terms should be clear: pilot period, allowance, support, cancellation, data access after the trial.

### 10.2. Sensitivity analysis: when do the proposed prices work?

The calculation below, my own, shows what happens **when the full athlete allowance is used**. For both plans it uses a support work value of 3,000 HUF/month; this may be optimistic for the larger plan. The per-athlete amount is a technical cost budget, not merely token cost. The real figure will be measured by the pilot.

| Variable technical cost / athlete / month | Monthly contribution of the 14,900 HUF, 10-athlete plan | Monthly contribution of the 24,900 HUF, 25-athlete plan | Coaches needed for 40,000 HUF fixed cost, from that plan only |
|---|---|---|---|
| 200 HUF | 9,900 HUF | 16,900 HUF | 5 / 3 |
| 600 HUF | 5,900 HUF | 6,900 HUF | 7 / 6 |
| 1,200 HUF | −100 HUF | −8,100 HUF | Neither covers the fixed cost |

Formula: **monthly contribution = net plan price − active athletes × variable technical cost − value of support work**. In the table, "contribution" is the amount remaining before fixed costs. This is not yet an accounting result.

In the base scenario, the 25-athlete plan gives only 1,000 HUF more monthly contribution for 15 additional athletes. This indicates that the volume discount may be too large. Possible responses are a higher large-plan price, a smaller allowance or a per-athlete overage fee. However, raising the price is only worthwhile with proven value; the cost base on its own does not prove willingness to pay.

If, beyond the 40,000 HUF fixed cost, you also want to earn **a monthly founder work budget of 400,000 HUF**, a total contribution of 440,000 HUF would be needed. In the 600 HUF base scenario, this is 75 fully used small plans or 64 large plans. In the 200 HUF scenario, 45 and 27 respectively. These are examples calculated purely with one type of plan, not sales forecasts; taxes, customer acquisition and several other costs are still missing from them. The 400,000 HUF is not a net salary. The founder budget is meant for product and business work done in addition to the separately accounted support work, so that the same working hour is not counted twice.

**Measuring cash and working time separately:** if you support the clients yourself, the 3,000 HUF may be an estimated time value, not an amount actually paid out. The work still ties up resources. The financial log should therefore show both the costs leaving the bank account and the minutes spent.

### 10.3. Effect of customer acquisition and retention

My own numerical example: if acquiring one paying coach costs 30,000 HUF in the combined value of advertising, demos and sales work, then with a monthly contribution of 5,900 HUF roughly **5.1 months** are needed to pay back the acquisition, even before allocating fixed costs. Early cancellation can easily derail this. A client acquired through a personal connection is not automatically free either: the time for the demo and onboarding must also be measured.

Initially, do not calculate long-term customer value from little data. Track cohorts by starting month separately: how many paid for the first time, how many are active in the second and third month, why they cancel, and how much support they need. Subscription retention and actual usage are separate metrics; annual prepayment, for example, does not on its own prove weekly usage.

**Pricing decision at the end of the pilot:** if users save time and pay, but support is heavy, first improve onboarding and the product's clarity. If they save little time, a lower price will not necessarily save the offer. If only large clients are unprofitable, adjust the plan allowance and the large-plan price; do not judge the whole product as unviable.

## 11. Data and the boundary of the injury feature

Information about injuries and health status can be health data requiring special protection. The design must clarify the controller/processor roles of the coach and the software provider, the legal basis and the separate condition for processing health data; explicit consent is one possible condition, not a solution that replaces every obligation. Data minimization, permission management, a retention policy, export and a deletion process are required. [EU data protection information](https://europa.eu/youreurope/business/governance-and-sustainability/digital-and-data-compliance/data-protection-gdpr/index_en.htm), [data protection principles](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/principles-gdpr_en)

Only the data needed for the task should go to the model, preferably without name and contact details. Pseudonymization is not full anonymization. By default, the OpenAI API does not use submitted data for model training, but there can still be data retention; the default period for abuse-monitoring logs is up to 30 days, with exceptions. The data handling of a consumer AI client must not automatically be assumed to be the same as that of the API. [OpenAI data handling](https://developers.openai.com/api/docs/guides/your-data)

The goal of the first version should be training planning support. Injury diagnosis, rehabilitation prescription or a promise of recovery can substantially change the product's professional and regulatory position. In EU software classification, the actual intended purpose and the claims also matter; a disclaimer sentence does not solve this. [MDCG 2019-11 rev.1](https://health.ec.europa.eu/document/download/b45335c5-1679-4c71-a91c-fc7a4d37f12b_en?filename=md_mdcg_2019_11_guidance_qualification_classification_software_en.pdf)

### 11.1. What does this mean concretely in the pilot?

The list below is my own product design work package, not a full legal compliance audit:

1. Create a data inventory: which field is needed and why, who sees it, how long you keep it, and which provider it goes to. Health data can also end up in a free-text note.
2. The coach should only have access to the data of athletes assigned to them. Ending the assignment should have a tested process; the athlete's own access must be handled separately.
3. Test export and deletion for logs, AI summaries and the backup schedule too. Clarify the conditions of deletion and any retention obligations in advance.
4. For system development tests, first use synthetic or properly prepared data. Before taking over real histories, settle the conditions of their use.
5. Have an actually tested data backup, restore and incident-handling contact. The existence of a backup does not prove it can be restored.
6. Handle data processing for training support and later, cross-user model development separately. One should not automatically follow from the other.

### 11.2. AI transparency and product promise

According to the European Commission's guidance, the transparency rules of Article 50 of the AI Act apply from 2 August 2026. Among other things, they concern informing people about direct AI interaction; the exact obligation depends on the role, use and exceptions. This does not mean that every training app is automatically a high-risk system. [Commission guidelines](https://digital-strategy.ec.europa.eu/en/policies/guidelines-ai-transparency-obligations)

My own product proposal: the interface should have separate states for an "AI proposal", a "coach-modified" and a "coach-approved" plan. The approving person and time should come from the actual operation. An AI communicating with the athlete should not give the impression that the message was written personally by the coach. A draft without approval should not appear as a final training instruction.

For injury situations, the first version's defensible promise is: it records the report, restricts automatic adjustment, and routes the case to the coach. Implementing this is not the same development task as producing a diagnosis or a rehabilitation program. Before the external pilot, it is worth requesting a targeted data protection and classification review based on the actual features and product claims.

## 12. Implementation schedule and budget

### 12.1. Detailed work breakdown

The estimated effort for a narrow pilot usable with external coaches is **240–400 focused hours**, if you already use the basic Python development tools. I am revising the earlier 160–280-hour estimate based on the detailed work breakdown: onboarding, evaluation and operations tasks involve more work. The lower range may be enough rather for a heavily narrowed internal prototype. This is my own planning estimate, not an external developer quote.

| Work package | Tangible outcome | Estimated hours |
|---|---|---|
| Problem discovery | Interview notes, measured baseline process, pilot offer | 16–24 |
| Professional rules | Decision conditions, prohibitions, reference cases | 24–40 |
| Data model and access | Versioned plans, log, coach–athlete permissions | 24–40 |
| Backend and AI pipeline | Event processing, rule checking, proposal and approval | 32–56 |
| Simple mobile-friendly interface | Logging, coach overview, display of adjustments | 40–64 |
| Evaluation and bug fixing | Professional test set, verification of permissions and error handling | 24–40 |
| Deployment | Logging, cost limit, backup, restore, basic processes | 16–24 |
| Pilot support | Onboarding, measurements, interviews, minor fixes | 24–32 |
| **Subtotal** |  | **200–320** |
| **With 20% contingency** |  | **240–384; rounded for planning to 240–400** |

Assumptions: one developer, one simple import format, a few known training templates, a mobile-friendly web interface and manual pilot sales. The estimate does not include native mobile apps, video processing, full payment/billing integration, automatic import from every competitor or a longer professional effectiveness study. Time for external expert review and contract work must be agreed separately.

### 12.2. Weekly capacity and scheduling

The detailed tasks, hour budgets and acceptance criteria of the first phase are in a separate document, adapted to a side-project pace (10 + 2 hours per week) and to the move: [First phase schedule](elso_szakasz_utemterv.md).

| Available time | Time span to the end of the pilot based on the estimated effort |
|---|---|
| 8 hours per week | 30–50 weeks |
| 15 hours per week | 16–27 weeks |
| 25 hours per week | 10–16 weeks |

These are estimates divided by capacity. Tester availability, learning technology and external review can extend calendar time. The four-week pilot really has to run for four weeks, even if development is faster. The **16-week sample schedule below plans with about 25 hours per week**; with less capacity, the same gates are met over a longer period.

1. **Weeks 1–2:** 6 coach and 6 athlete interviews; concrete recent adjustments; time measurement; first willingness-to-pay test. Most of them should not be exclusively your own clients.
2. **Weeks 3–4:** supervised manual trial; shared data schema; a few of your own or permission-granted plans; a test set of 30–50 typical and edge cases. First prove that the decision logic is useful.
3. **Weeks 5–10:** log, simple import/export, coach overview, missed session/rescheduling/day change/exercise swap, adjustment view and approval. Initially a few well-known programming templates. The fourth feature can be dropped if the first three are not yet reliable.
4. **Weeks 11–12:** small-circle internal use; professional and permission checks; time and cost measurement; testing data backup and restore. If a critical check fails, the external launch should be postponed.
5. **Weeks 13–16:** four-week paid external pilot, weekly feedback and a go/no-go decision. The six-week retention observation, if needed, runs until week 18.

### 12.3. What to spend on first?

**Cost scenarios with your own work:** for interview/manual validation, an extra budget of 0–30,000 HUF may be enough with existing tools. For the technical operation of a small hosted pilot, I would initially plan a budget of 15,000–50,000 HUF/month, depending on usage. A three-month technical reserve is thus 45,000–150,000 HUF. These are estimates, not full business start-up costs; legal, accounting, security or external development work requires separate quotes. The economic value of your own working time is expected to be substantially larger than the server cost.

Each phase should have its own spending decision:

| Phase | After what evidence should you move on? | What is it justified to spend on? |
|---|---|---|
| Interviews and manual trial | Several coaches show the same concrete problem | Interviews, documenting the workflow, a simple demo |
| Internal prototype | The process solved with manual support is measurably useful | Minimal database, interface, AI experiments |
| External paid pilot | There is committed participation, clarified data handling and working review | Stable hosting, backup, targeted expert review |
| Expansion | Usage, paid continuation and acceptable cost per client | Better onboarding, reliability, requested integrations |

A small technical cost does not mean the project is cheap relative to your own time. For example, 300 hours at an assumed alternative work value of 5,000 HUF/hour is an economic outlay of 1.5 million HUF. This is not a bill to pay or a claim about your actual hourly rate, but a comparison useful for the decision.

## 13. Validation questions and decision gates

In an interview, do not start with "would you use an AI app?". Ask for a concrete story: when the plan last fell apart, what they changed, in how many minutes, based on what data, what they would not hand over to a system. Ask them to show their current workflow and identify a single recurring, costly problem.

Recommended pilot goals, as your own decision thresholds:

- At least three coaches independent of you actually pay for the trial. Your own clients' satisfaction does not replace this.
- Including all review and correction time, the selected adjustment process is at least 30% shorter, in the median of several occasions.
- At least 80% of the proposals can be used without substantial professional rewriting. This is an operational goal, not a clinical quality indicator.
- After four to six weeks, the majority of the involved coaches use it on a weekly basis, and at least three commit to a paid continuation.
- At least 70% of the athletes' actual sessions are logged, as far as this can be verified in the pilot. With low data quality, improve logging first.
- Every pre-defined critical test case passes; there is no access to another athlete's data and no unreviewed, prohibited adjustment. This is necessary, but does not prove that every future error is ruled out.

If coaches value the summaries but reject the plan adjustment, narrow down to analysis. If data entry lapses, simplify the interface. If only your own clients use it, the tool can remain a valuable internal coaching aid, but a separate software business is not yet proven. If reviewing the proposals is more work than manual planning, do not scale automation.

Effectiveness claims about strength gains and injury risk require longer follow-up and an appropriate study; the small pilot should primarily measure usability, process quality and willingness to pay.

### 13.1. Interview plan: examine behavior, not polite interest

Proposed coach interview, 30–40 minutes:

1. How many athletes do they work with, with what tools, and how often do they rewrite programs?
2. Show the most recent concrete case when they made an adjustment because of a missed session, a changing training day or an exercise swap. Showing personal data is not necessary.
3. What information did they have to look up, and what was the hardest part of the decision?
4. How long do the adjustment, the review and informing the athlete take together?
5. What error would they not accept even if the system were faster?
6. Which current tool are they attached to, and what would make a new interface acceptable?
7. After a concrete demo, would they commit to a paid, time-limited pilot under the given terms?

In the athlete interview, logging should be central: when do they enter the data, what do they leave out, what happens with a weak internet connection, and how do they report a change to the plan? The coach's purchase intent is not enough if the athlete cannot use the tool regularly.

The sample should include coaches with different client counts, people using spreadsheets and people paying for an existing coaching app. The six coaches and six athletes are an initial exploratory sample; this is not representative research. Also record refusals and the cases where the problem is rare or insignificant. This reduces the risk of collecting only stories that support the idea.

### 13.2. What should the professional test set look like?

The initial proposal is **50 versioned cases**, with several kinds of athletes and coaching methods. This is the starting point of a minimum operational check, not proof of the full reliability of the system. One possible breakdown:

| Case family | Count | What needs to be checked? |
|---|---|---|
| Rescheduling and missed sessions | 10 | Only future work changes, no overcrowding or duplication |
| Frequency and time budget | 8 | The available days and minutes are actually respected |
| Partial completion | 6 | Completed sets are not automatically repeated |
| Exercise swap | 8 | Happens based on reason, equipment and coach permission |
| Missing or contradictory data | 6 | The system clarifies or refrains from adjusting |
| Pain and restriction | 6 | The prohibited automatic decision remains blocked |
| Version conflict and access | 6 | No outdated approval or access to another athlete's data |
| **Total** | **50** |  |

A case contains the starting plan, the actual log, the change request, the permitted and prohibited outputs, and the evaluation rationale. There can be several professionally appropriate answers; following a single sample text word for word is a weak quality measure.

From the set, for example, 35 cases can serve for development and 15 for held-out validation. Minor rewordings of the same case should not end up in both sets. In addition, test the critical permission and prohibition rules separately with tests run on every release. New cases arising from errors should extend the regression set; over time, new, previously unseen validation cases are also needed.

Because of the variable output of generative models, evaluate important cases with several runs, and do not let the most serious error disappear in an average. OpenAI's evaluation guide recommends task-specific, continuous evaluation and grading aligned with human review. The specific case breakdown above is my own proposal. [Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)

Initially, your own simple Python-based test runner and versioned case files are sufficient. The professional decision should be graded by a human; automatic checks examine numbers, limits and permissions. A second coach should review at least the held-out cases and the disputed decisions, so that you do not measure only fit with your own preferences.

### 13.3. How to measure time saving and acceptability?

Define the start and end points in advance. The measurement should run from opening the request to the reviewed, releasable plan; waiting for the AI, correction and writing explanations all count. Fast generation on its own is not an acceleration of the whole workflow.

For the initial comparison, every coach should do a few cases of similar difficulty with their usual tool and with the assistant. Alternate the order; when repeating the same case, handle the learning effect separately. This is a small usability study, not a rigorous effectiveness experiment. Show times per coach and per case family, not just the pooled average.

Example: 7 minutes of total assisted work instead of 10 minutes of manual work is a 30% time saving. If generation takes one minute but review and correction take ten, the process has become slower overall.

Proposed grading categories:

- **Acceptable:** can be released without professional changes; minor wording corrections are allowed.
- **Needs correction:** a substantive change to load, order, exercise or scheduling is needed.
- **Rejected:** the proposal does not resolve the request or requires re-planning.
- **Critical error:** violates a permission, an explicit prohibition or another predefined safety condition.

The 80% acceptability target is the proportion of the first category out of all requests classified in advance as within the supported scope. Do not leave incorrect or missing proposals out of the denominator. Track situations that require clarification and those excluded from the outset separately. In case of a critical error, meeting the percentage target is not enough for launch.

### 13.4. Pilot measurement sheet and decision

| Metric | Operational definition | Why is it needed? |
|---|---|---|
| Activated coach | Has loaded at least one program, linked an athlete and carried through one adjustment | Registration is weak evidence |
| Weekly active coach | Did meaningful review or adjustment work in the given week | A page opening in the background should not count as usage |
| Logging rate | Recorded actual sessions / sessions actually completed according to reconciliation | The planned session count is a different denominator and distorts on skipped sessions |
| Total adjustment time | Work and waiting from request to releasable plan | The review burden also counts |
| Acceptance rate | Proposals without substantive professional correction / supported requests | Measures professional usability |
| Cost | AI, hosting and support minutes, per coach | Reveals costly clients and processes |
| Paid continuation | Actual renewal or a concrete paid next period | Separates intent from purchase |

Re-planning events may also be rare. If only a few occur in the four-week pilot, do not claim a reliable acceptance percentage. Extend the observation or supplement it with supervised, pre-prepared cases; keep simulated and live usage data separate.

**Continue:** several external coaches pay, save time, return, and the cost is manageable. **Narrow down:** it is useful only in certain cases; focus on those. **Turn into an internal tool:** valuable to you, external demand not proven. **Stop or new target group:** no recurring problem, no willingness to pay, or review is persistently more work than the solution.

## 14. Concrete first work package

The next committable outcome is a single complete workflow: existing four-day plan → missed session and new availability → reviewable proposal → coach approval → fresh plan → actual log. For this, 2–3 coach examples, pilot data for 5–10 athletes and well-defined rules are more sufficient than a large general feature list.

From the first version I would leave out the social feed, meal planning, wearables, video technique analysis, a custom model, a coach marketplace and fully autonomous injury handling. None of these is needed to test whether people pay for the selected plan adjustment process.

Given your three years of coaching experience and the available technical history, the most justifiable next step is a human-supervised pilot built on your own professional logic. The business decision is best made based on the first external paying coaches, the time saved and the cost measured from usage.

## 15. Decision and risk register

The following are planning risks; there is no measured data yet on their likelihood. The goal is to define in advance which result would change the plan.

| Assumption or decision | Main risk | What to watch? | When to change course? |
|---|---|---|---|
| The coach is the best first buyer | Hard to reach, attached to their current tool | Interviews, demo-to-pilot, paid continuation | If there is no paying prospect even after several relevant interviews, re-examine the problem and the outreach |
| Plan adjustment is a frequent problem | The feature is needed too rarely | Number and duration of real adjustments | If rare, a summary or administration may be a better entry point |
| Plan adjustment takes a lot of time (**critical, unmeasured**) | No independent data; only vendor claims | Adjustment time measured in minutes per coach | If the current manual adjustment takes a few minutes, time saving cannot be the main argument |
| Differentiable from existing solutions | A close competitor (e.g. Kaizer) also handles powerlifting cases well | Competitor test with the same cases (3.3–3.4.) | If there is no meaningful difference, narrow down or switch to a summary-type product |
| The athlete logs | Too much data entry burden | Logging of actual sessions, missing fields | With low logging, reduce fields, steps and waiting |
| Coach review is fast | Every proposal has to be rethought | Total review and correction time | If there is no time saving, narrow down to easily verifiable operations |
| The AI interprets reliably | Misunderstanding or invented reasoning | Held-out case set, critical errors | Route problematic cases to a structured form or to a human |
| The plan price covers the service | Many athletes and support eat up the margin | Cost distribution, heavy users | Change the allowance and price based on usage measured in the pilot |
| One developer can operate it sustainably | Fixes and support crowd out development | Weekly time breakdown and recurrence of errors | Simplify and stabilize first, add features only afterwards |
| The professional method is transferable | Other coaches work by different principles | Reasons for rejections, variation between coaches | Separate mandatory limits from configurable preferences |
| The provider integration is lasting | Model, price or access changes | Release changes and your own test results | Replace the model only after re-evaluation; logging should work without AI as well |

### 15.1. Which decisions should be easily reversible?

The first model, the plan price, the pilot size and the scope of supported cases can be changed. Do not build these too rigidly into the system. The data structure, plan versions, permissions and correct handling of the actual training history are a lasting foundation; initial shortcuts here can become expensive later.

My own priority: first reliable data recording and reviewable proposals, then convenience automation. It also follows that the athlete's data should not depend on a given model's conversation memory.

### 15.2. What could be a lasting competitive advantage?

Access to the AI model is available to other developers as well. A more lasting advantage can be a good logging experience, decision logic understood and accepted by coaches, a case set extended from real errors, simple onboarding and professional trust. These are built during use and require dedicated work.

A 2025 pilot study also supports this. According to the public abstract, a quarter of recreational athletes training with a structured plan used an AI-generated plan. Experienced coaches often could not distinguish AI-written from human-written plans. The study is small-sample and preliminary; I could not access the full text. My own conclusion: generating an acceptable training plan is already a low barrier to entry, so the advantage may lie in the workflow, coach control and data quality, not in plan generation. [Wachholz et al., 2025](https://pubmed.ncbi.nlm.nih.gov/40082991/)

The amount of data collected is not an advantage on its own. With inconsistent RPE, missing sets and undocumented exercise swaps, more data can also mean more noise. Rather than greater control over users or making export harder, better results and a lighter workload should retain the client.

## 16. Launch plan and open research questions

### 16.1. Tangible outcome of the first two weeks

The sequence below assumes about 15–25 hours of available time per week. If you have less time, keep the sequence and stretch the calendar.

| Step | Material produced | Decision value |
|---|---|---|
| Day 1: target situation | One-page description: for whom, at what change, what result the app provides | It does not sprawl into a general fitness platform |
| Days 2–3: own cases | Write-ups of 10 real adjustments, without identifiable personal data | It becomes clear which decisions recur |
| Days 3–7: external interviews | At least 4 coach and 4 athlete interviews; further appointments | It can be verified whether the problem exists for others too |
| Days 5–8: process measurement | A few supervised cases solved manually, with time measurement | There will be a baseline for comparison |
| Days 8–10: demo | One traceable plan change example, even with manual background work | The user reacts to the concrete value |
| Days 10–12: technical trial | The full path of one athlete, one plan and one set | The actual technological difficulty can be assessed |
| Days 12–14: offer and decision | Fixed pilot terms, committed participation, continue or narrow down | Long development without evidence can be avoided |

A finished public application is not yet needed at the end of the two weeks. The important outcome is a verified problem, a tested workflow and the justification for the next investment. If there is no interest, document whether it is because of the problem, the solution, the price or the outreach.

### 16.2. What research is still missing for a more confident decision?

| Open question | Why does the present research not answer it? | Next evidence |
|---|---|---|
| Would Hungarian coaches pay for this? | A foreign list price is not Hungarian demand | A concrete paid pilot offer and purchase |
| How much time does a plan adjustment take today? | Only vendor estimates of general administration can be found | Cases measured in minutes in interviews and the manual trial |
| How many reachable Hungarian powerlifting coaches are there? | I found no public federation membership or coach count data | Your own list as per Chapter 4.2 |
| Is the selected process better than the competitors'? | Usability cannot be measured from public feature descriptions | The hands-on test with the same cases in Chapter 3.3 |
| Is re-planning frequent enough? | There is no real usage event count | Four to six weeks of observation with several coaches |
| How much development learning do you need? | The shared project history is not a full competency assessment | The result of the two-day full-process trial |
| Which model is good enough? | The API price list only shows cost | Quality and total cost measured on the same Hungarian case set |
| Which users are retained? | Your own retention cannot be derived from a large aggregated subscription report | Several months of your own data by starting cohort |
| Does it improve athletic performance? | The cited training studies did not examine this application | Longer follow-up, an appropriate comparison and study design |

### 16.3. Conditional decision for your situation

**If you have 15–25 hours per week and can reach a few external coaches:** building a narrow coach assistant pilot is justifiable. Use your three years of professional experience in decision cases, rules and personal onboarding.

**If you have at most 5–8 hours per week:** the goal should first be your own coaching tool, manual import and one or two well-defined adjustment situations. The full external service could drag on for a long time; the first useful result is best obtained from a smaller work package.

**If you have no access to external testers:** validate the outreach first. The lack of a channel to the market is an uncertainty that further programming does not solve.

**If you have a strong direct athlete community, but coaches are not interested:** the standalone athlete target group can be reassessed, for narrow professional use and with separate quality assurance. In that case, the economics of supervision, user support and direct customer acquisition must be re-planned.

Based on current evidence, the defensible first goal is: **an adjustment assistant used and paid for by a few external coaches that measurably saves time**. A standalone AI coach can be a later product direction of this, requiring separate evidence.

## 17. Sources and source criticism

The following are the main sources cited in the document, verified on 16 October 2026. The grouping shows how they were used. Direct source links can also be found next to the relevant claims. Prices and platform terms must be re-verified at the time of an actual development or purchasing decision.

### 17.1. Competitors – official offers

| Source | What did I use it for? | Limitation |
|---|---|---|
| [JuggernautAI price list](https://www.juggernautai.app/pricing) | Powerlifting consumer offer and list price | Vendor claim; campaign price may differ |
| [Sheiko Gold](https://sheikogold.com/) and [US App Store](https://apps.apple.com/us/app/sheiko-gold-powerlifting-ai/id1475890027) | Adaptive features and monthly price | Conflicting data for the annual price |
| [Fitbod FAQ](https://fitbod.me/faqs/) | Personalization and web pricing | May differ by sales channel |
| [Boostcamp Pro](https://www.boostcamp.app/pro) | Free/paid alternative | Not a product quality test |
| [TrainHeroic Coach](https://www.trainheroic.com/coach/) | Athlete allowances and monthly fees | Feature and plan differences matter |
| [MyStrengthBook](https://mystrengthbook.com/pricing-coaching) | Coaching business model | PULL and PUSH are different offers |
| [Everfit pricing](https://everfit.io/pricing/) and [AI Workout Builder](https://help.everfit.io/en/articles/9373485-introducing-ai-workout-builder) | Coaching platform and AI feature | The AI feature is not a proven autonomous coach |
| [RTS Training Lab](https://rtslab.reactivetrainingsystems.com/) | Powerlifting coaching comparison | Not independent evidence of effectiveness |
| [Kaizer comparison article](https://kaizer.app/en/blogs/best-personal-trainer-software-2026) | Closest competitor found; claims about other platforms' AI features | Its own marketing material; its claims about competitors need verification |
| [Trainerfu](https://www.trainerfu.com/blog/everfit_alternatives/), [Everfit blog](https://blog.everfit.io/everfit-vs-trainerize-vs-truecoach), [Coaching Portal](https://coachingportal.io/blog/ai-fitness-coaching-trends) | AI features of coaching platforms, approval practice | Material written by a third party or a competitor |

### 17.2. Market and sports-science background

| Source | Related question | Important limitation |
|---|---|---|
| [RevenueCat: State of Subscription Apps](https://www.revenuecat.com/state-of-subscription-apps) | Retention of AI apps and the subscription environment | The result of your own product does not follow from the studied platform sample |
| [Helms et al., 2018](https://pubmed.ncbi.nlm.nih.gov/29628895/) | RPE-based and percentage-based loading | Small sample, short time span |
| [Saric et al., 2019](https://pubmed.ncbi.nlm.nih.gov/30363041/) | Frequency with equal volume | Not a general rule for every frequency change |
| [Remmert et al., 2023 – RIR accuracy](https://pubmed.ncbi.nlm.nih.gov/37036795/) | RIR as input data | The studied exercises and conditions limit generalization |
| [Remmert et al., 2023 – six-week study](https://journals.sagepub.com/doi/10.1177/00315125231189098) | Development of estimation accuracy | Very small sample; public abstract |
| [Refalo et al., 2023](https://link.springer.com/article/10.1186/s40798-023-00554-y) | Proximity to failure and acute fatigue | Acute study, not long-term injury research |
| [Martikainen et al., 2025](https://link.springer.com/article/10.1007/s42978-025-00338-8) | Variable and constant RIR | Not an effectiveness test of an AI algorithm |
| [Wachholz et al., 2025](https://pubmed.ncbi.nlm.nih.gov/40082991/) | Acceptance of AI-generated training plans and how coaches judge them | Small-sample pilot; I could not access the full text |

### 17.3. Technology documentation

| Source | Role in the decision |
|---|---|
| [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture) | Role of the connection protocol |
| [Sign in with ChatGPT](https://developers.openai.com/siwc/token-sharing-open-source) and [limitations](https://developers.openai.com/siwc/token-sharing-open-source/preview-limitations) | Conditions of subscription-linked integration |
| [OpenAI API pricing](https://developers.openai.com/api/docs/pricing) | Example model usage cost |
| [OpenAI data handling](https://developers.openai.com/api/docs/guides/your-data) | Distinguishing model training from retention |
| [Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs) | Possibilities and limits of structured output |
| [Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices) | Task-specific testing |
| [FastAPI](https://fastapi.tiangolo.com/features/) and [Django](https://docs.djangoproject.com/en/5.2/intro/overview/) | Comparison of Python frameworks |
| [Supabase pricing](https://supabase.com/pricing) and [RLS](https://supabase.com/docs/guides/database/postgres/row-level-security) | Managed database and permissions |

A documented technical capability does not prove that the given solution is the fastest to build within your time budget. This must be decided based on the small technical trial and your own case set.

### 17.4. Data protection and intended purpose

- [EU GDPR information for businesses](https://europa.eu/youreurope/business/governance-and-sustainability/digital-and-data-compliance/data-protection-gdpr/index_en.htm) and [data protection principles](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/principles-gdpr_en): the foundations of data processing design.
- [MDCG 2019-11 rev.1](https://health.ec.europa.eu/document/download/b45335c5-1679-4c71-a91c-fc7a4d37f12b_en?filename=md_mdcg_2019_11_guidance_qualification_classification_software_en.pdf): the intended purpose of software and its medical device classification.
- [AI Act transparency guidelines](https://digital-strategy.ec.europa.eu/en/policies/guidelines-ai-transparency-obligations): the regulatory background for labeling AI interaction and origin.

These sources help identify the design questions. The concrete review of the given product must be carried out based on the final features, roles, data flows and marketing claims.
