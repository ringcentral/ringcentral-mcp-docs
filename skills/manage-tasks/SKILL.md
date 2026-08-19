---
name: manage-tasks
description: Creates, finds, updates, completes/reopens, or deletes RingCentral Team Chat tasks on behalf of the authenticated RingEX Chat user, resolving the destination chat and any assignees before writing and verifying completion state after it. Use when the user wants to create a task, assign a task, see what tasks are in a chat/channel, change a task's due date or assignee, mark a task done, reopen a task, or delete a task — not for Jira, monday.com, or other non-RingCentral task systems.
---

<!-- --8<-- [start:body] -->
# Manage Tasks

## Goal

Give the user one skill for the full lifecycle of a RingCentral Team Chat task — find it, create it, update it, mark it complete or reopen it, or delete it — with every write built on a resolved chat and person, and every completion verified rather than assumed.

## Trigger examples

- "Create a task in the launch channel to review the BRD, assign it to Priya."
- "What tasks are open in the product-updates chat?"
- "Mark the 'Fix auth bug' task done."
- "Reopen the deploy checklist task, I closed it too soon."
- "Push the due date on that task to next Friday."
- "Delete the old onboarding task in the sales channel."

## Scope boundary

- RingCentral Team Chat tasks only, via `read_team_chat`/`manage_chat_item` — not Jira, monday.com, or any other tracker (those have their own skills/tools).
- This skill only manages the task item itself — notes and events use the same two tools but a different `resource`, and are out of scope here.
- Reuse a `chatId`, `taskId`, or resolved person id already established earlier in the conversation. Re-resolving something already known wastes calls and risks landing on a different match the second time.

## Workflow

1. **Resolve the chat.**
      - A known `chatId` → use it directly.
      - A named channel/team → `read_team_chat` (`resource: "chat"`, `action: "list"`), matched by name, case-insensitively, preferring an exact match. If more than one plausibly matches, disambiguate rather than guess.

2. **Resolve any people involved.**
      - "Me"/"myself" → the authenticated user's own Team Chat person id.
      - A named assignee → `find_person`. A `personId` and an `extensionId` are distinct fields — never substitute one for the other.

3. **Find an existing task, if the request is about one.**
      - `read_team_chat` (`resource: "task"`, `action: "list"`, `chatId`) to list a chat's tasks, or `action: "get"` with a known `taskId` for one task's detail.
      - Match a task named by title case-insensitively, preferring an exact match. If several plausible tasks remain, ask which one before writing — never guess on an ambiguous title, especially before a delete.

4. **Create, update, complete/reopen, or delete, via `manage_chat_item`.**
      - **Create** (`resource: "task"`, `action: "create"`): requires the resolved `chatId` plus the task's content and assignee fields — build the payload from what the user actually asked for rather than padding in defaults; the exact field names for this action are visible in `tools/list`.
      - **Update** (`action: "update"`, `taskId`): send only the fields that should change.
      - **Complete or reopen** (`action: "complete"`, `taskId`, `status`): `status` is required on every call to this action. Send `"Complete"` to close it or `"Incomplete"` to reopen it — the completed state a subsequent read reports back is spelled `"Completed"`, a deliberate asymmetry, not a bug. This action's write response is empty, so always verify afterward with `read_team_chat` (`resource: "task"`, `action: "get"`, `taskId`) before telling the user it succeeded.
      - **Delete** (`action: "delete"`, `taskId`): only on an explicit ask, and only once the exact task is confirmed — this is irreversible.

## Guidance

- Never create a task into a loosely resolved chat, or assign it to a loosely resolved person — resolve first, act second.
- Never guess which task a title refers to when more than one plausible match exists; ask instead, particularly before a delete.
- Never claim a task completed or reopened without the follow-up `get` confirming it — the write call succeeding at the transport level isn't the same thing.
- Never resend a `complete`/`reopen` call without its `status` field, and never treat a rejected, correctly-formed request as a schema problem to probe by trial and error — read the task once to see its actual state, retry at most once if the failure looks transient, and otherwise report the rejection plainly.
<!-- --8<-- [end:body] -->
