# Document Creation

Create polished documents that match {{USER_FIRST_NAME}}'s communication style and formatting preferences. Always shows a draft for review before finalizing.

## When to Use

- Creating executive summaries, reports, briefs
- Drafting emails or presentations
- Writing strategic plans or proposals
- Any document creation request

## Arguments

- **document_type** (required): The type of document to create (e.g., executive summary, email, report, brief, proposal, presentation outline).
- **topic** (required): What the document is about.
- Examples:
  - `/draft executive summary Q1 progress on the main project`
  - `/draft email to the board summarizing our pivot decision`
  - `/draft brief competitive landscape in job optimization`

## Instructions

1. **Load style preferences first.** Before writing anything, read these files:
   - `brain/preferences/document-style.md` -- templates, formatting, structure preferences
   - `brain/preferences/communication.md` -- tone, formality, detail level
   - If either file is empty or missing, note this and use sensible professional defaults. Suggest running `/onboard` to set preferences.

2. **Load relevant brain context:**
   - `brain/context/` -- all files relevant to the topic
   - `brain/resources/summaries/` and `brain/resources/insights/` -- relevant digested resources
   - `output/analyses/` -- any existing analyses on the topic
   - `output/strategies/` -- any existing strategies on the topic

3. **Launch the writer agent** (or perform the writer role if the agent is not yet defined).

4. **Create the first draft.** Follow these rules:
   - Match {{USER_FIRST_NAME}}'s documented communication style and preferences
   - Adapt tone for the intended audience (infer from document type and topic)
   - Use the structure and formatting patterns from `document-style.md`
   - Ground all claims in brain context and ingested resources -- do not fabricate data
   - If information is missing, flag it with `[TODO: ...]` placeholders

5. **Present the draft for review.** Show the full draft in the conversation and ask:
   - "Does the tone and level of detail work?"
   - "Anything to add, remove, or change?"
   - "Who is the intended audience?" (if not already clear)

6. **Iterate based on feedback.** Make requested changes. Show the revised version. Repeat until {{USER_FIRST_NAME}} approves.

7. **Save the final version.** Once approved, write to `output/documents/[type]-[topic-slug]-[date].md`. Create the directory if it does not exist.

8. **Capture style learnings.** If {{USER_FIRST_NAME}} made corrections or expressed preferences during the review:
   - Propose updates to `brain/preferences/document-style.md` or `brain/preferences/communication.md`
   - Show the proposed updates before applying
   - This makes future drafts better
