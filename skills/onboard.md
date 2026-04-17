# Onboarding Session

Populate and refine the brain through a structured interview. Handles both initial onboarding (brain is empty) and refinement sessions (brain is already populated).

## When to Use

- First time setting up the assistant system
- Brain files feel incomplete or stale
- After a major change in role, projects, or priorities
- Periodic refinement of the brain

## Arguments

None. The skill auto-detects whether to run initial onboarding or refinement mode based on brain state.

## Instructions

1. **Assess brain state.** Read all brain files to determine which mode to use:
   - Read `brain/context/role-and-goals.md`
   - Read `brain/context/projects.md`
   - Read `brain/context/stakeholders.md`
   - Read `brain/context/decisions-log.md`
   - Read `brain/context/terminology.md`
   - Read `brain/preferences/communication.md`
   - Read `brain/preferences/analysis-style.md`
   - Read `brain/preferences/document-style.md`
   - Read `brain/preferences/priorities.md`
   - Read `brain/BRAIN_INDEX.md`

   If most files are empty, missing, or contain only placeholder content, enter **Initial Onboarding Mode**. Otherwise, enter **Refinement Mode**.

2. **Launch the onboarding-coach agent** (or perform the onboarding coach role if the agent is not yet defined).

---

### Initial Onboarding Mode

Run 5 focused rounds. Each round asks questions, then shows exactly what will be written to brain files for review before saving.

**Round 1: Who You Are** (~5 min)
Ask about:
- Role, title, responsibilities
- Company/organization and what it does
- Direct reports, manager, key collaborators
- What "winning" looks like this quarter and this year

After answers: Write to `brain/context/role-and-goals.md` and `brain/context/stakeholders.md`. Show the proposed content. Wait for confirmation before saving.

**Round 2: How You Work** (~5 min)
Ask about:
- Communication style preferences (formal/casual, detailed/concise)
- How analysis should be presented (bottom-line-up-front? deep dives?)
- Document formatting preferences (bullets? narrative? executive summary style?)
- Decision-making approach (data-driven? intuition? consensus?)

After answers: Write to `brain/preferences/communication.md`, `brain/preferences/analysis-style.md`, `brain/preferences/document-style.md`. Show proposed content. Wait for confirmation.

**Round 3: Current Projects** (~5 min)
Ask about:
- Active projects and their status
- Key milestones and deadlines
- Blockers and open questions
- Who is involved in what

After answers: Write to `brain/context/projects.md`. Update `brain/context/stakeholders.md` with project roles. Show proposed content. Wait for confirmation.

**Round 4: Your World** (~5 min)
Ask about:
- Key terminology and jargon specific to the domain
- Stakeholder map -- who matters and what they care about
- Competitive landscape -- who to watch
- Industry context the system should know

After answers: Write to `brain/context/terminology.md`. Update `brain/context/stakeholders.md`. Show proposed content. Wait for confirmation.

**Round 5: Teach Me Your Standards** (~5 min)
Ask about:
- Examples of documents that represent the desired style
- Analysis or strategies considered excellent
- Past decisions -- what worked, what did not
- Pet peeves or things to never do

After answers: Update `brain/preferences/` files and write to `brain/learnings/patterns.md`. Show proposed content. Wait for confirmation.

**After all rounds:**
- Write/update `brain/BRAIN_INDEX.md` with a complete index of all brain files
- Write to `brain/preferences/priorities.md` with synthesized priority framework
- Show a summary of everything captured
- Suggest next steps: `/ingest` resources, `/brief` for a test run

---

### Refinement Mode

For brains that are already populated:

1. **Identify gaps and staleness.** Review all brain files and find:
   - Files that have not been updated recently
   - Sections that are thin or marked with low confidence
   - Areas where information seems contradictory
   - Missing files that should exist based on other content

2. **Ask 5-10 targeted questions** about the weakest areas. Do not re-ask things already well-documented. Examples:
   - "Projects.md mentions the data pillar but has no timeline. When are the key milestones?"
   - "Stakeholders.md lists Sarah but does not describe her role. What does she do?"
   - "Your analysis style preferences are blank. How do you like analysis presented?"

3. **Update brain files** based on answers. Show every proposed change before writing.

4. **Update BRAIN_INDEX.md** with current state.

---

### Rules for Both Modes

- **Always show before saving.** Never write to a brain file without showing the proposed content first and getting confirmation.
- **Use proper frontmatter.** Every brain file must have the standard frontmatter:
  ```
  ---
  last_updated: [today's date]
  confidence: high|medium|low
  source: manual
  ---
  ```
- **Be conversational.** This is an interview, not a form. Ask follow-up questions when answers are interesting or unclear.
- **One round at a time.** Do not dump all questions at once. Complete each round before moving to the next.
- **Respect the user's time.** If {{USER_FIRST_NAME}} wants to stop partway through, save progress and note where to resume.
