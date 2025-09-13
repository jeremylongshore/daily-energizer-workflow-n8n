# Structured Output Parser Setup Guide for Daily Energizer
**Date: 2025-09-12**

## When to Use the Structured Output Parser

Use this guide if:
- You're on N8N version 1.60.0 or higher (self-hosted)
- You want strict JSON validation and type checking
- You prefer schema-based output validation

**Note**: N8N Cloud 1.110.1 has issues with complex nested JSON. If you encounter "Model output doesn't fit required format" errors, use the direct JSON output method instead (remove parser).

---

## Step 1: Configure Structured Output Parser Node

### Location
The Structured Output Parser should be connected between:
- **Input**: Select Story node
- **Output**: Downstream nodes that use the story data

### JSON Schema Configuration

1. Open the **Structured Output Parser** node
2. In the **"JSON Schema Example"** field, paste this complete example:

```json
{
  "selected_story": {
    "title": "Community Rallies to Save Local Wildlife Sanctuary",
    "summary": "Residents raised $500,000 in 48 hours to prevent development of critical habitat",
    "source": "Good News Network",
    "story_number": 1,
    "hours_old": 24,
    "emotional_impact": 5,
    "global_relevance": 4,
    "specificity": 5,
    "total_score": 14,
    "verification": "confirmed_from_list"
  },
  "selection_reason": "This story scored highest due to exceptional emotional impact and specific details about community action",
  "all_stories_scoring": [
    {
      "story_number": 1,
      "title": "Community Rallies to Save Local Wildlife Sanctuary",
      "source": "Good News Network",
      "emotional_impact": 5,
      "global_relevance": 4,
      "specificity": 5,
      "total_score": 14,
      "hours_old": 24,
      "eligible": true
    },
    {
      "story_number": 2,
      "title": "Scientists Develop Breakthrough in Clean Energy",
      "source": "Positive News UK",
      "emotional_impact": 3,
      "global_relevance": 5,
      "specificity": 4,
      "total_score": 12,
      "hours_old": 36,
      "eligible": true
    },
    {
      "story_number": 3,
      "title": "Young Inventor Creates Solution for Ocean Cleanup",
      "source": "The Optimist Daily",
      "emotional_impact": 4,
      "global_relevance": 5,
      "specificity": 3,
      "total_score": 12,
      "hours_old": 72,
      "eligible": false
    }
  ]
}
```

3. **Important Settings**:
   - Mode: **"From JSON Example"** (not "Manual")
   - Ensure "Required" toggle is ON for critical fields

---

## Step 2: Update Select Story Node Prompts

### System Message
```
You are an AI assistant for "The Daily Energizer" that evaluates news stories.

OUTPUT REQUIREMENTS:
- Generate valid JSON matching the exact schema structure
- Include scoring for ALL stories in the provided list
- Use only information from the provided stories
- Never hallucinate or create content

Your response must be parseable JSON that validates against the schema.
```

### Main Prompt
```
Evaluate ALL stories from the list below using these criteria:

SCORING CRITERIA (1-5 scale each):
1. Emotional Impact: How uplifting and inspiring is the story?
2. Global Relevance: Does it have universal appeal across cultures?
3. Specificity: Does it contain concrete details, names, and places?

SELECTION PROCESS:
1. Score every story on all three criteria
2. Calculate total score (sum of three criteria)
3. Mark eligibility (true if ≤48 hours old, false if older)
4. Select the eligible story with the highest total score
5. Provide a clear reason for your selection

Stories to evaluate:
{{ $json.promptText }}

Generate a JSON response with:
- selected_story: The chosen story with all details and scores
- selection_reason: One sentence explaining why this story won
- all_stories_scoring: Array containing scores for EVERY story

CRITICAL RULES:
- Copy titles, summaries, and sources EXACTLY as provided
- Include story_number based on order in the list
- Set verification to "confirmed_from_list"
- Score ALL stories, even those over 48 hours old
- Mark eligible as false for stories over 48 hours
```

---

## Step 3: Configure Parser Output Handling

### Parser Settings
1. **Input Source**: Set to receive from Select Story node
2. **Output Mode**: "Single Item" (not "All Items")
3. **Error Handling**:
   - On error: "Continue (using error output)"
   - This allows graceful failure handling

### Validation Rules
The parser will enforce:
- Required fields are present
- Data types match (strings, numbers, booleans)
- Array structures are valid
- Nested objects follow schema

---

## Step 4: Update Downstream Nodes

### Write Article Node
Update references to use parser output structure:
```
Title: {{ $('Structured Output Parser').item.json.selected_story.title }}
Summary: {{ $('Structured Output Parser').item.json.selected_story.summary }}
Source: {{ $('Structured Output Parser').item.json.selected_story.source }}
Hours Old: {{ $('Structured Output Parser').item.json.selected_story.hours_old }}
Scores: E:{{ $('Structured Output Parser').item.json.selected_story.emotional_impact }}, G:{{ $('Structured Output Parser').item.json.selected_story.global_relevance }}, S:{{ $('Structured Output Parser').item.json.selected_story.specificity }}
Total: {{ $('Structured Output Parser').item.json.selected_story.total_score }}/15
Reason: {{ $('Structured Output Parser').item.json.selection_reason }}
```

### Google Sheets Node
Update column mappings to reference parser output:
```
Source: {{ $('Structured Output Parser').item.json.selected_story.source }}
Emotional Impact: {{ $('Structured Output Parser').item.json.selected_story.emotional_impact }}
Global Relevance: {{ $('Structured Output Parser').item.json.selected_story.global_relevance }}
Specificity: {{ $('Structured Output Parser').item.json.selected_story.specificity }}
Total Score: {{ $('Structured Output Parser').item.json.selected_story.total_score }}
Selection Reason: {{ $('Structured Output Parser').item.json.selection_reason }}
All Stories Count: {{ $('Structured Output Parser').item.json.all_stories_scoring.length }}
All Stories JSON: {{ JSON.stringify($('Structured Output Parser').item.json.all_stories_scoring) }}
```

---

## Troubleshooting Parser Issues

### "Model output doesn't fit required format"
**Causes & Solutions:**

1. **LLM adding extra text**
   - Add to prompt: "Output ONLY valid JSON with no additional text"
   - Set temperature to 0 for consistency

2. **Schema mismatch**
   - Verify JSON example includes all required fields
   - Check data types match (numbers vs strings)

3. **Version incompatibility**
   - N8N Cloud 1.110.1 struggles with nested arrays
   - Consider self-hosted N8N for complex schemas

4. **Prompt conflicts**
   - Check System Message doesn't contradict Main Prompt
   - Remove any legacy output format instructions

### Testing the Parser

1. **Isolated Test**:
   - Run just the Select Story node
   - Check raw output before parser
   - Verify JSON structure matches schema

2. **Validation Test**:
   ```bash
   # Copy LLM output and validate locally
   echo '[OUTPUT]' | jq '.'
   ```

3. **Schema Verification**:
   - Ensure example JSON is valid
   - All fields in example should be expected in output

---

## Alternative: Direct JSON Output (No Parser)

If parser issues persist, remove it and use enhanced prompts:

**Benefits of No Parser**:
- Simpler workflow
- No schema validation overhead
- Works on all N8N versions
- Faster execution

**Benefits of Using Parser**:
- Guaranteed structure compliance
- Type safety
- Automatic error handling
- Clear schema documentation

Choose based on your needs and N8N version compatibility.

---

**Implementation Support**: If you encounter parser errors after following this guide, the enhanced prompts without parser (Option 1) are recommended for N8N Cloud users.

**Date: 2025-09-12**