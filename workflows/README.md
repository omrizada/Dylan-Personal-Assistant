# Workflows

Formal pipeline definitions for multi-skill chains. The [[chief-of-staff|Chief of Staff]] executes these when a request matches a workflow pattern.

## How Workflows Work

1. User request matches a workflow pattern (or user explicitly invokes one)
2. Chief of Staff loads the workflow definition
3. Each step executes in order, passing output to the next step
4. Steps reference `brain/OUTPUT_CONTRACTS.md` for typed input/output
5. If a step fails, the error handler kicks in (retry, skip, or surface to user)

## Available Workflows

| Workflow | File | Pattern |
|----------|------|---------|
| Competitive Intelligence | `competitive-intel.md` | "research competitors then analyze" |
| Decision Pipeline | `decision-pipeline.md` | Making a big decision with full analysis |
| Document Pipeline | `document-pipeline.md` | Research → Analyze → Draft → Review |
| Weekly Ops | `weekly-ops.md` | End-of-week review + planning cycle |
| Inbox Zero | `inbox-zero.md` | Triage → Followup → Delegate |
