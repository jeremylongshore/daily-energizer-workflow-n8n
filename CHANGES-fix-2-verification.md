# Fix 2: Story Verification Node

## Changes Required

Add a verification node after "Select Story" to validate the selection is real.

### New Node: Verify Story Selection

**Type:** n8n-nodes-base.code  
**Name:** "Verify Story Selection"  
**Position:** Between "Select Story" and "Set Today's Date"

### Node Code
```javascript
// Verify the selected story is real and from the list
const selection = $input.first().json.output;
const originalStories = $node["Combine Stories"].json.stories;

if (!selection || !selection.title || !selection.summary) {
  throw new Error("Invalid selection format - missing required fields");
}

if (selection.hours_old > 48) {
  throw new Error(`Selected story is ${selection.hours_old} hours old - exceeds 48 hour limit`);
}

// Find exact match in original list
const matchFound = originalStories.some(story => 
  story.title === selection.title && 
  story.summary === selection.summary
);

if (!matchFound) {
  throw new Error("HALLUCINATION DETECTED: Selected story not found in original list!");
}

if (selection.verification !== "confirmed_from_list") {
  throw new Error("Selection verification flag not set - potential hallucination");
}

console.log(`✓ Verified: Story is real and from list`);
console.log(`✓ Age: ${selection.hours_old} hours old`);
console.log(`✓ Title matches exactly`);
console.log(`✓ Summary matches exactly`);

return [{
  json: {
    ...selection,
    verified: true,
    verification_timestamp: new Date().toISOString()
  }
}];
```

### Connection Updates
1. Disconnect "Select Story" from "Set Today's Date"
2. Connect "Select Story" → "Verify Story Selection" → "Set Today's Date"

### Update Select Story Output
Modify the "Select Story" prompt to include verification field in output:

Add to the output format section:
```json
{
  "title": "[EXACT title from the list]",
  "summary": "[EXACT summary from the list]",
  "reason": "[One sentence why this was most inspiring]",
  "story_number": [The story number from the list],
  "hours_old": [Hours old from the list],
  "verification": "confirmed_from_list"
}
```

### Update Write Article Node
Add context about verification:

```
IMPORTANT: You are writing about a REAL news story that happened ${hours_old} hours ago.
Do NOT embellish or add details not in the provided summary.
Use ONLY the information provided in the story summary.

Selected Story (VERIFIED REAL):
Title: {{ $('Verify Story Selection').item.json.title }}
Summary: {{ $('Verify Story Selection').item.json.summary }}
Published: ${hours_old} hours ago
```

## Testing
1. Run workflow and check console for verification messages
2. Try modifying a story title manually to test error detection
3. Verify error is thrown if story doesn't match original list