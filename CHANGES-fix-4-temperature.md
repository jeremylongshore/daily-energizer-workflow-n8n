# Fix 4: Set Temperature to Zero

## Changes Required

Update all LLM nodes to use temperature = 0 for deterministic output.

### Nodes to Update

#### 1. GPT4o-mini 1 (ID: a6141442-9952-454c-a72f-10bbb84493da)
Update parameters.options:
```json
"options": {
  "maxTokens": 1200,
  "temperature": 0
}
```

#### 2. Gpt4o-mini 2 (ID: 6335a2ea-c636-49f3-aa7f-512b69d2156b)
Update parameters.options:
```json
"options": {
  "maxTokens": 1000,
  "temperature": 0
}
```

#### 3. Gpt4o-mini (ID: 1ae71c67-6ed1-4486-8d9d-a911d65c6f37)
Update parameters.options:
```json
"options": {
  "maxTokens": 500,
  "temperature": 0
}
```

### Why Temperature = 0?

- **Temperature 0**: Completely deterministic, always selects most likely token
- **Temperature 0.4** (current): Adds randomness, can lead to variations
- **For story selection**: We want consistency and reliability
- **Prevents**: Creative interpretations that might lead to hallucinations

### Additional Recommended Settings

Consider adding these to further reduce hallucination risk:

```json
"options": {
  "maxTokens": 1200,
  "temperature": 0,
  "topP": 1,
  "frequencyPenalty": 0,
  "presencePenalty": 0
}
```

## Testing
1. Run workflow 5 times with same input
2. Verify same story is selected each time
3. Check that output format is consistent
4. Confirm no creative variations in selection