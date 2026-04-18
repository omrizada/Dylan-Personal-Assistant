# Weekly Review

End-of-week retrospective and next-week planning session. Routes to [[chief-of-staff]] for orchestration, then [[strategist]] for priority planning. See also [[Dashboard]].

## When to Use

- End of week to reflect on progress and plan ahead
- When you need to recalibrate priorities
- Before a planning meeting where you need a clear picture of the week
- When things feel chaotic and you need to reset

## Arguments

None. This skill reads brain context and synthesizes automatically.

## Instructions

1. **Load brain context.** Read all relevant brain files:
   - `brain/context/projects.md` -- current project status and milestones
   - `brain/context/decisions-log.md` -- decisions made this week
   - `brain/context/okrs.md` -- OKRs and key results (if exists)
   - `brain/learnings/session-notes.md` -- notes captured during the week
   - `brain/learnings/patterns.md` -- recurring patterns observed
   - `brain/context/followups.md` -- commitments and their status

2. **Compile the retrospective.** Review the past week across these dimensions:
   - **Completed**: What shipped, what got done, what moved forward
   - **Slipped**: What was planned but didn't happen, and why
   - **Decisions made**: Key decisions from the decisions-log with rationale
   - **Patterns observed**: Recurring themes from the week (blockers, energy drains, momentum builders)
   - **Commitments status**: Check followups.md for anything due or overdue

3. **Plan the next week.** The [[strategist]] builds the forward-looking section:
   - **Priority stack**: Top 3-5 items for next week, ordered by impact
   - **Key milestones**: What's due or approaching deadline
   - **Decisions needed**: Pending decisions that should be resolved next week
   - **Risks**: Anything that could derail the plan

4. **Structure the output** as a review document:

   ```
   WEEKLY REVIEW: [Week of Date]
   ==============================

   RETROSPECTIVE
   -------------

   Completed
   - Item with brief context
   - ...

   Slipped
   - Item -- reason it slipped
   - ...

   Decisions Made
   - Decision -- rationale (from decisions-log)
   - ...

   Patterns Observed
   - Pattern with implication
   - ...

   Commitments Status
   - Person: task -- status
   - ...

   NEXT WEEK PLAN
   --------------

   Priority Stack
   1. [Highest impact] -- why this is #1
   2. ...
   3. ...

   Key Milestones
   - Milestone -- deadline
   - ...

   Decisions Needed
   - Decision -- context and stakes
   - ...

   Risks
   - Risk -- mitigation
   - ...

   ENERGY CHECK
   ------------
   Brief note on what drained vs. energized this week,
   to inform how next week is structured.
   ```

5. **Save the report.** Write to `output/documents/{date}-weekly-review.md`. Create the directory if it does not exist.

6. **Offer follow-up options:**
   - "Want me to update project statuses based on this review?" (updates `brain/context/projects.md`)
   - "Want me to strategize on any of the slipped items?" (triggers `/strategize`)
   - "Want me to challenge next week's priority stack?" (triggers `/challenge`)
