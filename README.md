# Daily Energizer Workflow

N8N workflow for generating daily inspirational articles from positive news sources.

## Version History

### Main Branch
- Original workflow v2 (baseline)

### Feature Branches

#### fix-1-date-filtering
- Adds date filtering nodes to enforce 48-hour limit on RSS feed stories
- Filters out old stories before selection

#### fix-2-verification-node  
- Adds verification node after story selection
- Validates selected story exists in original list
- Prevents hallucinations

#### fix-3-llm-prompts
- Strengthens LLM prompts with anti-hallucination rules
- Updates prompt structure for better compliance

#### fix-4-temperature-zero
- Sets all LLM temperature settings to 0
- Ensures deterministic output

#### fix-5-all-combined
- Combines all fixes into one branch
- Full implementation of all anti-hallucination measures

## Testing Instructions

1. Checkout the branch you want to test
2. Import the workflow JSON into n8n
3. Run the workflow and verify:
   - Stories are < 48 hours old
   - Selected story matches source
   - No hallucinated content

## Files

- `daily-energizer-workflow.json` - The n8n workflow file
- Branch-specific versions with incremental fixes