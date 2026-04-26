---
last_updated:
---

# Output Contracts

Defines structured output formats for skills that chain into other skills. When a skill has a contract, its output MUST include the specified fields. See also [[LOADING_PROTOCOL]], [[frameworks]], [[Dashboard]].

## Why Contracts Matter

When skills chain (e.g., `/analyze` --> `/strategize` --> `/challenge`), each skill needs to know what format to expect from the previous one. Contracts ensure:
- Outputs are parseable by the next skill in the chain
- No information is lost between steps
- The Chief of Staff can verify output quality before passing it forward

## Contract Format

Each contract specifies required fields using this pattern:
```
### /skill-name Output Contract
**Produces**: [what this skill outputs]
**Consumed by**: [which skills use this output]
**Required fields**:
- field_name: description
```

---

## Analysis Contracts

### /analyze Output Contract
**Produces**: Structured analysis report
**Consumed by**: /strategize, /challenge, /draft, /report
**Required fields**:
- **executive_summary**: 2-3 sentence summary of findings
- **key_findings**: Bulleted list of 3-7 findings, each with evidence
- **frameworks_applied**: Which frameworks were used and their conclusions
- **implications**: What the findings mean for active projects
- **risks_identified**: Potential risks with severity (high/medium/low)
- **recommended_actions**: Numbered list of concrete next steps
- **confidence_level**: Overall confidence (high/medium/low) with reasoning
- **data_gaps**: What information is missing that would improve the analysis

### /research Output Contract
**Produces**: Market/competitive research brief
**Consumed by**: /analyze, /strategize, /draft, /report
**Required fields**:
- **executive_summary**: 2-3 sentence overview
- **findings**: Structured by source/topic with confidence ratings per finding
- **competitive_landscape**: Key players, their positions, and implications
- **trends**: Identified trends with trajectory (growing/stable/declining)
- **implications_for_user**: How findings connect to brain/context/projects.md
- **sources**: List of sources with credibility assessment
- **confidence_level**: Overall and per-finding
- **gaps_and_limitations**: What couldn't be verified or found

### /extract-wisdom Output Contract
**Produces**: Quick content extraction
**Consumed by**: /analyze, /strategize, /learn
**Required fields**:
- **key_ideas**: 5 numbered ideas, one sentence each
- **surprising_insights**: 3 insights that challenge assumptions
- **actionable_recommendations**: Steps the user could take
- **memorable_quotes**: 2-3 quotes worth remembering
- **brain_connections**: Links to existing brain knowledge

---

## Strategy Contracts

### /strategize Output Contract
**Produces**: Strategic plan with options
**Consumed by**: /challenge, /draft, /decide, /report
**Required fields**:
- **situation_assessment**: Current state summary grounded in brain context
- **options**: 2-4 strategic options, each with: description, pros, cons, effort, risk
- **recommended_option**: Which option and why
- **execution_plan**: Phased steps with owners and timelines
- **success_metrics**: How to measure if the strategy works
- **risks_and_mitigations**: Risk table with mitigation strategies
- **decision_needed**: What the user needs to decide

### /decide Output Contract
**Produces**: Decision framework analysis
**Consumed by**: /draft (for decision memos), /postmortem (for retrospectives)
**Required fields**:
- **decision_question**: The question being decided
- **options_evaluated**: Each option with scored pros/cons
- **framework_used**: Which decision framework and why
- **recommendation**: Clear recommendation with confidence
- **trade_offs**: What you give up with the recommended option
- **reversibility**: How easy is it to reverse this decision?
- **decision_record**: Ready to append to brain/context/decisions-log.md

### /prioritize Output Contract
**Produces**: Ranked task list
**Consumed by**: /weekly-review, /delegate, /okr
**Required fields**:
- **ranked_list**: Tasks in priority order with scores
- **framework_scores**: Per-task breakdown (Eisenhower, ICE, OKR alignment, energy)
- **rationale**: Why #1 is #1 and why the last item is last
- **quick_wins**: Items that are high-impact + low-effort
- **defer_candidates**: Items that can wait without consequence

---

## Execution Contracts

### /meeting-prep Output Contract
**Produces**: Pre-meeting briefing
**Consumed by**: /draft (for agendas), /followup (for action items post-meeting)
**Required fields**:
- **meeting_info**: Name, time, attendees
- **attendee_context**: Per-person: role, what they care about, recent interactions
- **relevant_status**: Project updates relevant to the meeting topic
- **open_items**: Unresolved issues from prior meetings
- **suggested_talking_points**: 3-5 points the user should raise
- **preparation_needed**: Anything to review or prepare before the meeting

### /triage Output Contract
**Produces**: Classified inbox with draft responses
**Consumed by**: /followup (for commitments extracted), /delegate (for action items)
**Required fields**:
- **urgent**: Messages requiring immediate response, with draft responses
- **needs_response**: Messages needing a thoughtful reply, with draft responses
- **fyi**: Informational messages, one-line summary each
- **noise**: Messages that can be ignored
- **action_items_extracted**: Commitments or tasks identified, ready for /followup add
- **total_processed**: Count of messages classified

### /weekly-review Output Contract
**Produces**: Week retrospective + next week plan
**Consumed by**: /brief (for Monday morning context), /okr (for progress tracking)
**Required fields**:
- **completed_this_week**: What got done
- **slipped_this_week**: What didn't get done and why
- **decisions_made**: Key decisions with rationale
- **patterns_observed**: Recurring themes or behaviors
- **next_week_priorities**: Top 3-5 items for next week
- **follow_ups_due**: Commitments coming due next week
- **brain_updates_needed**: Suggested brain file changes

### /followup Output Contract
**Produces**: Commitment status report
**Consumed by**: /brief, /weekly-review, /delegate
**Required fields**:
- **overdue**: Commitments past deadline with days overdue
- **due_soon**: Commitments due within 3 days
- **on_track**: Active commitments not yet due
- **recently_completed**: Items marked done in the last 7 days
- **nudge_drafts**: Pre-written reminder messages for overdue items

---

## Creation Contracts

### /draft Output Contract
**Produces**: Document matching user's style
**Consumed by**: /challenge (for review), /repurpose (for reformatting)
**Required fields**:
- **document**: The full document text
- **format**: What type (email, report, presentation, brief, etc.)
- **audience**: Who this is for
- **tone**: Formal/informal/technical
- **file_saved**: Path where the document was saved

### /report Output Contract
**Produces**: Audience-formatted status report
**Consumed by**: /repurpose, /draft
**Required fields**:
- **report**: The full report text
- **audience**: executive/team/client/board
- **key_metrics**: Metrics included with current values
- **status_indicators**: On-track/at-risk/off-track per project
- **decisions_needed**: Items requiring reader action

---

## Review Contracts

### /challenge Output Contract
**Produces**: Devil's advocate analysis
**Consumed by**: /strategize (for plan revision), /decide (for decision refinement)
**Required fields**:
- **blind_spots**: Issues the original plan missed
- **assumptions_challenged**: Assumptions that may be wrong, with alternatives
- **risks_surfaced**: New risks not in the original analysis
- **severity_ratings**: Each finding rated critical/high/medium/low
- **constructive_alternatives**: For each criticism, a suggested improvement
- **overall_assessment**: Summary judgment with confidence

### /premortem Output Contract
**Produces**: Failure mode analysis
**Consumed by**: /strategize (for plan hardening), /decide (for risk awareness)
**Required fields**:
- **failure_modes**: Each with description, likelihood (1-5), impact (1-5), risk_score
- **top_3_risks**: Highest risk_score items with detailed prevention plans
- **early_warning_signs**: What to watch for that indicates trouble
- **fallback_plans**: What to do if each failure mode materializes
- **prevention_actions**: Concrete steps to reduce risk before launch

### /postmortem Output Contract
**Produces**: After-action review
**Consumed by**: /learn (for brain updates), /strategize (for future planning)
**Required fields**:
- **timeline**: What happened, in chronological order
- **what_went_well**: Practices to preserve
- **what_went_wrong**: Issues without blame
- **root_causes**: 5 Whys analysis for each failure
- **prevention_actions**: Assigned, deadlined actions
- **learnings**: Key takeaways for brain/learnings/strategies.md
