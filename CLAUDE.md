# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

N8N workflow automation for generating **daily inspirational articles** from positive news RSS feeds with comprehensive anti-hallucination measures. This is a client project for repair and enhancement.

## Workflow Architecture

### Core Workflow File
- **`daily-energizer-workflow.json`** - 78KB N8N workflow definition (70 nodes total)
  - Direct import into N8N platform for execution
  - Contains complete anti-hallucination system implementation

### Data Flow
1. **RSS Feed Collection** → 10 positive news sources fetch stories
2. **Date Filtering** → Removes stories older than 48 hours
3. **Story Selection** → LLM selects most inspiring story (temperature 0)
4. **Verification** → Validates selected story exists in source
5. **Article Generation** → Creates article from verified story only

## N8N Commands

```bash
# Import workflow into N8N instance
n8n import:workflow --input=daily-energizer-workflow.json

# Execute workflow (requires workflow ID from N8N)
n8n execute --id=[workflow-id]

# Export updated workflow
n8n export:workflow --id=[workflow-id] --output=daily-energizer-workflow.json
```

## Critical Anti-Hallucination System

### 4-Layer Protection (ALL REQUIRED)

1. **Date Filtering** - 10 Filter nodes enforce 48-hour freshness
   - Formula: `Math.floor((Date.now() - new Date($json.pubDate).getTime()) / (1000 * 60 * 60))`
   
2. **Verification Node** - Cross-references selected story with source list
   - Returns: 'passed', 'partial', or 'failed'
   - Workflow halts on failure
   
3. **LLM Prompt Hardening** - Explicit anti-hallucination instructions
   - 6-field JSON output requirement
   - Must include `verification: "confirmed_from_list"`
   
4. **Temperature Zero** - All 3 GPT-4o-mini nodes at deterministic setting

### Critical Development Rules
- **NEVER** increase temperature above 0 in any LLM node
- **NEVER** remove or bypass verification nodes  
- **ALWAYS** maintain the 48-hour date filter on all RSS feeds
- **ALWAYS** preserve the 6-field JSON output format

## Known Issues & Solutions

### Format Stories Node Variable Syntax
**Problem**: Node may use incorrect `items[0].json.stories` syntax
**Solution**: Must use N8N helper: `$input.first().json.stories`

```javascript
// CORRECT N8N syntax
const stories = $input.first().json.stories;
```

### Common Errors

| Issue | Solution |
|-------|----------|
| "Referenced node doesn't exist" | Verify node connections and N8N variable syntax |
| JSON parsing errors | Check Structured Output Parser has 6-field schema |
| Old stories appearing | Confirm all 10 RSS feeds have date filter nodes |
| Hallucinated content | Verify all 3 LLM nodes have temperature = 0 |

## RSS Feed Sources

10 positive news feeds:
- Positive News UK
- Good News Network  
- Sunny Skyz
- The Optimist Daily
- Good Good Good
- Nice News
- Epoch Times Bright
- Reasons to Be Cheerful
- YES! Magazine
- Not All News is Bad!

## Testing Requirements

Before deployment verify:
- [ ] All RSS feeds return data successfully
- [ ] Date filters remove stories > 48 hours old
- [ ] Story selection outputs valid 6-field JSON
- [ ] Selected story exists in original feed list
- [ ] Article uses only provided information
- [ ] All 3 LLM nodes show temperature: 0

## Expected Output Format

```json
{
  "title": "exact title from RSS feed",
  "summary": "exact summary from RSS feed",
  "reason": "one sentence explaining selection",
  "story_number": 1,
  "hours_old": 24,
  "verification": "confirmed_from_list"
}
```

## Development Commands

### Workflow Management
```bash
# Import workflow into N8N instance
n8n import:workflow --input=daily-energizer-workflow.json

# Execute workflow with specific ID
n8n execute --id=[workflow-id]

# Export updated workflow
n8n export:workflow --id=[workflow-id] --output=daily-energizer-workflow.json

# Validate workflow JSON structure
jq . daily-energizer-workflow.json > /dev/null && echo "Valid JSON"
```

### Git Operations for This Project
```bash
# Common workflow development cycle
git status
git add daily-energizer-workflow.json
git commit -m "Update workflow: [description]"

# Create feature branch for workflow changes
git checkout -b fix-[issue-number]-[description]
```

## Project Structure

```
daily-energizer-workflow/
├── daily-energizer-workflow.json    # Main N8N workflow (70 nodes, 78KB)
├── CLAUDE.md                        # This guidance file
├── README.md                        # Project overview
├── IMPLEMENTATION-GUIDE.md          # Complete technical documentation
├── BRENT-ACTION-PLAN.md            # Client requirements for improvements
└── docs/                           # Documentation templates
    ├── ADRs/                       # Architecture Decision Records
    └── PRDs/                       # Product Requirements Documents
```

## Critical Workflow Architecture

### Node Dependencies & Flow
The 70-node workflow follows this critical path:
1. **RSS Collection Layer** (30 nodes): 10 feeds → Set Fields → Date Filters
2. **Data Processing Layer** (5 nodes): Combine → Format → Select Story
3. **Verification Layer** (3 nodes): Verify Selection → Validation
4. **Content Generation Layer** (3 nodes): Write Article → Generate Image
5. **Output Layer**: Final formatting and delivery

### Anti-Hallucination System Dependencies
All 4 layers are interdependent - removing any layer compromises the entire system:
- **Date Filtering** prevents old content hallucination
- **Verification Node** catches fabricated story selection  
- **Prompt Hardening** enforces strict content rules
- **Temperature Zero** ensures deterministic output

## Critical Implementation Rules

### Node Variable Syntax (N8N Specific)
```javascript
// CORRECT - Always use N8N helpers
const stories = $input.first().json.stories;
const allItems = $input.all();
const currentData = $json;

// INCORRECT - Will cause undefined variable errors
const stories = items[0].json.stories;
const data = items.json;
```

### LLM Configuration Requirements
**All GPT nodes MUST maintain:**
- Model: `gpt-4o-mini`
- Temperature: `0` (never increase)
- Max tokens: Appropriate for response size
- JSON mode: Enabled for structured output

### RSS Feed Data Preservation
Each story object must maintain these fields throughout the workflow:
```json
{
  "title": "original from RSS",
  "summary": "original from RSS", 
  "pubDate": "ISO date string",
  "hours_old": "calculated number",
  "source": "feed name (for traceability)"
}
```

## Common Issues & Solutions

### 1. "Referenced node doesn't exist" Error
**Cause**: N8N node connections broken or incorrect variable syntax
**Solution**: Check node connections in N8N UI and verify `$input.first()` syntax

### 2. JSON Parsing Failures  
**Cause**: Structured Output Parser schema mismatch
**Solution**: Verify 6-field JSON schema matches expected output format

### 3. Old Stories in Output
**Cause**: Date filter nodes disabled or formula incorrect
**Solution**: Confirm all 10 date filter nodes active with `hours_old <= 48`

### 4. Hallucinated Content
**Cause**: Temperature > 0 or bypassed verification
**Solution**: Verify all LLM nodes at temperature 0 and verification node connected

### 5. Format Stories Node Failure
**Cause**: Using `items[0]` instead of N8N syntax
**Solution**: Use `$input.first().json.stories` in all Code nodes

## Testing & Validation Workflow

Before any deployment or major changes:

```bash
# 1. Validate workflow JSON structure
jq . daily-energizer-workflow.json

# 2. Check node count (should be 70)
jq '.nodes | length' daily-energizer-workflow.json

# 3. Verify all LLM nodes have temperature 0
jq '.nodes[] | select(.type == "n8n-nodes-base.openai") | .parameters.temperature' daily-energizer-workflow.json
```

## Documentation References

- **Complete Implementation**: See `IMPLEMENTATION-GUIDE.md` for full technical details
- **Client Requirements**: See `BRENT-ACTION-PLAN.md` for current enhancement requests  
- **Architecture Decisions**: See `docs/ADRs/` for design rationale
- **Change History**: Git log shows all anti-hallucination fixes applied