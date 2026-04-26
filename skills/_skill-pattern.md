# Skill Pattern Reference

All skills follow this structure. When creating a new skill, copy this pattern and fill in the specifics.

## Standard Structure

```
# [Skill Name]

[One-line description]. Routes to [[agent-name]].

## When to Use
[2-3 bullet points of trigger conditions]

## Arguments
- **arg** (required/optional): Description

## Instructions

1. **Load context**: Follow `brain/LOADING_PROTOCOL.md`. For this skill, load: [specific files]
2. [Skill-specific step]
3. [Skill-specific step]
4. **Format output**: [output template]
5. **Save**: `output/{type}/{date}-{slug}.md`

## Follow-Up Options
- [Related skill 1]
- [Related skill 2]
```

## Brain Loading Shorthand

Instead of listing every brain file, use tier references:
- "Load hot tier" = role-and-goals.md, projects.md, priorities.md
- "Load warm: stakeholders, terminology" = add those to hot
- "Load cold: [specific file]" = only when explicitly needed

## Output Routing

| Skill Type | Save To |
|-----------|---------|
| Analysis | output/analyses/ |
| Strategy | output/strategies/ |
| Document | output/documents/ |
| Inline response | No file saved |

## Output Contracts

If the skill has a defined output contract in `brain/OUTPUT_CONTRACTS.md`, the output MUST include all required fields. This ensures downstream skills can parse and use the output correctly.

Check `brain/OUTPUT_CONTRACTS.md` for:
- What fields are required for this skill's output
- Which skills consume this output
- The expected format for each field

## Standard Follow-Up Pattern

After every skill execution, offer 2-3 relevant follow-ups:
- "Want me to /challenge this?"
- "Should I /draft a summary?"
- "Run /followup to track action items?"
