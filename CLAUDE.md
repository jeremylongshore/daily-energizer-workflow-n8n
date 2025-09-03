# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

N8N workflow automation for generating **daily inspirational articles** from positive news RSS feeds. Features sophisticated anti-hallucination measures and strict content verification.

## Workflow Architecture

### Main Workflow File
- `daily-energizer-workflow.json` (62KB, 2,119 lines)
- N8N automation platform workflow
- Generates one uplifting article daily from RSS feeds

### RSS Feed Sources (10 feeds)
```
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
```

## Anti-Hallucination System

The workflow implements **4 layers** of protection against AI hallucination:

### 1. Date Filtering (fix-1-date-filtering)
- 48-hour freshness requirement on RSS stories
- Prevents using outdated content
- Date comparison nodes validate timestamps

### 2. Verification Node (fix-2-verification-node)
- Cross-references selected stories with original RSS sources
- Ensures story actually exists in feed
- Blocks fabricated content

### 3. Strengthened Prompts (fix-3-stronger-prompts)
- Explicit instructions: "DO NOT invent details"
- "Use ONLY information from the RSS feed"
- Multiple reinforcement points in prompts

### 4. Temperature Zero (fix-4-temperature-zero)
- LLM temperature set to 0 for deterministic output
- Eliminates randomness in content generation
- Ensures consistent, factual responses

## Version Control Structure

```
main                    # Production workflow
├── fix-1-date-filtering
├── fix-2-verification-node  
├── fix-3-stronger-prompts
├── fix-4-temperature-zero
└── fix-5-all-combined  # All fixes integrated
```

## Key Configurations

### LLM Settings
- **Model**: GPT-4o-mini (via OpenRouter)
- **Temperature**: 0 (deterministic)
- **Max Tokens**: 2000 for article, 200 for title

### Story Selection Criteria
1. Emotional impact score (1-10)
2. Global relevance (1-10)  
3. Specificity of details (1-10)
4. Recency (within 48 hours)

### Output Format
```json
{
  "title": "Article title",
  "content": "Full article text",
  "source_verification": {
    "story_exists": true,
    "date_valid": true,
    "source_feed": "Feed name"
  }
}
```

## Common Commands

### Deploy Workflow
```bash
# Import workflow to N8N
n8n import:workflow --input=daily-energizer-workflow.json

# Test workflow execution
n8n execute --id=[workflow-id]
```

### Version Management
```bash
# Switch to specific fix branch
git checkout fix-5-all-combined

# Compare versions
git diff main fix-5-all-combined
```

## Development Guidelines

### When Modifying Workflow
1. Export current version first
2. Test each node individually  
3. Verify anti-hallucination measures remain intact
4. Check RSS feed connectivity
5. Validate output format

### Critical Rules
- **NEVER** increase temperature above 0
- **NEVER** remove verification nodes
- **ALWAYS** maintain 48-hour date filter
- **ALWAYS** test with real RSS data

## Integration Points

- **RSS Feeds Project**: Uses curated feeds from `../rss_feeds/`
- **Output**: Can feed into content management systems
- **Monitoring**: Check N8N execution logs daily

## Performance Targets

- Workflow execution: < 60 seconds
- RSS fetch: < 5 seconds per feed
- LLM generation: < 20 seconds
- Total daily runtime: < 2 minutes