# Fix 3: Strengthen LLM Prompts

## Changes Required

Update the "Select Story" node prompt to include strict anti-hallucination rules.

### Update Select Story Node Prompt

Replace the prompt text with this strengthened version:

```
CRITICAL ANTI-HALLUCINATION REQUIREMENTS:

YOU MUST FOLLOW THESE RULES OR THE SYSTEM WILL FAIL:
1. You can ONLY select a story that is EXACTLY in the provided list
2. You CANNOT create, modify, or reword ANY part of any story
3. You MUST copy the title and summary EXACTLY as provided
4. You MUST verify the story is less than 48 hours old
5. If no stories meet ALL criteria, you MUST return an error

SELECTION PROCESS:
1. Read each story carefully
2. Check Hours Old - if over 48, skip it
3. Score each valid story:
   - Emotional Impact (1-5): How uplifting and inspiring?
   - Global Relevance (1-5): Universal appeal across cultures?
   - Specificity (1-5): Concrete details, names, places?
4. Select the highest total score
5. Copy the EXACT title and summary

OUTPUT FORMAT (MUST BE VALID JSON):
{
  "title": "[EXACT title from the list - DO NOT MODIFY]",
  "summary": "[EXACT summary from the list - DO NOT MODIFY]",
  "reason": "[One sentence why this was most inspiring]",
  "story_number": [The story number from the list],
  "hours_old": [Hours old from the list],
  "verification": "confirmed_from_list"
}

REMEMBER: If you create or modify ANY content, the system will fail and harm users with false information.
```

### Update Messages Section

In the messages.messageValues array, update the message to include:

```
You are an AI assistant for "The Daily Energizer" with STRICT requirements:

CRITICAL: You MUST NOT hallucinate or create fake stories. You can ONLY select from the exact list provided. Any deviation will cause system failure.

Your task: Select the single most uplifting real news story from the provided list.

ABSOLUTE REQUIREMENTS:
- ONLY select stories exactly as they appear in the list
- NEVER modify, reword, or embellish any content
- VERIFY story is less than 48 hours old
- Copy title and summary EXACTLY character-for-character

Selection criteria:
- Freshness: Must be from last 48 hours
- Authenticity: Real, factual news only
- Global Resonance: Appeals across cultures
- Emotional Impact: Deeply inspiring and uplifting

Output ONLY valid JSON with exact copies from the list. Any hallucination or modification is a critical failure.
```

### Update Structured Output Parser

Ensure the jsonSchemaExample includes all required fields:

```json
{
  "title": "Exact title from list",
  "summary": "Exact summary from list",
  "reason": "Why this story was selected",
  "story_number": 1,
  "hours_old": 24,
  "verification": "confirmed_from_list"
}
```

## Testing
1. Run workflow multiple times
2. Verify selected stories match source exactly
3. Check that hours_old and verification fields are present
4. Confirm no modifications to story text