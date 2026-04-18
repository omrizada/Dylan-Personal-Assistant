# Multi-Framework Task Prioritization

Rank tasks using multiple prioritization frameworks to surface the highest-leverage work. Invokes the [[strategist]] agent.

## When to Use

- You have a backlog of tasks and need to decide what to focus on
- Weekly planning sessions
- When everything feels urgent and you need clarity
- Evaluating whether current priorities still make sense

## Arguments

- **tasks** (required): A list of tasks to prioritize. Can be:
  - Pasted list in the conversation
  - `pull from ClickUp` -- fetch tasks from ClickUp workspace

## Instructions

1. **Load brain context.** Read all relevant brain files:
   - `brain/context/projects.md` -- active projects for alignment check
   - `brain/context/okrs.md` -- current OKRs for alignment scoring
   - `brain/preferences/priorities.md` -- decision-making weights and what matters most
   - `brain/context/role-and-goals.md` -- overarching objectives
   - `brain/learnings/strategies.md` -- proven approaches

2. **Gather the task list.** If "pull from ClickUp" is specified, use ClickUp tools to fetch active tasks. Otherwise, parse the pasted list.

3. **Route to the strategist agent.** Run each task through all four frameworks:

   ### Framework 1: Eisenhower Matrix
   Classify each task into one of four quadrants:
   ```
   EISENHOWER MATRIX
   ┌──────────────────────┬──────────────────────┐
   │ URGENT + IMPORTANT   │ NOT URGENT + IMPORTANT│
   │ → Do first           │ → Schedule            │
   │                      │                       │
   │ [tasks]              │ [tasks]               │
   ├──────────────────────┼──────────────────────┤
   │ URGENT + NOT IMPORTANT│ NOT URGENT + NOT IMP │
   │ → Delegate           │ → Eliminate           │
   │                      │                       │
   │ [tasks]              │ [tasks]               │
   └──────────────────────┴──────────────────────┘
   ```

   ### Framework 2: ICE Scoring
   Score each task on three dimensions (1-10 scale):
   - **Impact**: How much will this move the needle?
   - **Confidence**: How sure are we of the impact estimate?
   - **Ease**: How easy is this to execute?
   - **ICE Score** = Impact x Confidence x Ease

   ```
   | Task | Impact | Confidence | Ease | ICE Score |
   |------|--------|------------|------|-----------|
   ```

   ### Framework 3: OKR Alignment
   For each task, assess alignment with current OKRs from `brain/context/okrs.md`:
   - Which objective does this serve?
   - Which key result does this move?
   - Alignment score: Strong / Moderate / Weak / None

   ```
   | Task | Objective | Key Result | Alignment |
   |------|-----------|------------|-----------|
   ```

   ### Framework 4: Energy Matching
   Categorize each task by the type of energy it requires:
   - **Deep Work**: Requires focus, creativity, uninterrupted time
   - **Admin**: Process-oriented, low cognitive load
   - **Creative**: Brainstorming, writing, ideation
   - **Collaborative**: Requires other people, meetings, alignment

   Suggest optimal time-of-day and context for each category.

4. **Synthesize a final ranked stack.** Combine signals from all four frameworks into a single prioritized list:

   ```
   FINAL PRIORITY STACK
   ====================

   1. [Task] — ICE: X | Eisenhower: Q1 | OKR: Strong | Energy: Deep Work
      WHY TOP: [1-sentence rationale]

   2. [Task] — ICE: X | Eisenhower: Q1 | OKR: Strong | Energy: Admin
      WHY HERE: [1-sentence rationale]

   ...

   BOTTOM OF STACK:
   N. [Task] — ICE: X | Eisenhower: Q4 | OKR: None | Energy: Admin
      WHY BOTTOM: [1-sentence rationale]
   ```

5. **Include rationale for top 3 and bottom 3 positions.** Explain why the highest-priority items deserve immediate focus and why the lowest-priority items can be deferred or eliminated.

6. **Present in the conversation.** Show the full analysis with all four frameworks, followed by the synthesized stack.

7. **Offer follow-up options:**
   - "Want me to create a schedule for the top items?" (triggers `/strategize`)
   - "Want me to challenge this ranking?" (triggers `/challenge`)
   - "Want me to update OKR progress based on completed items?" (triggers `/okr update`)

See also: [[priorities]]
