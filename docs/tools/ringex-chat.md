# RingEX Chat — Tools Reference

Full reference for every tool available on the [RingEX Chat](../servers/ringex-chat.md) server. As of **v1.1.0**, the 65 fine-grained `team_messaging_*` tools have been replaced with 9 workflow-oriented tools. Most write tools accept a `resource` and/or `action` discriminator instead of exposing a separate tool per operation — pick the resource/action combination for what you want to do, then supply the ids and fields that combination requires.

Tools are listed alphabetically — use the on-page navigation ("On this page") to jump to a specific tool.

!!! tip "Exact schemas live in `tools/list`"
    The tables below document every supported resource/action combination and what it does, but the authoritative required/optional fields for a given combination are always visible by calling `tools/list` on the server. Resource/action tables here are guidance, not a substitute for that schema.

---

## about_ringcentral_mcp_tools

Call this first when you want to know what a RingEX MCP server can do, what tools are available, or which RingCentral tasks are supported. Returns a concise overview of the available tool categories and representative tool names for the connected server.

**Available on:** [RingEX Phone](../servers/ringex-phone.md) · [RingEX Chat](../servers/ringex-chat.md) · [RingEX Admin](../servers/ringex-admin.md)  
**Access:** Read-only

---

### Parameters

This tool takes no parameters.

---

### Returns

| Field | Type | Description |
|-------|------|-------------|
| `summary` | `string` | A short description of what the connected server can help with. |
| `categories` | `array` | A list of capability categories, each with: `category` (name), `examples` (example use cases), and `representativeTools` (a sample of tool names in that category). |
| `usageNotes` | `array` | Operational tips — e.g. that `tools/list` should be used to inspect exact tool names and input schemas, that authenticated `accountId`/`extensionId` parameters usually default to the current user, and that write tools should only be selected when the user actually asks for that side effect. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "about_ringcentral_mcp_tools",
        "arguments": {}
      }
    }
    ```

=== "Claude prompt"

    ```
    What can this RingCentral MCP server do?
    ```

---

!!! tip "Start here"
    Run this tool right after connecting a new RingEX server to confirm which capabilities and tools are exposed, before calling `tools/list` for exact schemas.

---

## find_person

Resolves a RingCentral Team Chat person by exact person id, or by name, email, extension number, or phone number through the company directory. Returns a single resolved person for an exact match, a compact candidate list when the query is ambiguous, or `not_found` when nothing matches — it never guesses. `personId`, `extensionId`, email, extension number, and phone number are returned as distinct labeled fields and must not be treated as interchangeable.

**Server:** [RingEX Chat](../servers/ringex-chat.md)  
**Access:** Read-only

!!! note "Not a directory admin tool"
    This tool resolves a person for use with `send_post` or `manage_team` — it does not perform administrative directory reads or user changes. Use RingEX Admin for that.

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `personId` | — | Exact RingCentral Team Chat person id. Resolves the person directly. Provide either `personId` or `query`, never both. |
| `query` | — | A name, email address, extension number, or phone number to resolve through the company directory. Provide either `personId` or `query`, never both. |

---

### Returns

A single resolved person (with distinct `personId`, `extensionId`, email, and phone fields), a compact list of candidates if the query is ambiguous, or a `not_found` result.

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "find_person",
        "arguments": { "query": "Ada Lovelace" }
      }
    }
    ```

=== "Claude prompt"

    ```
    Find Ada Lovelace in the team chat directory.
    ```

---

## read_team_chat

Reads RingCentral Team Chat resources with a strict, discriminated input. Select a `resource` (`chat`, `post`, `file`, `adaptive_card`, `note`, `task`, `event`, `incoming_webhook`) and an `action`, then supply the ids and filters that action requires. This tool is strictly read-only and stays available even when write tools are disabled.

**Server:** [RingEX Chat](../servers/ringex-chat.md)  
**Access:** Read-only

---

### Supported resource / action combinations

| Resource | Actions | Notes |
|----------|---------|-------|
| `chat` | `list`, `get` | `list` covers all/recent/favorite chats, direct conversations, teams, and the Everyone chat, filtered by `type`. `get` retrieves one chat, conversation, team, or company info by id. |
| `post` | `list`, `get`, `list_attachments` | `list_attachments` discovers attachments across one bounded page of posts in a chat. |
| `file` | `download` | Requires `chatId`, `postId`, and `fileId` from a readable post. Returns bounded file content as a native MCP image, audio, or embedded resource. |
| `adaptive_card` | `get` | Reads an existing card; use `manage_adaptive_card` to create/update/delete. |
| `note` | `list`, `get` | Use `manage_chat_item` to create/update/publish/lock/unlock/delete. |
| `task` | `list`, `get` | Use `manage_chat_item` to create/update/complete/delete. |
| `event` | `list`, `get` | Use `manage_chat_item` to create/update/delete. |
| `incoming_webhook` | `list`, `get` | Use `manage_incoming_webhook` to create/activate/suspend/delete. |

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `resource` | ✅ | One of `chat`, `post`, `file`, `adaptive_card`, `note`, `task`, `event`, `incoming_webhook`. |
| `action` | ✅ | The read action valid for the chosen resource (see table above). |
| *(resource-specific)* | — | Ids and filters required by the chosen resource/action — e.g. `chatId`, `postId`, `fileId`, `recordCount`, `type`. Exact fields are visible in `tools/list`. |

---

### Examples

=== "List recent chats"

    ```json
    {
      "resource": "chat",
      "action": "list",
      "type": "recent",
      "recordCount": 30
    }
    ```

=== "List posts in a chat"

    ```json
    {
      "resource": "post",
      "action": "list",
      "chatId": "123",
      "recordCount": 20
    }
    ```

=== "Get a task"

    ```json
    {
      "resource": "task",
      "action": "get",
      "taskId": "task-123"
    }
    ```

=== "Download a file"

    ```json
    {
      "resource": "file",
      "action": "download",
      "chatId": "123",
      "postId": "post-456",
      "fileId": "file-789"
    }
    ```

=== "Claude prompt"

    ```
    Show me the last 20 posts in the product-updates chat.
    ```

---

## send_post

Sends a RingCentral Team Chat post, optionally with file or image attachments, to a known chat (`chatId`) or a resolved person (`personId`) for a direct chat. When a person is the destination, the direct conversation is opened or reused first. Files are uploaded before the post is created. The result reports the destination chat id, created post id, uploaded attachment ids, and per-step status, so a failed post can be retried without re-uploading.

**Server:** [RingEX Chat](../servers/ringex-chat.md)  
**Access:** Write

!!! tip "Resolve people first"
    Use `find_person` to resolve a name, email, or phone number to a `personId` before calling `send_post`.

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `chatId` | One of `chatId`/`personId` | A known Team Chat chat id to post into. |
| `personId` | One of `chatId`/`personId` | A resolved Team Chat person id (from `find_person`) for a direct chat. The direct conversation is opened or reused before posting. |
| `text` | ✅ | The post text (max 10,000 characters). |
| `threadId` | — | Optional thread id to reply within a thread of the destination chat. |
| `files` | — | Optional array (1–25) of file/image attachments, uploaded before the post is created. Each entry is either a file reference (`file`) or raw base64 bytes (`contentBase64` + `contentType` + `name`) — do not pass a local path, sandbox URI, data URL, or arbitrary URL. |

---

### Returns

The destination chat id, the created post id, any uploaded attachment ids, and per-step status for the resolve/upload/post workflow.

---

### Examples

=== "Post to a chat"

    ```json
    { "chatId": "chat-123", "text": "Deployment completed successfully." }
    ```

=== "Post to a person"

    ```json
    { "personId": "person-456", "text": "Could you review the deployment?" }
    ```

=== "Reply in a thread"

    ```json
    { "chatId": "chat-123", "text": "Acknowledged.", "threadId": "post-789" }
    ```

=== "Claude prompt"

    ```
    Post in the sales channel that the demo is confirmed.
    ```

---

## manage_post

Updates or deletes an existing RingCentral Team Chat post. Reading posts uses `read_team_chat`. This tool can delete content, so it is annotated as destructive.

**Server:** [RingEX Chat](../servers/ringex-chat.md)  
**Access:** Write · Destructive

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `action` | ✅ | `update` or `delete`. |
| `chatId` / `postId` | ✅ | Identify the post to update or delete. |
| `text` | Required for `update` | Replacement text for the post. |

---

### Examples

=== "Update a post"

    ```json
    { "action": "update", "chatId": "chat-123", "postId": "post-789", "text": "Corrected: deployment completed at 4:15pm." }
    ```

=== "Delete a post"

    ```json
    { "action": "delete", "chatId": "chat-123", "postId": "post-789" }
    ```

---

## manage_adaptive_card

Creates, updates, or deletes a RingCentral Team Chat Adaptive Card. Cards must be **version 1.3** with only `Action.OpenUrl` and `Action.Submit` actions and meaningful `fallbackText` — other versions or actions are rejected before the request reaches RingCentral. Reading cards uses `read_team_chat`. This tool can delete content, so it is annotated as destructive.

**Server:** [RingEX Chat](../servers/ringex-chat.md)  
**Access:** Write · Destructive

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `action` | ✅ | `create`, `update`, or `delete`. |
| `chatId` | ✅ | The chat to post the card into (for `create`), or that contains it (for `update`/`delete`). |
| `card` | Required for `create`/`update` | Adaptive Card payload — version `1.3`, body elements, and only `Action.OpenUrl`/`Action.Submit` in `actions`. Must include `fallbackText`. |
| `cardId` | Required for `update`/`delete` | Id of the existing card. |

---

### Example

=== "Create a card (Open URL)"

    ```json
    {
      "action": "create",
      "chatId": "chat-123",
      "card": {
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "type": "AdaptiveCard",
        "version": "1.3",
        "fallbackText": "A pull request is ready for review.",
        "body": [
          { "type": "TextBlock", "text": "Pull request ready for review", "weight": "Bolder", "wrap": true }
        ],
        "actions": [
          { "type": "Action.OpenUrl", "title": "Open pull request", "url": "https://example.com/pull/123" }
        ]
      }
    }
    ```

=== "Create a card (Submit choice)"

    ```json
    {
      "action": "create",
      "chatId": "chat-123",
      "card": {
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "type": "AdaptiveCard",
        "version": "1.3",
        "fallbackText": "Approval is requested for change CHG-123.",
        "body": [
          { "type": "TextBlock", "text": "Approve change CHG-123?", "weight": "Bolder", "wrap": true }
        ],
        "actions": [
          { "type": "Action.Submit", "title": "Approve", "data": { "changeId": "CHG-123", "decision": "approve" } },
          { "type": "Action.Submit", "title": "Reject", "data": { "changeId": "CHG-123", "decision": "reject" } }
        ]
      }
    }
    ```

!!! note "Action.Submit needs an outbound webhook"
    `Action.Submit` requires an application configured for Interactive Messages with an outbound webhook URL. A generic incoming webhook (see `manage_incoming_webhook`) cannot receive submitted interaction data.

---

## manage_team

Creates, updates, archives, unarchives, deletes, joins, or leaves a RingCentral Team Chat team; adds or removes members; adds or removes a chat from favorites; or updates the company Everyone chat. Reading teams and chats uses `read_team_chat`. This tool includes archive, delete, and remove-members actions, so it is annotated as destructive.

**Server:** [RingEX Chat](../servers/ringex-chat.md)  
**Access:** Write · Destructive

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `action` | ✅ | One of `create`, `update`, `delete`, `archive`, `unarchive`, `join`, `leave`, `add_members`, `remove_members`, `favorite`, `unfavorite`, `update_everyone`. |
| `teamId` / `chatId` | Required for most actions | Identifies the team or chat being acted on (not required for `create`). |
| `name`, `members`, etc. | Action-specific | Fields required by the chosen action — e.g. `name`/`members` for `create`, `members` for `add_members`/`remove_members`. Exact fields are visible in `tools/list`. |

---

### Examples

=== "Create a team"

    ```json
    { "action": "create", "name": "Launch Task Force", "members": ["person-1", "person-2"] }
    ```

=== "Add members"

    ```json
    { "action": "add_members", "teamId": "team-123", "members": ["person-3"] }
    ```

=== "Favorite a chat"

    ```json
    { "action": "favorite", "chatId": "chat-123" }
    ```

=== "Claude prompt"

    ```
    Create a team called "Launch Task Force" and add Ana and Ben.
    ```

---

## manage_chat_item

Creates, updates, or deletes a RingCentral Team Chat note, task, or event; publishes, locks, or unlocks a note; or completes a task. Select a `resource` (`note`, `task`, `event`) and an action valid for that resource. Reading these items uses `read_team_chat`. This tool includes delete actions, so it is annotated as destructive.

**Server:** [RingEX Chat](../servers/ringex-chat.md)  
**Access:** Write · Destructive

---

### Supported resource / action combinations

| Resource | Actions |
|----------|---------|
| `note` | `create`, `update`, `delete`, `publish`, `lock`, `unlock` |
| `task` | `create`, `update`, `delete`, `complete` |
| `event` | `create`, `update`, `delete` |

!!! note "Notes start as drafts"
    A note created with `resource: note, action: create` is a draft and isn't visible to other team members until `action: publish` is called on it.

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `resource` | ✅ | `note`, `task`, or `event`. |
| `action` | ✅ | An action valid for the chosen resource (see table above). |
| `chatId` | Required for `create` | The chat the item belongs to. |
| `noteId` / `taskId` / `eventId` | Required for update/delete/publish/lock/unlock/complete | Identifies the existing item. |
| *(resource-specific fields)* | Action-specific | e.g. text/title/due date for a task, body for a note, start/end time for an event. Exact fields are visible in `tools/list`. |

---

### Examples

=== "Create a task"

    ```json
    { "resource": "task", "action": "create", "chatId": "chat-123", "text": "Fix auth bug", "dueDate": "2026-08-14" }
    ```

=== "Complete a task"

    ```json
    { "resource": "task", "action": "complete", "taskId": "task-456" }
    ```

=== "Publish a note"

    ```json
    { "resource": "note", "action": "publish", "noteId": "note-789" }
    ```

=== "Claude prompt"

    ```
    Create a task in the engineering channel: "Fix auth bug" due Friday.
    ```

---

## manage_incoming_webhook

Creates an incoming webhook in a RingCentral Team Chat group, or activates, suspends, or deletes an existing webhook. Reading webhooks uses `read_team_chat`. This tool includes a delete action, so it is annotated as destructive.

**Server:** [RingEX Chat](../servers/ringex-chat.md)  
**Access:** Write · Destructive

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `action` | ✅ | `create`, `activate`, `suspend`, or `delete`. |
| `chatId` | Required for `create` | The group/team chat to create the webhook in. |
| `webhookId` | Required for `activate`/`suspend`/`delete` | Identifies the existing webhook. |
| `name` | Optional for `create` | A display name for the webhook. |

---

### Examples

=== "Create a webhook"

    ```json
    { "action": "create", "chatId": "chat-123", "name": "CI alerts" }
    ```

=== "Suspend a webhook"

    ```json
    { "action": "suspend", "webhookId": "webhook-456" }
    ```

---

!!! note "Data export moved to RingEX Admin"
    Prior to v1.1.0, this server also exposed `team_messaging_create_data_export_task`, `_get_data_export_task`, and `_list_data_export_tasks`. Bulk Team Chat data export is now handled by [RingEX Admin](../servers/ringex-admin.md), since it's an account-sensitive administrative workflow.
