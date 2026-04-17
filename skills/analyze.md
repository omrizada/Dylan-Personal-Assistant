# Deep Analysis

Perform thorough analysis of a topic, question, or resource using the full brain context and structured analytical frameworks.

## When to Use

- Analyzing a document or dataset
- Answering a complex question that requires structured thinking
- Identifying trends, gaps, risks, or opportunities
- Cross-referencing multiple sources of information

## Arguments

- **topic** (required): A topic, question, or file path to analyze.
  - Examples:
    - `the execution gaps in our Job Post Bet plan`
    - `resources/q1-metrics.xlsx`
    - `why is retention dropping in the enterprise segment?`

## Instructions

1. **Load brain context.** Read all relevant brain files before beginning analysis:
   - `brain/context/` -- all files, for full situational awareness
   - `brain/preferences/analysis-style.md` -- how {{USER_FIRST_NAME}} wants analysis presented
   - `brain/resources/summaries/` and `brain/resources/insights/` -- relevant digested resources
   - `brain/learnings/` -- patterns and strategies that may apply

2. **If the argument is a file path**, read the file first. If it has not been ingested yet, suggest running `/ingest` first but proceed with analysis regardless.

3. **Launch the analyst agent** (or perform the analyst role if the agent is not yet defined). Apply relevant analytical frameworks based on the topic:
   - **SWOT** -- for strategic position analysis
   - **Root Cause Analysis** -- for problems and failures
   - **Pareto Analysis** -- for prioritization questions
   - **Gap Analysis** -- for plan vs. reality comparisons
   - **Trend Analysis** -- for data over time
   - **Stakeholder Analysis** -- for people/org dynamics
   - Choose the most appropriate framework(s); do not force-fit

4. **Cross-reference with brain knowledge.** The analysis must not exist in a vacuum. Connect findings to:
   - Active projects and their status
   - Known stakeholder positions and interests
   - Previous decisions and their outcomes
   - Patterns observed in past interactions

5. **Structure the output** as a formal analysis report:

   ```
   ANALYSIS: [Topic]
   Date: [today's date]
   ==================

   EXECUTIVE SUMMARY
   One paragraph -- the bottom line.

   KEY FINDINGS
   1. Finding with supporting evidence
   2. Finding with supporting evidence
   3. ...

   FRAMEWORK APPLICATION
   [Name of framework used]
   - Structured output of the framework

   CONNECTIONS TO CURRENT CONTEXT
   - How this relates to active projects
   - Implications for stakeholders
   - Alignment or conflict with existing strategies

   RISKS AND BLIND SPOTS
   - What could go wrong
   - What might be missing from this analysis

   RECOMMENDATIONS
   1. Specific, actionable recommendation
   2. ...

   CONFIDENCE LEVEL
   High / Medium / Low -- with explanation of what would increase confidence
   ```

6. **Save the report.** Write the analysis to `output/analyses/[topic-slug]-[date].md`. Create the directory if it does not exist.

7. **Offer follow-up options:**
   - "Want me to challenge these findings?" (triggers `/challenge`)
   - "Want me to turn this into a strategy?" (triggers `/strategize`)
   - "Want me to draft a document based on this?" (triggers `/draft`)
