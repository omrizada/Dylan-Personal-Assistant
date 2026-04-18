# Status Report Generator

Auto-generate status reports tailored to different audiences. Invokes the [[writer]] agent with [[analyst]] input for data synthesis.

## When to Use

- Preparing a weekly or monthly status update
- Reporting to leadership, board, clients, or your team
- Need a quick snapshot of project status for a specific audience
- Before a meeting where you need to present progress

## Arguments

- **audience** (required): The audience type for the report.
  - `executive` -- 1-page summary for senior leadership
  - `team` -- detailed breakdown for internal team
  - `client` -- external-facing progress report
  - `board` -- high-level strategic overview for board members

## Instructions

1. **Load brain context.** Read all relevant brain files:
   - `brain/context/projects.md` -- active projects, status, milestones
   - `brain/context/stakeholders.md` -- who cares about what
   - `brain/preferences/document-style.md` -- formatting and structure preferences
   - `brain/preferences/communication.md` -- tone and voice
   - `brain/context/decisions-log.md` -- recent decisions to highlight
   - `brain/learnings/strategies.md` -- context for strategic framing

2. **Route to the writer agent** with analyst support. The analyst synthesizes project data and metrics; the writer structures and formats the report for the target audience.

3. **Generate the report based on audience type:**

   ### Executive (`executive`)
   One-page maximum. Structure:
   ```
   STATUS REPORT — [Date]
   ======================

   OVERALL STATUS: [On Track / At Risk / Off Track]

   KEY METRICS
   - Metric 1: value (trend)
   - Metric 2: value (trend)

   PROJECT STATUS
   | Project | Status | Progress | Next Milestone |
   |---------|--------|----------|----------------|

   TOP RISKS
   - Risk with mitigation plan

   DECISIONS NEEDED
   - Decision with context and deadline
   ```

   ### Team (`team`)
   Detailed breakdown. Structure:
   ```
   TEAM STATUS REPORT — [Date]
   ===========================

   PER-PROJECT BREAKDOWN
   For each active project:
   - Status and progress since last report
   - Completed items this period
   - Current blockers and dependencies
   - Action items with owners and deadlines
   - Next steps

   CROSS-PROJECT DEPENDENCIES
   - Dependency map between projects

   TEAM ACTION ITEMS
   | Action | Owner | Deadline | Priority |
   |--------|-------|----------|----------|

   BLOCKERS REQUIRING ESCALATION
   - Blocker with proposed resolution
   ```

   ### Client (`client`)
   External-facing, no internal jargon. Structure:
   ```
   PROGRESS REPORT — [Date]
   ========================

   EXECUTIVE SUMMARY
   Brief, positive, professional summary of progress.

   MILESTONES
   | Milestone | Target Date | Status |
   |-----------|-------------|--------|

   PROGRESS HIGHLIGHTS
   - Achievement 1 with business impact
   - Achievement 2 with business impact

   NEXT STEPS
   - What's coming next with expected timelines

   ITEMS FOR DISCUSSION
   - Topics that need client input or decision
   ```

   ### Board (`board`)
   High-level strategic view. Structure:
   ```
   BOARD UPDATE — [Date]
   =====================

   STRATEGIC SUMMARY
   2-3 sentences on overall trajectory.

   KEY PERFORMANCE INDICATORS
   | KPI | Target | Actual | Trend |
   |-----|--------|--------|-------|

   STRATEGIC INITIATIVES
   For each major initiative:
   - Business impact and progress
   - Investment and ROI indicators

   RISKS AND MITIGATION
   - Strategic risks with mitigation approach

   TRAJECTORY
   Where we're heading and what it means for the business.
   ```

4. **Formatting rules:**
   - Adapt language and depth to the audience -- no internal jargon in client/board reports
   - Use data and metrics where available; flag where data is missing
   - Keep executive and board reports concise (1-2 pages max)
   - Highlight items that need action or decisions prominently

5. **Save the report.** Write to `output/documents/{date}-{audience}-report.md`. Create the directory if it does not exist.

6. **Offer follow-up options:**
   - "Want me to adapt this for a different audience?" (re-run with different audience type)
   - "Want me to analyze any of these areas deeper?" (triggers `/analyze`)
   - "Want me to draft an email to send this report?" (triggers `/draft`)
