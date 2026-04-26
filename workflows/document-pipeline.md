# Document Pipeline

End-to-end document creation with research and review. See also [[writer]], [[analyst]], [[critic]], [[brain/OUTPUT_CONTRACTS|Output Contracts]].

## Trigger
- "create a comprehensive report on X"
- "write a well-researched document about X"
- "I need a [type] about [topic] for [audience]"

## Steps

### Step 1: Research (if needed)
- **Skill**: /research OR /analyze (based on whether external or internal data)
- **Condition**: Skip if user provides all source material
- **Output contract**: /research or /analyze

### Step 2: Draft
- **Skill**: /draft
- **Agent**: Writer
- **Input**: Research/analysis + user's brief
- **Output contract**: /draft (document, format, audience, tone)

### Step 3: Review
- **Skill**: /challenge
- **Agent**: Critic
- **Input**: Step 2 draft
- **Output contract**: /challenge (blind_spots, constructive_alternatives)

### Step 4: Revise
- **Agent**: Writer
- **Input**: Step 2 draft + Step 3 critique
- **Output**: Final document incorporating critic feedback

### Step 5: Format Variants (optional)
- **Skill**: /repurpose
- **Condition**: Only if user wants multiple formats
- **Input**: Step 4 final document

## Output
- Saved to: `output/documents/{date}-{type}-{topic}.md`
- Offered: /repurpose, /challenge (another round)
