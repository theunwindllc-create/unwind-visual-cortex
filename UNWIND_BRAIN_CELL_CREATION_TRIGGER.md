# Unwind Brain Cell Creation Trigger

**Purpose:** To ensure the standardized "Unwind Brain Scaffolding System" is used whenever the user requests the creation of a new brain cell.

## Trigger Phrases

When the user's prompt includes any of the following phrases (or close variations), the system MUST reference the master prompt for creating a new brain cell:

*   "create a new cell in the brain"
*   "let's create a new brain cell"
*   "do a new cell in the brain"
*   "spin up a new brain"
*   "new Unwind Brain"
*   "scaffold a new brain"

## Action to be Taken

Upon detecting any of the trigger phrases, the system MUST perform the following actions:

1.  **Reference the Master System Guide:** Immediately access and review the contents of the `UNWIND_BRAIN_COMPLETE_SYSTEM.md` file to determine the correct workflow.
2.  **Follow the Decision Tree:** Use the decision tree in Section 3 of the Master System Guide to select the appropriate SOP (`MASTER_SOP_Brain_Cell_Creation.md` for creation, or `UNWIND_BRAIN_MASTER_PROMPT.md` for setup).

2.  **Use the Quick Start Guide:** Present the user with the "Quick Start Prompt" from the `UNWIND_BRAIN_QUICK_START_GUIDE.md` to gather the necessary information for the new brain cell (i.e., name, purpose, functionality, integrations).

3.  **Execute the Scaffolding Script:** Use the `unwind_brain_scaffolder.py` script with the user-provided information to automate the creation of the new brain cell's directory structure, tracking database, and all associated coordination files.

4.  **Follow the Standard Protocol:** Adhere strictly to the multi-agent coordination protocol as defined in the master prompt for all subsequent development on the new brain cell.

**Author:** Unwind Code
