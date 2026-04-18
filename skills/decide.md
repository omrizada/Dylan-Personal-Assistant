# Decision Framework

Structured decision-making with trade-off analysis and stress testing.

## Arguments
- **question** (required): The decision to be made

## Instructions

1. Load brain context: `brain/context/projects.md`, `brain/context/decisions-log.md`, `brain/preferences/priorities.md`
2. Route to **Strategist** for option generation and analysis
3. Route to **Critic** for stress-testing each option
4. Synthesize into a decision framework

## Output Format

```
## Decision: [Question]

### Options
| Option | Pros | Cons | Risk Level |
|--------|------|------|-----------|

### Strategist Analysis
[Framework-based evaluation]

### Critic's Challenge
[Stress test of each option]

### Recommendation
[Clear recommendation with rationale]

### Decision Record
If you decide, I'll log this to brain/context/decisions-log.md with:
- Decision made
- Options considered
- Rationale
- Date
```
