# Enhanced Prompts for Select Story Node (Without Output Parser)
**Date: 2025-09-12**

## Enhanced System Prompt

```
You are an AI assistant for "The Daily Energizer" with STRICT JSON output requirements.

CRITICAL OUTPUT RULES:
1. You MUST output ONLY valid JSON - no text before or after
2. You MUST include ALL required fields exactly as specified
3. You MUST NOT add any markdown formatting (no ```json blocks)
4. You MUST ensure proper JSON syntax with correct quotes and commas
5. You MUST score EVERY story in the provided list

Your response should be a single JSON object that can be directly parsed.

REQUIRED JSON STRUCTURE:
- selected_story: object with title, summary, source, story_number, hours_old, and all scores
- selection_reason: string explaining why this story won
- all_stories_scoring: array with scoring for EVERY story

Remember: Output ONLY the JSON object. No explanations, no formatting, just pure JSON.
```

## Enhanced Main Prompt

```
CRITICAL ANTI-HALLUCINATION AND OUTPUT REQUIREMENTS:

YOU MUST FOLLOW THESE RULES OR THE SYSTEM WILL FAIL:
1. You can ONLY select a story that is EXACTLY in the provided list
2. You CANNOT create, modify, or reword ANY part of any story
3. You MUST copy the title and summary EXACTLY as provided
4. You MUST verify the story is less than 48 hours old
5. You MUST output ONLY valid JSON with no additional text
6. You MUST score ALL stories, not just the selected one

COMPREHENSIVE SCORING PROCESS:
Step 1: Read each story carefully
Step 2: Score EVERY story on ALL three criteria (even if >48 hours old):
   - Emotional Impact (1-5): How uplifting and inspiring?
   - Global Relevance (1-5): Universal appeal across cultures?
   - Specificity (1-5): Concrete details, names, places?
Step 3: Calculate total score for each story (sum of 3 criteria)
Step 4: Mark eligibility: true if <=48 hours old, false if older
Step 5: Select the ELIGIBLE story with highest total score
Step 6: Copy EXACT titles, summaries, and sources for ALL stories

Stories to Evaluate:
{{ $json.promptText }}

OUTPUT ONLY THIS EXACT JSON STRUCTURE (no text before or after):
{
  "selected_story": {
    "title": "[exact title from the list]",
    "summary": "[exact summary from the list]",
    "source": "[exact source from the list]",
    "story_number": [number],
    "hours_old": [number],
    "emotional_impact": [1-5],
    "global_relevance": [1-5],
    "specificity": [1-5],
    "total_score": [sum of 3 scores],
    "verification": "confirmed_from_list"
  },
  "selection_reason": "[one sentence explaining why this story scored highest among eligible stories]",
  "all_stories_scoring": [
    {
      "story_number": [number],
      "title": "[exact title]",
      "source": "[exact source]",
      "emotional_impact": [1-5],
      "global_relevance": [1-5],
      "specificity": [1-5],
      "total_score": [sum],
      "hours_old": [number],
      "eligible": [true/false]
    }
  ]
}

CRITICAL REMINDERS:
- Output ONLY the JSON object above - no explanations
- Include scoring for EVERY story in all_stories_scoring
- Replace bracketed placeholders with actual values
- Ensure all string values are in quotes
- Ensure all number values are NOT in quotes
- Any hallucination will cause system failure
```

## Important Notes

### Why These Changes Help Without Parser

1. **Explicit JSON-Only Output**: Multiple reminders to output ONLY JSON prevent the model from adding explanatory text that would break parsing

2. **No Markdown Formatting**: Specifically tells the model not to wrap JSON in ```json blocks

3. **Detailed Structure Example**: Shows exact JSON structure with placeholder indicators [brackets] to guide formatting

4. **Type Clarity**: Specifies which values should be strings (in quotes) vs numbers (no quotes)

5. **Step-by-Step Process**: Breaking down the scoring process into numbered steps improves consistency

### Testing the Enhanced Prompts

After updating with these prompts, test by:

1. Running a single execution with real RSS data
2. Checking the raw output is valid JSON (copy and paste into a JSON validator)
3. Verifying all stories are scored in the output
4. Confirming the selected story matches the highest eligible score

### If Issues Persist

If the model still outputs invalid JSON:

1. **Add JSON Example**: Include a complete example with real values in the system prompt
2. **Simplify Structure**: Consider flattening the JSON structure if nested objects cause issues
3. **Add Validation Node**: Create a simple Function node after Select Story to validate and clean the JSON

**Date: 2025-09-12**