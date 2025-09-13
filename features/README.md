# Features Directory

This directory contains all feature development documentation for the Daily Energizer workflow enhancements.

## Directory Structure

```
features/
├── README.md                    # This file
├── requirements/               # Original client requirements and implementation guides
│   ├── BRENT-ACTION-PLAN.md   # Client feature requests for source tracking and scoring
│   └── IMPLEMENTATION-GUIDE.md # Complete implementation history and technical details
├── PRDs/                      # Product Requirements Documents
│   ├── source-tracking-prd.md # PRD for RSS feed source tracking feature
│   └── scoring-visibility-prd.md # PRD for story selection scoring visibility
├── ADRs/                      # Architecture Decision Records
│   ├── adr-001-rss-source-tracking.md # Technical decision for source tracking implementation
│   └── adr-002-scoring-visibility.md  # Technical decision for scoring visibility implementation
└── tasks/                     # Implementation task lists
    ├── tasks-source-tracking-prd.md   # Detailed tasks for source tracking feature
    └── tasks-scoring-visibility-prd.md # Detailed tasks for scoring visibility feature
```

## Feature Overview

### 1. RSS Feed Source Tracking
**Status**: Ready for implementation
**Goal**: Track which RSS feed each selected story originated from to enable quality control and prevent hallucinations.

**Key Documents**:
- PRD: `PRDs/source-tracking-prd.md`
- ADR: `ADRs/adr-001-rss-source-tracking.md`
- Tasks: `tasks/tasks-source-tracking-prd.md`

### 2. Story Selection Scoring Visibility
**Status**: Ready for implementation
**Goal**: Expose detailed scoring breakdown for all stories to understand LLM selection decisions and optimize prompts.

**Key Documents**:
- PRD: `PRDs/scoring-visibility-prd.md`
- ADR: `ADRs/adr-002-scoring-visibility.md`
- Tasks: `tasks/tasks-scoring-visibility-prd.md`

## Implementation Priority

1. **Source Tracking** - Higher priority as it provides essential quality control and audit capabilities
2. **Scoring Visibility** - Can be implemented after source tracking to provide optimization insights

Both features can be implemented independently but work well together for comprehensive workflow transparency.

## Related Files

- Main workflow file: `../daily-energizer-workflow.json`
- Workflow documentation: `../CLAUDE.md`
- Project README: `../README.md`