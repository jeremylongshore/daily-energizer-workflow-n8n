# Fix 1: Date Filtering Implementation

## Changes Required

Add 10 new Code nodes after each "Set RSS Fields" node to filter stories by date.

### Node Code Template
Place this after each "Set RSS Fields" node (Set RSS Fields, Set RSS Fields1, ... Set RSS Fields9):

```javascript
// Filter stories to only include those from last 48 hours
const items = $input.all();
const fortyEightHoursAgo = new Date();
fortyEightHoursAgo.setHours(fortyEightHoursAgo.getHours() - 48);

const filteredItems = items.filter(item => {
  const storyDate = new Date(item.json.pubDate);
  const isRecent = storyDate >= fortyEightHoursAgo;
  
  if (isRecent) {
    // Add hours_old field for later use
    const hoursOld = Math.round((new Date() - storyDate) / (1000 * 60 * 60));
    item.json.hours_old = hoursOld;
    return true;
  }
  return false;
});

console.log(`Filtered ${items.length} stories down to ${filteredItems.length} from last 48 hours`);
return filteredItems;
```

### Node Properties
- Type: n8n-nodes-base.code
- Name: "Filter Last 48 Hours (Source Name)"
- Position: After each Set RSS Fields node

### Connection Updates
1. Disconnect "Set RSS Fields" from "Merge Stories"
2. Connect "Set RSS Fields" → "Filter Last 48 Hours" → "Merge Stories"

### Format Stories Update
Update the "Format Stories for Prompt" node to include hours_old:

```javascript
const stories = items[0].json.stories;

if (!stories || stories.length === 0) {
  throw new Error("No stories found to format!");
}

const formatted = stories.map((story, index) => {
  // Validate required fields
  if (!story.title || !story.summary || !story.pubDate) {
    console.log(`Story ${index + 1} missing required fields:`, story);
    return null;
  }
  
  const hoursOld = story.hours_old || 'Unknown';
  
  return `Story ${index + 1}:
Title: ${story.title}
Summary: ${story.summary}
Published: ${story.pubDate}
Hours Old: ${hoursOld}`;
}).filter(s => s !== null).join('\n\n');

if (formatted.length === 0) {
  throw new Error("No valid stories to format!");
}

return [{
  json: {
    promptText: formatted,
    storyCount: stories.length,
    timestamp: new Date().toISOString()
  }
}];
```

## Testing
After implementing:
1. Run the workflow
2. Check console logs for filtering messages
3. Verify all selected stories are < 48 hours old
4. Confirm hours_old field appears in story data