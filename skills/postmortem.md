# Postmortem

Blameless after-action review that extracts root causes and prevention actions from incidents, projects, or events. Routes to [[analyst]] for timeline reconstruction and root cause analysis, then [[critic]] to challenge conclusions. Auto-updates [[strategies]] and decisions-log.

## When to Use

- After something went wrong and you want to learn from it
- After a project completes (successful or not) to capture learnings
- After a missed deadline, failed launch, lost deal, or any significant event
- When you want to turn an experience into reusable knowledge

## Arguments

- **event** (required): The incident, project, or event to review
  - Examples:
    - `"Q1 product launch delay"`
    - `"Lost the Acme partnership deal"`
    - `"Server outage on March 15"`
    - `"Team restructuring rollout"`

## Instructions

1. **Gather context.** Read brain files for relevant background:
   - `brain/context/projects.md` -- project status and history
   - `brain/context/decisions-log.md` -- decisions that led to this point
   - `brain/context/stakeholders.md` -- people involved
   - `brain/learnings/strategies.md` -- any prior strategies that were in play
   - `brain/learnings/session-notes.md` -- any prior discussions about this topic

2. **Ask for the facts.** If the brain does not have enough context, ask {{USER_FIRST_NAME}} to walk through what happened. Keep questions focused:
   - What was the intended outcome?
   - What actually happened?
   - When did things start going off track?

3. **The [[analyst]] builds the postmortem:**

   ```
   POSTMORTEM: [Event Name]
   ========================
   Date of event: [date]
   Date of review: [today]

   1. TIMELINE
   -----------
   What happened, in order:
   - [Date/Time]: [Event] — [Impact]
   - [Date/Time]: [Event] — [Impact]
   - ...

   2. WHAT WENT WELL
   -----------------
   Preserve and repeat:
   - [Positive 1] — [why it worked]
   - [Positive 2] — [why it worked]

   3. WHAT WENT WRONG
   ------------------
   Without blame — focus on systems, not people:
   - [Issue 1] — [observable impact]
   - [Issue 2] — [observable impact]

   4. ROOT CAUSES (5 Whys)
   -----------------------
   For each major failure:

   Issue: [Issue 1]
   - Why? [Because X]
   - Why? [Because Y]
   - Why? [Because Z]
   - Why? [Because W]
   - Why? [Root cause]
   → Root cause: [one-line summary]

   Issue: [Issue 2]
   - Why? ...
   → Root cause: [one-line summary]

   5. CONTRIBUTING FACTORS
   ----------------------
   Context that made failure more likely:
   - [Factor 1] — [how it contributed]
   - [Factor 2] — [how it contributed]

   6. PREVENTION ACTIONS
   ---------------------
   Specific, assigned, deadlined:
   - [ ] [Action 1] — Owner: [person] — Deadline: [date]
   - [ ] [Action 2] — Owner: [person] — Deadline: [date]

   7. LEARNINGS
   ------------
   What we now know that we didn't before:
   - [Learning 1]
   - [Learning 2]
   ```

4. **The [[critic]] challenges the conclusions:**
   - Are the root causes actually root causes, or symptoms?
   - Are there contributing factors being overlooked?
   - Are the prevention actions specific enough to actually prevent recurrence?
   - Is blame creeping in disguised as analysis?
   - What would a skeptic say about these conclusions?

5. **Auto-update brain files:**
   - Append validated learnings to `brain/learnings/strategies.md` with a reference to this postmortem
   - Append prevention decisions to `brain/context/decisions-log.md` with rationale
   - Update `brain/BRAIN_INDEX.md` with new last-updated dates

6. **Output the full postmortem in conversation.**

7. **Offer follow-up options:**
   - "Want me to create ClickUp tasks for the prevention actions?" (uses `/delegate`)
   - "Want me to draft a summary to share with the team?" (triggers `/draft`)
   - "Want me to dig deeper into any of the root causes?"
