# Daily Energizer Workflow

N8N workflow automation for generating daily inspirational articles from positive news RSS feeds with comprehensive anti-hallucination measures.

## Overview

The Daily Energizer workflow fetches positive news from 10 RSS feeds, selects the most inspiring story, and generates an uplifting article. It includes a 4-layer anti-hallucination system to ensure all content is real and traceable.

## Quick Start

```bash
# Import workflow into N8N
n8n import:workflow --input=daily-energizer-workflow.json

# Execute workflow (requires workflow ID from N8N)
n8n execute --id=[workflow-id]
```

## Key Features

- **10 Positive News Sources**: Curated RSS feeds for uplifting content
- **48-Hour Freshness**: Only processes recent stories
- **Anti-Hallucination System**: 4 layers of protection against fabricated content
- **Temperature Zero**: Deterministic LLM output
- **Story Verification**: Cross-references selected stories with source

## Documentation

- `CLAUDE.md` - Guidance for Claude Code when working with this repository
- `IMPLEMENTATION-GUIDE.md` - Complete technical documentation and implementation history
- `BRENT-ACTION-PLAN.md` - Current client requirements for source tracking and scoring visibility

## Workflow File

- `daily-energizer-workflow.json` - The complete N8N workflow (70 nodes, 78KB)
  - Import directly into N8N platform
  - Contains all anti-hallucination measures
  - Fully implemented and tested