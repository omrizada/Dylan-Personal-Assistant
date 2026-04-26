# Decision Pipeline

Full analysis workflow for significant decisions. See also [[strategist]], [[critic]], [[brain/OUTPUT_CONTRACTS|Output Contracts]].

## Trigger
- "I need to make a decision about X"
- "help me decide between X and Y"
- Explicitly via: "run the decision pipeline for X"

## Steps

### Step 1: Analyze Context
- **Skill**: /analyze
- **Agent**: Analyst
- **Input**: Decision question + relevant brain context
- **Output contract**: /analyze (key_findings, implications, data_gaps)

### Step 2: Generate Options
- **Skill**: /strategize
- **Agent**: Strategist
- **Input**: Step 1 analysis
- **Output contract**: /strategize (options, recommended_option, execution_plan, risks)

### Step 3: Stress-Test
- **Skill**: /premortem
- **Agent**: Critic + Strategist
- **Input**: Step 2 recommended option
- **Output contract**: /premortem (failure_modes, top_3_risks, prevention_actions)

### Step 4: Decide
- **Skill**: /decide
- **Agent**: Strategist + Critic
- **Input**: Steps 1-3 combined
- **Output contract**: /decide (recommendation, trade_offs, reversibility, decision_record)

### Step 5: Record
- **Action**: Append to brain/context/decisions-log.md
- **Format**: Decision, options considered, rationale, date

## Error Handling
- Any step fails: Surface partial results with "Here's what I have so far -- [analysis/options/risks]. Want to continue?"

## Output
- Saved to: `output/analyses/{date}-decision-{topic}.md`
- Auto-logged to: brain/context/decisions-log.md (after user confirmation)
