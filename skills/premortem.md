# Premortem

Structured failure analysis: "Imagine this has already failed spectacularly -- why?" Routes to [[critic]] and [[strategist]] in parallel. The Critic identifies failure modes; the Strategist builds prevention plans.

Different from `/challenge` (adversarial questioning of assumptions). A premortem is a systematic, structured imagination of failure to surface risks before they materialize.

## When to Use

- Before launching a major initiative or project
- Before making a high-stakes decision
- When a plan feels "too clean" and you suspect hidden risks
- When you want to stress-test execution, not just strategy

## Arguments

- **subject** (required): The plan, project, or decision to analyze.
  - Examples:
    - `the new hiring plan for Q2`
    - `launching the self-serve product tier`
    - `switching from Slack to Teams`
    - `the partnership deal with Acme Corp`

## Instructions

1. **Load brain context.** Read all relevant brain files:
   - `brain/context/projects.md` -- current status and dependencies
   - `brain/context/stakeholders.md` -- people involved and their dynamics
   - `brain/context/decisions-log.md` -- related prior decisions
   - `brain/learnings/patterns.md` -- historical patterns of what has gone wrong before
   - `brain/learnings/strategies.md` -- what has and hasn't worked
   - `brain/preferences/analysis-style.md` -- how to present the analysis

2. **Set the frame.** Establish the premise:
   > "It is [6 months from now]. The [subject] has failed. Not a minor setback -- a significant, visible failure. Your job is to explain why."

3. **Generate failure modes.** The [[critic]] and [[strategist]] work in parallel:

   **Critic generates failure reasons** across these categories:
   - **Execution failures**: Team capacity, skill gaps, timeline issues, resource constraints
   - **Strategic failures**: Wrong market, wrong timing, wrong approach, misread customer needs
   - **People failures**: Key person leaves, stakeholder misalignment, cultural resistance, communication breakdown
   - **External failures**: Market shift, competitor move, regulatory change, economic downturn
   - **Technical failures**: Architecture won't scale, integration breaks, data quality issues
   - **Assumption failures**: Which core assumptions, if wrong, would cause collapse

   **Strategist evaluates each failure mode:**
   - Likelihood (high / medium / low)
   - Impact (catastrophic / significant / manageable)
   - Detectability (would we see this coming, or would it blindside us?)

4. **Rank and prioritize.** Create a risk matrix:
   - Priority = Likelihood x Impact x (1/Detectability)
   - Focus prevention plans on the top-ranked items

5. **Build prevention strategies.** For each high-priority failure mode:
   - What specific action would prevent or mitigate this?
   - Who owns the prevention?
   - What's the early warning signal to watch for?
   - What's the fallback if prevention fails?

6. **Structure the output:**

   ```
   PREMORTEM: [Subject]
   Date: [today's date]
   =====================

   THE SCENARIO
   It is [future date]. [Subject] has failed. Here's why.

   FAILURE MODES
   -------------

   | # | Failure Mode | Category | Likelihood | Impact | Detectability | Priority |
   |---|-------------|----------|------------|--------|---------------|----------|
   | 1 | [mode]      | [cat]    | High       | Catastrophic | Low      | CRITICAL |
   | 2 | ...         | ...      | ...        | ...    | ...           | ...      |

   DETAILED ANALYSIS
   -----------------

   [For each CRITICAL and HIGH priority failure mode:]

   ### [#]. [Failure Mode Name]
   **What happens:** Narrative description of how this failure unfolds.
   **Root cause:** The underlying driver.
   **Early warning signs:** What to watch for.
   **Prevention strategy:** Specific actions to take now.
   **Fallback plan:** If prevention fails, what's Plan B.
   **Owner:** Who should be responsible for this.

   PATTERN CHECK
   -------------
   - Connections to historical patterns from brain/learnings/
   - "We've seen this before when..."

   TOP 3 ACTIONS
   -------------
   The three most impactful things to do right now to reduce risk:
   1. Action -- addresses failure modes [#, #]
   2. Action -- addresses failure modes [#, #]
   3. Action -- addresses failure modes [#, #]

   CONFIDENCE LEVEL
   ----------------
   How confident we are in this analysis, and what would improve it.
   ```

7. **Save the report.** Write to `output/analyses/premortem-[subject-slug]-[date].md`. Create the directory if it does not exist.

8. **Offer follow-up options:**
   - "Want me to turn the prevention strategies into a project plan?" (triggers `/strategize`)
   - "Want me to challenge any of these assumptions further?" (triggers `/challenge`)
   - "Want me to research how others have handled [specific failure mode]?" (triggers `/research`)
