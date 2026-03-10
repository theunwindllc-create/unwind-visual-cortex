# Premiere Pro UXP API - Asset Import Implementation Notes

## Key API Methods for Asset Import (P2-T003)

### Project.importFiles()
**Signature:**
```typescript
importFiles(
  filePaths: string[],
  suppressUI: boolean,
  targetBin: ProjectItem,
  asNumberedStills: boolean
): boolean
```

**Parameters:**
- `filePaths`: Array of absolute file paths to import
- `suppressUI`: Set to `true` to suppress import dialog
- `targetBin`: Target bin (ProjectItem) to import into. If null, imports to root.
- `asNumberedStills`: Set to `true` for image sequences

**Returns:** `boolean` - Success status

### Getting Active Project
```typescript
const app = require('premierepro');
const project = await app.Project.getActiveProject();
```

### Getting/Creating Bins
To create a bin, we need to use the ProjectItem structure:
- Root item: `project.getRootItem()` returns FolderItem
- Need to check FolderItem API for bin creation

### Important Notes:
1. **importFiles is synchronous** (returns boolean, not Promise)
2. **targetBin parameter is optional** - can pass null to import to root
3. **suppressUI should be true** for automation
4. **asNumberedStills should be false** for video files

## Next Steps:
1. Check FolderItem/ProjectItem API for bin creation
2. Implement actual importFiles call in premiere_api.ts
3. Test with real Premiere Pro instance

## FolderItem API - Bin Creation

### createBinAction()
**Signature:**
```typescript
createBinAction(
  name: string,
  makeUnique: boolean
): Action
```

**Important:** This returns an **Action** object, not a bin directly!
- Actions need to be executed within a transaction
- Use `project.executeTransaction()` to execute actions

### Bin Creation Pattern:
```typescript
const project = await app.Project.getActiveProject();
const rootItem = project.getRootItem();

// Create bin action
await project.executeTransaction((compoundAction) => {
  const createBinAction = rootItem.createBinAction(binName, true);
  compoundAction.addAction(createBinAction);
}, "Create Bin");
```

### Getting Bin After Creation:
After creating a bin, need to:
1. Get root item: `project.getRootItem()`
2. Get items: `rootItem.getItems()`
3. Find bin by name

### Key Insight:
- Premiere UXP uses an **Action-based API** for modifications
- Actions must be executed within transactions
- This is different from direct method calls
