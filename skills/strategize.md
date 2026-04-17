# Strategic Thinking Session

Facilitate deep strategic thinking on a question or challenge. Produces a structured strategy document with options, tradeoffs, and a clear recommendation.

## When to Use

- Planning how to approach a new initiative
- Evaluating competing priorities or options
- Making a significant decision that needs structured thinking
- Building a roadmap or execution plan

## Arguments

- **question** (required): A strategic question, challenge, or decision to think through.
  - Examples:
    - `how should we prioritize manual interventions vs data analysis pillars?`
    - `what is the right GTM strategy for the new product?`
    - `should we build or buy the analytics capability?`

## Instructions

1. **Load brain context.** Read all relevant brain files:
   - `brain/context/` -- all files, especially `projects.md`, `role-and-goals.md`, `decisions-log.md`
   - `brain/preferences/analysis-style.md` -- how {{USER_FIRST_NAME}} likes strategic thinking presented
   - `brain/preferences/priorities.md` -- what matters most, decision-making weights
   - `brain/learnings/strategies.md` -- successful strategies and frameworks from the past
   - `brain/resources/insights/` -- relevant resource insights

2. **Launch the strategist agent** (or perform the strategist role if the agent is not yet defined). Apply relevant strategic frameworks based on the question:
   - **First Principles Thinking** -- break down to fundamentals
   - **OKR Alignment** -- does this serve the objectives?
   - **Scenario Planning** -- what happens under different assumptions?
   - **Porter's Five Forces** -- for competitive strategy questions
   - **Decision Matrix** -- for comparing options with weighted criteria
   - **Second-Order Thinking** -- what are the consequences of the consequences?
   - Choose frameworks that fit; do not force-fit

3. **Structure the output** as a strategy document:

   ```
   STRATEGY: [Question/Challenge]
   Date: [today's date]
   ==============================

   CONTEXT
   Brief summary of the situation, drawn from brain context.
   Why this question matters right now.

   STRATEGIC OPTIONS
   Option A: [Name]
   - Description
   - Pros
   - Cons
   - Resource requirements
   - Timeline
   - Risk level: High / Medium / Low

   Option B: [Name]
   - (same structure)

   Option C: [Name]
   - (same structure)

   TRADEOFF ANALYSIS
   What you gain and lose with each option.
   Which of {{USER_FIRST_NAME}}'s stated priorities each option serves best.

   FRAMEWORK APPLICATION
   [Name of framework]
   - Structured output

   RECOMMENDATION
   Clear recommendation with rationale.
   Why this option over the others.
   What would need to be true for this to succeed.

   EXECUTION OUTLINE
   If the recommendation is accepted:
   1. First step and timeline
   2. Second step and timeline
   3. Key milestones
   4. How to measure success

   DECISION NEEDED
   What {{USER_FIRST_NAME}} needs to decide, and what information would help.
   ```

4. **Save the document.** Write the strategy to `output/strategies/[topic-slug]-[date].md`. Create the directory if it does not exist.

5. **Offer follow-up options:**
   - "Want me to stress-test this strategy?" (triggers `/challenge`)
   - "Want me to research what others have done?" (triggers `/research`)
   - "Want me to draft an execution plan document?" (triggers `/draft`)
   - "Should I log this decision once you decide?" (updates `brain/context/decisions-log.md`)
