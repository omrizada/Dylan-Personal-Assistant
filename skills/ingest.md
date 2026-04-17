# Resource Ingestion

Process a file or folder of files into the brain's knowledge system. Creates summaries, extracts insights, and updates relevant brain context files.

## When to Use

- New document added to `resources/`
- Batch processing multiple files
- Re-ingesting a resource after it has been updated

## Arguments

- **path** (required): A file path or folder path to ingest. Can be absolute or relative to the project root.
  - Examples: `resources/report.pdf`, `resources/`, `{{PROJECT_DIR}}

## Instructions

1. **Validate the input path.** Confirm the file or folder exists. If it is a folder, list all files in it. Filter to supported types: `.docx`, `.xlsx`, `.pptx`, `.pdf`, `.md`. Warn about and skip unsupported file types.

2. **Check for already-ingested files.** Look in `resources/ingested/` for a marker file matching each resource filename. If found, ask {{USER_FIRST_NAME}} whether to re-ingest or skip. Marker files are named `{original-filename}.ingested.md`.

3. **For each file, launch the librarian agent** (or perform the librarian role if the agent is not yet defined) to do the following:

   a. **Read the resource.** Use the appropriate tool for the file type:
      - `.pdf` -- Read tool with page ranges for large files
      - `.md` -- Read tool directly
      - `.docx`, `.xlsx`, `.pptx` -- Read tool (Claude Code supports these natively)

   b. **Create a summary.** Write a structured summary to `brain/resources/summaries/{filename}-summary.md` with this format:
      ```
      ---
      last_updated: [today's date]
      source_file: [original path]
      confidence: high
      ---

      # Summary: [Document Title or Filename]

      ## Key Points
      - Top 5-10 takeaways

      ## Detailed Summary
      Structured breakdown of the document contents

      ## Relevance
      How this connects to {{USER_FIRST_NAME}}'s active projects and goals
      ```

   c. **Extract insights.** Write cross-cutting insights to `brain/resources/insights/{filename}-insights.md`:
      ```
      ---
      last_updated: [today's date]
      source_file: [original path]
      ---

      # Insights: [Document Title or Filename]

      ## Key Insights
      - Non-obvious findings, implications, connections

      ## Connections to Existing Knowledge
      - How this relates to what is already in the brain

      ## Questions Raised
      - Things that need further investigation or clarification

      ## Suggested Actions
      - Concrete steps suggested by this resource
      ```

   d. **Update brain context files.** Scan the resource for:
      - New people mentioned --> update `brain/context/stakeholders.md`
      - New projects or project updates --> update `brain/context/projects.md`
      - Domain terminology --> update `brain/context/terminology.md`
      - Show {{USER_FIRST_NAME}} what changes are being proposed to context files before writing

   e. **Mark as ingested.** Create `resources/ingested/{filename}.ingested.md` containing:
      ```
      ---
      ingested_date: [today's date]
      source_file: [original path]
      summary_file: brain/resources/summaries/{filename}-summary.md
      insights_file: brain/resources/insights/{filename}-insights.md
      ---
      ```

4. **Update BRAIN_INDEX.md.** Add entries for the new summary and insights files.

5. **Report results.** Show {{USER_FIRST_NAME}}:
   - How many files were processed
   - Summary of key findings across all ingested files
   - What brain context files were updated
   - Any files that were skipped and why
