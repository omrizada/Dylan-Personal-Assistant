# Market Research

Research a topic using web search to gather competitive intelligence, best practices, trends, and benchmarks. Produces a structured research brief with sources and confidence levels.

## When to Use

- Competitive intelligence -- what are competitors doing?
- Best practices -- how do others approach this problem?
- Market trends -- what is changing in the industry?
- Benchmarks -- what does "good" look like?
- Validating assumptions with external data

## Arguments

- **topic** (required): A topic, question, or area to research.
  - Examples:
    - `what are the best practices for job post optimization in 2026?`
    - `competitive landscape for AI-powered recruitment tools`
    - `benchmarks for enterprise SaaS retention rates`
    - `what is Company X doing in the job matching space?`

## Instructions

1. **Load brain context first.** Read relevant brain files to understand what {{USER_FIRST_NAME}} already knows and what matters:
   - `brain/context/role-and-goals.md` -- what {{USER_FIRST_NAME}} is working on
   - `brain/context/projects.md` -- active projects for relevance filtering
   - `brain/context/terminology.md` -- domain vocabulary
   - `brain/resources/insights/` -- existing knowledge to build on, not duplicate

2. **Launch the market-researcher agent** (or perform the market researcher role if the agent is not yet defined).

3. **Conduct web research.** Use WebSearch and WebFetch tools to:
   - Search for the topic from multiple angles (competitors, trends, best practices, data)
   - Visit and read the most relevant results
   - Look for recent information (prioritize 2025-2026 sources)
   - Gather data points, quotes, and specific examples
   - Collect source URLs for everything

4. **Cross-reference with brain context.** For every finding, consider:
   - How does this relate to {{USER_FIRST_NAME}}'s active projects?
   - Does this confirm or contradict existing assumptions?
   - What are the implications for {{USER_FIRST_NAME}}'s work specifically?

5. **Rate confidence levels** for each finding:
   - **High** -- Multiple credible sources confirm this
   - **Medium** -- Some evidence supports this, but limited sources
   - **Low** -- Single source or speculative; needs further validation

6. **Structure the output** as a research brief:

   ```
   RESEARCH BRIEF: [Topic]
   Date: [today's date]
   =======================

   EXECUTIVE SUMMARY
   Top 3-5 findings in bullet points.

   KEY FINDINGS

   Finding 1: [Title]
   Confidence: High / Medium / Low
   - Details and evidence
   - Source: [URL or publication]

   Finding 2: [Title]
   Confidence: High / Medium / Low
   - Details and evidence
   - Source: [URL or publication]

   (continue for all findings)

   COMPETITIVE LANDSCAPE
   (if applicable)
   - Competitor A: What they are doing, strengths, weaknesses
   - Competitor B: ...

   TRENDS AND PATTERNS
   What direction is the market moving? What is emerging?

   BENCHMARKS
   (if applicable)
   Relevant data points for comparison.

   IMPLICATIONS FOR {{USER_FIRST_NAME}}
   What this means for active projects and goals.
   Specific opportunities or threats to watch.

   GAPS AND LIMITATIONS
   What this research could not answer.
   Suggested follow-up research topics.

   SOURCES
   Numbered list of all sources with URLs.
   ```

7. **Save the report.** Write to `output/analyses/research-[topic-slug]-[date].md`. Create the directory if it does not exist.

8. **Offer follow-up options:**
   - "Want me to analyze these findings in depth?" (triggers `/analyze`)
   - "Want me to build a strategy based on this research?" (triggers `/strategize`)
   - "Want me to challenge any of these findings?" (triggers `/challenge`)
   - "Should I ingest any of the source documents into the brain?" (triggers `/ingest`)
