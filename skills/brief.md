# Morning Briefing

Synthesize the current state of {{USER_FIRST_NAME}}'s world into a scannable briefing that takes under 2 minutes to read.

## When to Use

- Start of day catch-up
- Before meetings where you need full context
- After being away for a few days
- Anytime you want a snapshot of where things stand

## Arguments

None. This skill reads all available brain context automatically.

## Instructions

1. **Load all brain context files.** Read every file in these directories:
   - `brain/context/` (projects, stakeholders, decisions-log, role-and-goals, terminology)
   - `brain/learnings/` (patterns, feedback, strategies)
   - `brain/resources/insights/` (cross-resource insights)
   - `brain/BRAIN_INDEX.md` (for completeness check)

2. **Synthesize into a structured briefing.** Organize the output as follows:

   ```
   BRIEFING - [Today's Date]
   ========================

   ACTIVE PROJECTS
   ---------------
   For each project:
   - Status (on track / at risk / blocked)
   - Recent changes or progress since last update
   - Next milestone and deadline
   - Key blockers or open questions

   PENDING DECISIONS
   -----------------
   - Decisions that need to be made, with context
   - Decisions recently made, with rationale (from decisions-log)

   ACTION ITEMS
   ------------
   - Concrete next steps extracted from projects and decisions
   - Ordered by urgency

   RECENT CHANGES
   --------------
   - What changed in brain files since last briefing
   - New resources ingested
   - New learnings captured

   STAKEHOLDER UPDATES
   -------------------
   - Any notable changes in stakeholder context
   - Upcoming interactions to prepare for
   ```

3. **Formatting rules:**
   - Keep each section concise -- bullet points, not paragraphs
   - Highlight anything time-sensitive or requiring immediate action
   - If a brain file is empty or missing, note it as "not yet populated" rather than skipping it
   - If the brain is mostly empty (system not yet onboarded), say so and suggest running `/onboard`

4. **Do NOT create or save a file.** Output the briefing directly in the conversation. This is a read-only operation.
