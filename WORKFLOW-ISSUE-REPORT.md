# Workflow Issue Report: Undefined promptText Variable
**Date: 2025-09-08**
**Issue: Select Story LLM node hallucinating due to undefined variable**

## Executive Summary

The customer is correct. The Select Story LLM node is referencing `{{ $json.promptText }}` in its prompt, but this variable is not directly available in the current node's context. This causes the LLM to receive no actual stories, forcing it to hallucinate content.

## Root Cause Analysis

### The Data Flow Problem

1. **Format Stories for Prompt** node creates the `promptText` field containing formatted stories
2. **Select Story** node tries to access `{{ $json.promptText }}` 
3. However, `$json` refers to the CURRENT node's input, not the Format Stories node's output
4. The Select Story node receives data from Format Stories, but N8N's variable scoping means `$json.promptText` is undefined

### Evidence Found

In the Select Story node prompt:
```
Stories to Evaluate:
{{ $json.promptText }}
```

This variable reference is incorrect because:
- `$json` refers to the immediate input data
- The `promptText` field was created in the "Format Stories for Prompt" node
- N8N requires explicit node references to access data from other nodes

## Impact

**CRITICAL**: Without access to the actual RSS stories, the Select Story LLM:
- Has no real stories to select from
- Is forced to hallucinate/invent stories
- Completely bypasses all 4 anti-hallucination layers
- Produces 100% fabricated content

## Solutions

### Solution 1: Direct Node Reference (RECOMMENDED)
**Implementation**: Replace the undefined variable with explicit node reference
```
Change from: {{ $json.promptText }}
Change to: {{ $('Format Stories for Prompt').item.json.promptText }}
```

**Pros:**
- Simple one-line fix
- Maintains existing workflow structure
- Properly accesses the formatted stories

**Cons:**
- None

### Solution 2: Pass Data Through Input
**Implementation**: Ensure promptText is in the direct input chain
```javascript
// Modify Format Stories node to pass promptText in its output
return [{
  json: {
    promptText: formatted,
    stories: stories,  // Include original stories too
    storyCount: stories.length,
    timestamp: new Date().toISOString()
  }
}];
```

Then use: `{{ $json.promptText }}`

**Pros:**
- Cleaner variable reference
- Data flows naturally through the chain

**Cons:**
- Requires modifying the Format Stories node
- May need to adjust downstream nodes

### Solution 3: Use Items Array
**Implementation**: Access the first item's data explicitly
```
Change to: {{ $input.first().json.promptText }}
```

**Pros:**
- More explicit about data source
- Works with N8N's item-based processing

**Cons:**
- Less readable than Solution 1

## Recommended Fix

**Use Solution 1** - Change the Select Story node prompt from:
```
Stories to Evaluate:
{{ $json.promptText }}
```

To:
```
Stories to Evaluate:
{{ $('Format Stories for Prompt').item.json.promptText }}
```

## Testing After Fix

1. **Verify Data Flow**
   - Check that Select Story receives actual story list
   - Confirm no "undefined" text in LLM prompt

2. **Test Story Selection**
   - Run workflow and verify selected story exists in RSS feeds
   - Check that all 6 output fields are populated correctly

3. **Validate Anti-Hallucination**
   - Ensure selected story passes verification node
   - Confirm story details match RSS source exactly

## Prevention Measures

1. **Add Debug Logging**
   - Log the prompt content before sending to LLM
   - Alert if promptText is undefined or empty

2. **Input Validation**
   - Add checks in Select Story node for empty/undefined input
   - Fail fast with clear error messages

3. **Documentation Update**
   - Update CLAUDE.md with variable reference patterns
   - Document the data flow between nodes

## Conclusion

This is a critical bug that completely breaks the anti-hallucination system. The fix is simple but essential - the Select Story node must reference the Format Stories node's output correctly using `$('Format Stories for Prompt').item.json.promptText` instead of the undefined `$json.promptText`.

Without this fix, the workflow will continue generating 100% hallucinated content regardless of all other anti-hallucination measures in place.