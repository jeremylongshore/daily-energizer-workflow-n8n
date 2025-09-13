# 🔧 Structured Output Parser Configuration Guide
**Date: 2025-09-12**

## Quick Decision Guide

### Use Output Parser If:
- ✅ Self-hosted N8N (version 1.60.0+)
- ✅ Want strict JSON validation
- ✅ Need guaranteed structure compliance
- ✅ Prefer schema-based validation

### Skip Parser If:
- ❌ Using N8N Cloud 1.110.1
- ❌ Getting "format doesn't match" errors
- ❌ Need simpler workflow
- ❌ Want faster execution

## Parser Configuration Steps

### Step 1: JSON Schema Setup

Open **Structured Output Parser** node and paste this in **JSON Schema Example**:

```json
{
  "selected_story": {
    "title": "Teen Invents Device to Clean Ocean Plastic",
    "summary": "A 16-year-old created a solar-powered device that collected 50 tons of ocean plastic in its first month",
    "source": "Good News Network",
    "story_number": 1,
    "hours_old": 18,
    "emotional_impact": 5,
    "global_relevance": 5,
    "specificity": 5,
    "total_score": 15,
    "verification": "confirmed_from_list"
  },
  "selection_reason": "Perfect score across all criteria with global environmental impact and specific measurable results",
  "all_stories_scoring": [
    {
      "story_number": 1,
      "title": "Teen Invents Device to Clean Ocean Plastic",
      "source": "Good News Network",
      "emotional_impact": 5,
      "global_relevance": 5,
      "specificity": 5,
      "total_score": 15,
      "hours_old": 18,
      "eligible": true
    },
    {
      "story_number": 2,
      "title": "Community Garden Feeds 100 Families",
      "source": "Positive News UK",
      "emotional_impact": 4,
      "global_relevance": 3,
      "specificity": 5,
      "total_score": 12,
      "hours_old": 36,
      "eligible": true
    }
  ]
}
```

**Settings:**
- Mode: **"From JSON Example"**
- Required Fields: **ON**

### Step 2: Select Story Node Prompts

**System Message:**
```
You are The Daily Energizer AI that evaluates news stories.

OUTPUT: Valid JSON matching the provided schema exactly.
Include ALL stories with complete scoring.
Never add text outside the JSON structure.
```

**Main Prompt:**
```
Score ALL stories below on three criteria (1-5 each):
- Emotional Impact: How uplifting/inspiring?
- Global Relevance: Universal appeal?
- Specificity: Concrete details/names?

Stories to evaluate:
{{ $json.promptText }}

Return JSON with:
1. selected_story: Highest-scoring eligible story (≤48 hours)
2. selection_reason: One sentence why it won
3. all_stories_scoring: Array with EVERY story's scores

Copy titles/summaries EXACTLY. Include story_number, hours_old, source.
Set verification: "confirmed_from_list"
```

### Step 3: Connect Parser

**Node Connections:**
```
Format Stories → Select Story → Structured Output Parser → Write Article
                                                        ↓
                                                   Google Sheets
```

**Parser Input Settings:**
- Input from: **Select Story**
- Mode: **Single Item**
- On Error: **Continue (error output)**

## Downstream Node Updates

### Write Article References
```
Title: {{ $('Structured Output Parser').item.json.selected_story.title }}
Summary: {{ $('Structured Output Parser').item.json.selected_story.summary }}
Source: {{ $('Structured Output Parser').item.json.selected_story.source }}
Scores: {{ $('Structured Output Parser').item.json.selected_story.total_score }}/15
Reason: {{ $('Structured Output Parser').item.json.selection_reason }}
```

### Google Sheets Mappings
```
Source: {{ $('Structured Output Parser').item.json.selected_story.source }}
Emotional: {{ $('Structured Output Parser').item.json.selected_story.emotional_impact }}
Global: {{ $('Structured Output Parser').item.json.selected_story.global_relevance }}
Specificity: {{ $('Structured Output Parser').item.json.selected_story.specificity }}
Total: {{ $('Structured Output Parser').item.json.selected_story.total_score }}
Reason: {{ $('Structured Output Parser').item.json.selection_reason }}
All Stories: {{ JSON.stringify($('Structured Output Parser').item.json.all_stories_scoring) }}
```

## Troubleshooting

### "Model output doesn't fit required format"

**Quick Fixes:**
1. Check System Message - Remove any conflicting instructions
2. Clear Messages section - Delete old format requirements
3. Set Temperature to 0 - Ensures consistency
4. Simplify prompt - Remove verbose instructions

**If Issues Persist:**
Remove parser and use direct JSON output (works on all versions)

### Schema Validation Tips

**Good Schema Practices:**
- Use realistic example values
- Include all possible fields
- Keep nesting to 2 levels max
- Use consistent data types

**Common Mistakes:**
- Missing required fields in example
- Type mismatches (string vs number)
- Too much nesting (>3 levels)
- Conflicting prompt instructions

## Alternative: Direct JSON (No Parser)

If parser fails, remove it and enhance prompts:

**Enhanced System Message:**
```
Output ONLY valid JSON - no text before/after.
No markdown formatting (no ```json blocks).
Must parse directly as JSON.
```

**Benefits:**
- Works on ALL N8N versions
- No schema overhead
- Simpler troubleshooting
- Faster execution

## Testing Checklist

### With Parser:
- [ ] Parser accepts LLM output
- [ ] All fields populated correctly
- [ ] Downstream nodes receive data
- [ ] No format errors in logs

### Without Parser:
- [ ] LLM outputs clean JSON
- [ ] JSON.parse() succeeds
- [ ] All data fields present
- [ ] Google Sheets captures data

## Performance Comparison

| Aspect | With Parser | Without Parser |
|--------|------------|----------------|
| Validation | Strict | None |
| Speed | +2-3 sec | Baseline |
| Reliability | High (if compatible) | Depends on prompt |
| Debugging | Clear errors | Manual checking |
| Version Needs | 1.60.0+ self-hosted | Any version |

## Final Recommendation

**For N8N Cloud Users:**
Skip the parser. Use enhanced prompts for direct JSON output.

**For Self-Hosted Users:**
Try parser first. Fall back to direct JSON if issues occur.

**For Production:**
Test thoroughly with your specific N8N version before committing.

---
*Configuration Guide by Jeremy Longshore*