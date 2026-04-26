# Competitive Intelligence Pipeline

See also [[market-researcher]], [[analyst]], [[writer]], [[brain/OUTPUT_CONTRACTS|Output Contracts]].

## Trigger
- "research competitors and analyze"
- "competitive analysis of X"
- "what are others doing with X"

## Steps

### Step 1: Research
- **Skill**: /research
- **Agent**: Market Researcher
- **Input**: User's research question
- **Output contract**: /research (findings, competitive_landscape, trends, sources)
- **Brain files**: Hot tier + terminology

### Step 2: Analyze
- **Skill**: /analyze
- **Agent**: Analyst
- **Input**: Step 1 output (research findings)
- **Output contract**: /analyze (key_findings, implications, risks, recommended_actions)
- **Brain files**: Hot tier + projects (to contextualize findings)

### Step 3: Draft Brief
- **Skill**: /draft
- **Agent**: Writer
- **Input**: Step 2 output (analysis)
- **Output contract**: /draft (document, format="competitive brief")
- **Brain files**: document-style, communication

### Step 4 (Optional): Challenge
- **Skill**: /challenge
- **Agent**: Critic
- **Input**: Step 3 output (draft brief)
- **Trigger**: Only if user requests or findings are high-stakes
- **Output contract**: /challenge (blind_spots, assumptions_challenged, severity_ratings)

## Error Handling
- Step 1 fails (no results): Surface to user with "Couldn't find relevant competitive data. Want to refine the search?"
- Step 2 fails: Return raw research findings without analysis
- Step 3 fails: Return analysis without formatting

## Output
- Saved to: `output/analyses/{date}-competitive-intel-{topic}.md`
- Offered follow-ups: /strategize (build strategy from findings), /repurpose (share findings)
