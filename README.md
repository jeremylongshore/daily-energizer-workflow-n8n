# Daily Energizer Workflow

[![Release](https://img.shields.io/github/v/release/jeremylongshore/daily-energizer-workflow)](https://github.com/jeremylongshore/daily-energizer-workflow/releases)
[![N8N Workflow](https://img.shields.io/badge/N8N-Workflow-blue)](https://n8n.io)
[![Anti-Hallucination](https://img.shields.io/badge/Anti--Hallucination-4%20Layers-green)](https://github.com/jeremylongshore/daily-energizer-workflow)

N8N workflow automation for generating **daily inspirational articles** from positive news RSS feeds with comprehensive anti-hallucination measures, automated image generation, and advanced Google Sheets integration.

## 🎯 Overview

The Daily Energizer workflow fetches positive news from 10 curated RSS feeds, intelligently selects the most inspiring story using AI scoring, and generates uplifting articles with automated image creation. Features a robust 4-layer anti-hallucination system to ensure all content is real, traceable, and verified.

## 🚀 Quick Start

### Version 4 (Current - Recommended)
```bash
# Import V4 workflow (latest with enhanced features)
n8n import:workflow --input="The Daily Energizer Article and Image Generator V4.json"

# Execute workflow (requires workflow ID from N8N)
n8n execute --id=[workflow-id]
```

### Version 3 (Stable Fallback)
```bash
# Import V3 workflow (stable version)
n8n import:workflow --input="The Daily Energizer Article and Image Generator V3.json"
```

## ✨ Key Features

### V4 Enhanced Features
- **🔄 Story Deduplication**: Prevents repeated content with Remove Duplicates node
- **📝 Story-Centered Summaries**: Generates focused 200-word summaries
- **🖼️ Automated Image Generation**: Full image processing pipeline with Google Drive integration
- **📊 Advanced Google Sheets Integration**: Review status tracking and enhanced data management
- **✅ Content Validation**: Ensures proper article formatting and signature lines

### Core Features (All Versions)
- **📰 10 Positive News Sources**: Curated RSS feeds for uplifting content
- **⏰ 48-Hour Freshness**: Only processes recent stories
- **🛡️ Anti-Hallucination System**: 4 layers of protection against fabricated content
- **🎯 Temperature Zero**: Deterministic LLM output for consistency
- **✅ Story Verification**: Cross-references selected stories with original sources
- **📊 Comprehensive Scoring**: Transparent AI evaluation on 3 criteria
- **🔍 Source Tracking**: Full attribution from RSS feed to final article

## 📋 Workflow Versions

| Version | File Name | Features | Status |
|---------|-----------|----------|---------|
| **V4** | `The Daily Energizer Article and Image Generator V4.json` | Enhanced processing, image generation, advanced sheets integration | 🟢 **Current** |
| **V3** | `The Daily Energizer Article and Image Generator V3.json` | Core features, anti-hallucination, scoring system | 🟡 **Stable** |

## 📚 Documentation

### Core Documentation
- [`CLAUDE.md`](CLAUDE.md) - Comprehensive guidance for Claude Code development
- [`IMPLEMENTATION-GUIDE.md`](features/requirements/IMPLEMENTATION-GUIDE.md) - Complete technical documentation
- [`FEATURE-UPDATES-SUMMARY.md`](FEATURE-UPDATES-SUMMARY.md) - V4 feature overview
- [`MANUAL-UPDATE-GUIDE.md`](MANUAL-UPDATE-GUIDE.md) - Manual configuration procedures

### Feature Documentation
- [`features/requirements/BRENT-ACTION-PLAN.md`](features/requirements/BRENT-ACTION-PLAN.md) - Client requirements
- [`features/PRDs/`](features/PRDs/) - Product Requirement Documents
- [`features/ADRs/`](features/ADRs/) - Architecture Decision Records

## 🏗️ Architecture

### V4 Enhanced Data Flow
1. **RSS Collection** → 10 positive news feeds with source tracking
2. **Date Filtering** → 48-hour freshness enforcement
3. **Story Deduplication** → Prevent repeated content
4. **AI Story Selection** → Comprehensive scoring on 3 criteria
5. **Story Verification** → Cross-reference with source list
6. **Article Generation** → Full inspirational article creation
7. **Summary Generation** → Story-centered 200-word summaries
8. **Image Processing** → Automated image generation and URL conversion
9. **Google Sheets Integration** → Review status and data management

### Anti-Hallucination System
- **Layer 1**: 48-hour date filtering
- **Layer 2**: Story verification against source list
- **Layer 3**: Strengthened anti-hallucination prompts
- **Layer 4**: Temperature zero for deterministic output

## 🛠️ Development

```bash
# Check workflow status
make status

# Validate JSON structure
jq . "The Daily Energizer Article and Image Generator V4.json" > /dev/null && echo "Valid JSON"

# Create backup before changes
cp "The Daily Energizer Article and Image Generator V4.json" "backup-$(date +%Y%m%d).json"
```

## 📊 RSS Feed Sources

1. Good News Network
2. Positive News UK
3. Sunny Skyz
4. The Optimist Daily
5. Good Good Good
6. Nice News
7. Epoch Times Bright
8. Reasons to Be Cheerful
9. YES! Magazine
10. Not All News is Bad!

## 🎯 Scoring Criteria

All stories are evaluated on:
- **Emotional Impact** (1-5): Uplifting and inspiring qualities
- **Global Relevance** (1-5): Universal appeal across cultures
- **Specificity** (1-5): Concrete details, names, and places
- **Total Score**: Sum of all criteria (3-15 range)

## 🚀 Deployment

### Requirements
- N8N platform (Cloud or self-hosted)
- OpenAI API access (GPT-4o-mini)
- Google Sheets API credentials
- Google Drive API access (for image processing)

### Configuration
1. Import workflow JSON file into N8N
2. Configure API credentials
3. Set up Google Sheets integration
4. Test with manual execution
5. Schedule for daily automation

## 📈 Performance Metrics

- **Processing Time**: < 5 minutes per execution
- **Story Success Rate**: 95%+ verified content
- **Image Generation**: Automated with direct URL conversion
- **Anti-Hallucination**: 4-layer protection system
- **Content Quality**: Consistent scoring and verification

## 🔗 Links

- [N8N Platform](https://n8n.io)
- [Technical Documentation](CLAUDE.md)
- [Feature Updates](FEATURE-UPDATES-SUMMARY.md)
- [Implementation Guide](features/requirements/IMPLEMENTATION-GUIDE.md)

---

**Built with ❤️ for positive news automation**
*Last Updated: September 19, 2025*