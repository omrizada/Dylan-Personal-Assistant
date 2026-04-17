# Devil's Advocate Session

Stress-test a plan, idea, or assumption. Find blind spots, identify risks, and challenge thinking constructively. The goal is to make the idea stronger, not to tear it down.

## When to Use

- Before committing to a major decision
- When a plan feels too optimistic or too easy
- To find blind spots in your thinking
- Before presenting a strategy to stakeholders
- When you want someone to push back

## Arguments

- **input** (required): A plan, idea, assumption, or strategy to challenge. Can be a description, a file path to an existing document, or a reference to a previous analysis/strategy.
  - Examples:
    - `our assumption that data analysis should come before manual interventions`
    - `output/strategies/gtm-plan-2026-03-29.md`
    - `the idea that we should hire three more engineers before Q3`

## Instructions

1. **Load brain context.** Read relevant brain files:
   - `brain/context/` -- all files, for situational awareness
   - `brain/learnings/` -- past patterns, what has worked and failed before
   - `brain/preferences/priorities.md` -- what {{USER_FIRST_NAME}} values, to frame critiques against what matters

2. **If the argument is a file path**, read the document. If it references a previous analysis or strategy from `output/`, read that file.

3. **Launch the critic agent** (or perform the critic role if the agent is not yet defined).

4. **Apply structured critique.** Evaluate the input across these dimensions:

   a. **Assumptions** -- What is being taken for granted? Which assumptions are untested?
   b. **Evidence** -- What data supports this? What data is missing? Is the evidence being interpreted correctly?
   c. **Risks** -- What could go wrong? What are the downside scenarios? What is the blast radius of failure?
   d. **Blind Spots** -- What perspectives are missing? Who would disagree and why? What is the argument against this?
   e. **Dependencies** -- What needs to be true for this to work? Which dependencies are fragile?
   f. **Second-Order Effects** -- What are the unintended consequences? What does this make harder later?
   g. **Alternatives** -- What other approaches were not considered? Is there a simpler path?

5. **Rate each finding by severity:**
   - **CRITICAL** -- Could cause the plan to fail outright. Must be addressed.
   - **HIGH** -- Significant risk or gap. Should be addressed before proceeding.
   - **MEDIUM** -- Worth considering. Could become a problem if ignored.
   - **LOW** -- Minor concern. Note it but do not let it block progress.

6. **Structure the output:**

   ```
   CHALLENGE: [Plan/Idea Being Tested]
   Date: [today's date]
   =====================================

   OVERALL ASSESSMENT
   One paragraph summary -- how robust is this thinking?

   CRITICAL ISSUES
   - [Issue]: Explanation and why it matters
     Suggested mitigation: ...

   HIGH-PRIORITY CONCERNS
   - [Issue]: Explanation
     Suggested mitigation: ...

   MEDIUM-PRIORITY CONCERNS
   - [Issue]: Explanation
     Suggested mitigation: ...

   LOW-PRIORITY NOTES
   - [Item]: Brief note

   STRONGEST COUNTERARGUMENT
   The single best argument against this plan, stated as compellingly as possible.

   WHAT WOULD MAKE THIS STRONGER
   Specific improvements that would address the issues above.
   ```

7. **Be constructive.** Every criticism must come with a suggested mitigation or improvement. The purpose is to strengthen the idea, not to kill it.

8. **Do NOT save the output automatically.** Present it in the conversation. If {{USER_FIRST_NAME}} wants to keep it, save to `output/analyses/challenge-[topic-slug]-[date].md`.

9. **Offer follow-up options:**
   - "Want me to revise the original strategy based on these findings?"
   - "Want me to research any of these concerns further?" (triggers `/research`)
   - "Want me to do a deeper analysis on any specific issue?" (triggers `/analyze`)
