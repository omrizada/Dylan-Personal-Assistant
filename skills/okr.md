# OKR Tracker

Define, track, and review Objectives and Key Results. Manages `brain/context/okrs.md` as the source of truth. Invokes the [[strategist]] agent.

## When to Use

- Setting quarterly objectives and key results
- Logging progress on a key result
- Checking current OKR status at a glance
- End-of-quarter review and planning

## Subcommands

- `/okr set` -- Define objectives and key results for the quarter
- `/okr update "KR name" "progress"` -- Log progress on a specific key result
- `/okr check` -- Show current OKR status dashboard
- `/okr review` -- Quarterly synthesis and carry-forward planning

## Instructions

### For all subcommands

1. **Load brain context.** Read:
   - `brain/context/okrs.md` -- current OKR state
   - `brain/context/projects.md` -- project alignment
   - `brain/context/role-and-goals.md` -- overarching objectives
   - `brain/preferences/priorities.md` -- decision-making weights

---

### `/okr set`

2. **Facilitate OKR definition.** Guide {{USER_FIRST_NAME}} through setting objectives and key results:
   - Ask for 2-4 objectives for the quarter
   - For each objective, define 2-4 measurable key results
   - Each key result must have: description, target metric, and measurement method
   - Validate: Are these ambitious but achievable? Are key results measurable?

3. **Write to brain file.** Save the defined OKRs to `brain/context/okrs.md` in this format:

   ```markdown
   ## Current Quarter: [Q# YYYY]

   ### Objective 1: [Objective description]

   | Key Result | Target | Current | Status | Last Updated |
   |-----------|--------|---------|--------|-------------|
   | KR 1.1: [description] | [target] | [baseline] | Not Started | [date] |
   | KR 1.2: [description] | [target] | [baseline] | Not Started | [date] |

   ### Objective 2: [Objective description]
   ...
   ```

4. **Cross-reference with projects.** Map each key result to relevant active projects from `brain/context/projects.md` and note alignment.

5. **Update brain index.** Update `brain/BRAIN_INDEX.md` with the new last-updated date.

---

### `/okr update "KR name" "progress"`

2. **Find the key result.** Match the provided KR name (fuzzy match is acceptable) in `brain/context/okrs.md`.

3. **Update the entry.** Set the new current value, update the status, and set the last-updated date:
   - **Status logic:**
     - On track: Current >= expected pace toward target
     - At risk: Current is behind expected pace but recoverable
     - Off track: Current is significantly behind with low chance of recovery
     - Complete: Target has been met or exceeded

4. **Write the updated file.** Save changes to `brain/context/okrs.md`.

5. **Update brain index.** Update `brain/BRAIN_INDEX.md` with the new last-updated date.

6. **Confirm the update.** Show the updated key result row and its status.

---

### `/okr check`

2. **Generate a status dashboard.** Read `brain/context/okrs.md` and present:

   ```
   OKR STATUS — [Quarter]
   ======================

   OVERALL: [X of Y key results on track]

   ON TRACK
   - KR: [description] — [current] / [target] ([%])

   AT RISK
   - KR: [description] — [current] / [target] ([%])
     Risk: [why it's at risk]

   OFF TRACK
   - KR: [description] — [current] / [target] ([%])
     Issue: [what's blocking progress]

   COMPLETE
   - KR: [description] — [current] / [target]

   DAYS REMAINING IN QUARTER: [count]
   ```

3. **Flag items needing attention.** For at-risk and off-track items, suggest specific actions or decisions.

---

### `/okr review`

2. **Perform a quarterly synthesis.** Analyze the full quarter's OKR performance:

   ```
   OKR REVIEW — [Quarter]
   ======================

   SCORECARD
   | Objective | Key Results Hit | Score |
   |-----------|----------------|-------|

   WHAT WORKED
   - Successes with contributing factors

   WHAT DIDN'T WORK
   - Misses with root cause analysis

   KEY LEARNINGS
   - Insights about goal-setting, execution, or measurement

   CARRY-FORWARD ITEMS
   - Incomplete KRs worth continuing
   - New objectives suggested by this quarter's learnings

   RECOMMENDATIONS FOR NEXT QUARTER
   - Adjustments to goal-setting approach
   - Areas deserving more/less focus
   ```

3. **Archive the quarter.** Move the completed quarter's OKRs to the "Previous Quarters" section in `brain/context/okrs.md`.

4. **Offer to set next quarter's OKRs.** If the review is complete, suggest running `/okr set` for the next quarter.

5. **Update brain files.** Write learnings to `brain/learnings/strategies.md` and update `brain/BRAIN_INDEX.md`.

See also: [[projects]]
