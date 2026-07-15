# RingEx Chat — Tools Reference

Full reference for every tool available on the [RingEx Chat](../servers/ringex-chat.md) server. Tools are listed alphabetically — use the on-page navigation ("On this page") to jump to a specific tool.

---

## about_ringcentral_mcp_tools

Call this first when you want to know what a RingEx MCP server can do, what tools are available, or which RingCentral tasks are supported. Returns a concise overview of the available tool categories and representative tool names for the connected server.

**Available on:** [RingEx Phone](../servers/ringex-phone.md) · [RingEx Chat](../servers/ringex-chat.md) · [RingEx Admin](../servers/ringex-admin.md)  
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
    Run this tool right after connecting a new RingEx server to confirm which capabilities and tools are exposed, before calling `tools/list` for exact schemas.

---

## open_team_messaging_conversation

Opens (or creates) a direct RingCentral Team Messaging conversation with one or more known users, returning a chat id that can be used as a destination for posts or files. This tool only opens/creates the conversation — it does not send a message. It should not be used to check whether a historical conversation already exists, since it may create one; list conversations instead for that purpose. Member names must already be resolved to a user id or email before calling this tool.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `members` | ✅ | RingCentral users to include in the conversation, each as an object with an `id` or `email`. Use RingCentral user identifiers only — do not pass SMS phone numbers. |

---

### Returns

Returns the raw Team Messaging conversation response. Use the returned chat id as the destination for `send_team_messaging_post` or `upload_team_messaging_file`.

| Field | Description |
|-------|-------------|
| `id` | Team Messaging chat id for the opened/created conversation. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "open_team_messaging_conversation",
        "arguments": {
          "members": [{ "id": "1021461048" }]
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Open a direct Team Messaging conversation with John Smith so I can send him a note.
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## send_team_messaging_post

Sends a new post to an existing RingCentral Team Messaging chat. The sender is always the authenticated user — there is no way to send as someone else. The target must be a Team Messaging chat id, not an SMS conversation id. You can supply text, one or more attachment objects (from prior Team Messaging file uploads), or both, and optionally reply under a specific thread.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `teamMessagingChatId` | ✅ | Existing Team Messaging chat id to post to (e.g. `"123456789"`). Not an SMS conversation, voicemail, or message-store id. |
| `text` | — | Text content of the post (e.g. `"I am running five minutes late."`). |
| `threadId` | — | Existing Team Messaging thread id to reply under, if posting as a threaded reply. |
| `attachments` | — | Attachment objects accepted by the Team Messaging post API, such as `[{"type":"File","id":"file-id"}]`, typically produced by `upload_team_messaging_file`. |

---

### Returns

Returns the raw Team Messaging post response.

| Field | Description |
|-------|-------------|
| `id` | Team Messaging post id. |
| `groupId` | Team Messaging chat id where the post was created. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "send_team_messaging_post",
        "arguments": {
          "teamMessagingChatId": "123456789",
          "text": "I am running five minutes late."
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Post "I am running five minutes late" to the #project-phoenix chat.
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## team_messaging_activate_webhook

Activates an existing RingCentral Team Messaging webhook by its id.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `webhookId` | ✅ | Id of the webhook to activate. |

---

### Returns

Returns the raw RingCentral response for the webhook activation.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_activate_webhook",
        "arguments": {
          "webhookId": "webhook-1"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Activate the Team Messaging webhook with id webhook-1.
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## team_messaging_add_chat_to_favorites

Adds a known Team Messaging chat to the authenticated user's favorites list.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `chatId` | ✅ | Id of the chat to add to favorites. |

---

### Returns

Returns the raw RingCentral response for the favorite operation.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_add_chat_to_favorites",
        "arguments": {
          "chatId": "123456789"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Add the #project-phoenix chat to my Team Messaging favorites.
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## team_messaging_add_team_members

Adds one or more already-resolved RingCentral users to an existing Team Messaging team. Free-form names should be resolved to a user id or email (e.g. via a directory search) before calling this tool.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `chatId` | ✅ | Team Messaging team chat id (e.g. `"123"`). |
| `body` | ✅ | Members to add, as an object with a `members` array of user id or email objects, e.g. `{"members":[{"id":"1021461048"}]}`. |

---

### Returns

Returns the raw Team Messaging team member add response.

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_add_team_members",
        "arguments": {
          "chatId": "123",
          "body": {
            "members": [{ "id": "1021461048" }]
          }
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Add John Smith to the Project Phoenix team.
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## team_messaging_archive_team

Archives an existing Team Messaging team.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `chatId` | ✅ | Team Messaging team chat id to archive. |

---

### Returns

Returns the raw RingCentral response for the archive operation.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_archive_team",
        "arguments": {
          "chatId": "123"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Archive the Project Phoenix team in Team Messaging.
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## team_messaging_complete_task

Marks a known Team Messaging task as complete.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `taskId` | ✅ | Id of the task to complete. |
| `body` | ✅ | Structured request body required by the RingCentral task-complete schema. |

---

### Returns

Returns the raw RingCentral response for the complete-task operation.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_complete_task",
        "arguments": {
          "taskId": "task-1",
          "body": {}
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Mark my "Review contract" task as complete.
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## team_messaging_create_adaptive_card

Creates an adaptive card in a known Team Messaging chat. Only include card fields that were requested by the user or required by the adaptive card schema — avoid adding empty body content just to satisfy the shape.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `chatId` | ✅ | Team Messaging chat id where the card should be created (e.g. `"123"`). Not an SMS conversation id. |
| `body` | ✅ | Structured adaptive card request body, e.g. `{"type":"AdaptiveCard","version":"1.3"}`. |

---

### Returns

Returns the raw Team Messaging adaptive card response.

| Field | Description |
|-------|-------------|
| `id` | Adaptive card id. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_create_adaptive_card",
        "arguments": {
          "chatId": "123",
          "body": {
            "type": "AdaptiveCard",
            "version": "1.3"
          }
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Create an adaptive card in the #project-phoenix chat.
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## team_messaging_create_data_export_task

Creates a Team Messaging data export task.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `body` | — | Structured request body for the data export task. Provide the fields required by the RingCentral schema. |

---

### Returns

Returns the raw RingCentral response for the create-data-export-task operation.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_create_data_export_task",
        "arguments": {
          "body": {}
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Start a data export of our Team Messaging history.
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## team_messaging_create_event_by_group_id

Creates a new Team Messaging event scoped to a specific group (chat).

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `groupId` | ✅ | Id of the group the event should be created under. |
| `body` | ✅ | Structured request body for the event. Provide the fields required by the RingCentral event schema. |

---

### Returns

Returns the raw RingCentral response for the create-event-by-group operation.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_create_event_by_group_id",
        "arguments": {
          "groupId": "123",
          "body": {
            "title": "Sprint planning",
            "startTime": "2026-07-16T10:00:00Z",
            "endTime": "2026-07-16T11:00:00Z"
          }
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Create a "Sprint planning" event in the Project Phoenix group chat for tomorrow 10-11 AM.
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## team_messaging_create_event

Creates a new Team Messaging event.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `body` | ✅ | Structured request body for the event. Provide the fields required by the RingCentral event schema (e.g. title, start/end time). |

---

### Returns

Returns the raw RingCentral response for the create-event operation.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_create_event",
        "arguments": {
          "body": {
            "title": "Team standup",
            "startTime": "2026-07-16T09:00:00Z",
            "endTime": "2026-07-16T09:30:00Z"
          }
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Create a Team Messaging event called "Team standup" tomorrow from 9:00 to 9:30 AM.
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## team_messaging_create_note

Creates a note inside a known Team Messaging chat.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `chatId` | ✅ | Team Messaging chat id where the note should be created. |
| `body` | ✅ | Structured request body for the note. Provide the fields required by the RingCentral note schema. |

---

### Returns

Returns the raw RingCentral response for the create-note operation.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_create_note",
        "arguments": {
          "chatId": "123",
          "body": {
            "title": "Meeting notes",
            "text": "Discussed Q3 roadmap."
          }
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Create a note titled "Meeting notes" in the Project Phoenix chat.
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## team_messaging_create_task

Creates a task inside a known Team Messaging chat. The request must include a subject and the assignees required by the task schema — when no assignee is specified and the current user is known, the task should default to being assigned to the current user rather than left unassigned.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `chatId` | ✅ | Team Messaging chat id where the task should be created (e.g. `"123"`). Not an SMS or message-store id. |
| `body` | ✅ | Structured task create body. Include `subject` and `assignees` as user id objects, e.g. `{"subject":"Review contract","assignees":[{"id":"1021461048"}]}`. |

---

### Returns

Returns the raw Team Messaging task response.

| Field | Description |
|-------|-------------|
| `id` | Team Messaging task id. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_create_task",
        "arguments": {
          "chatId": "123",
          "body": {
            "subject": "Review contract",
            "assignees": [{ "id": "1021461048" }]
          }
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Create a task in the Project Phoenix chat to "Review contract" and assign it to me.
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## team_messaging_create_team

Creates a new Team Messaging team.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `body` | ✅ | Structured request body for the new team. Provide the fields required by the RingCentral team schema (e.g. name, members). |

---

### Returns

Returns the raw RingCentral response for the create-team operation.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_create_team",
        "arguments": {
          "body": {
            "name": "Project Phoenix"
          }
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Create a new Team Messaging team called "Project Phoenix".
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## team_messaging_create_webhook_in_group

Creates a webhook in a known Team Messaging group.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `groupId` | ✅ | Id of the group to create the webhook in. |

---

### Returns

Returns the raw RingCentral response for the create-webhook-in-group operation.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_create_webhook_in_group",
        "arguments": {
          "groupId": "123"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Create a webhook for the Project Phoenix group chat.
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## team_messaging_delete_adaptive_card

Deletes a known Team Messaging adaptive card.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `cardId` | ✅ | Id of the adaptive card to delete. |

---

### Returns

Returns the raw RingCentral response for the delete-adaptive-card operation.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_delete_adaptive_card",
        "arguments": {
          "cardId": "card-1"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Delete the adaptive card with id card-1.
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## team_messaging_delete_event

Deletes a known Team Messaging event.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `eventId` | ✅ | Id of the event to delete. |

---

### Returns

Returns the raw RingCentral response for the delete-event operation.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_delete_event",
        "arguments": {
          "eventId": "event-1"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Delete the "Team standup" event from Team Messaging.
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## team_messaging_delete_note

Deletes a known Team Messaging note.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `noteId` | ✅ | Id of the note to delete. |

---

### Returns

Returns the raw RingCentral response for the delete-note operation.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_delete_note",
        "arguments": {
          "noteId": "note-1"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Delete the "Meeting notes" note from Team Messaging.
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## team_messaging_delete_post

Deletes a known post from a known Team Messaging chat.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `chatId` | ✅ | Team Messaging chat id containing the post. |
| `postId` | ✅ | Id of the post to delete. |

---

### Returns

Returns the raw RingCentral response for the delete-post operation.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_delete_post",
        "arguments": {
          "chatId": "123",
          "postId": "post-1"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Delete my last post in the Project Phoenix chat.
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## team_messaging_delete_task

Deletes a known Team Messaging task.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `taskId` | ✅ | Id of the task to delete. |

---

### Returns

Returns the raw RingCentral response for the delete-task operation.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_delete_task",
        "arguments": {
          "taskId": "task-1"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Delete my "Review contract" task in Team Messaging.
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## team_messaging_delete_team

Deletes an existing Team Messaging team.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `chatId` | ✅ | Team Messaging team chat id to delete. |

---

### Returns

Returns the raw RingCentral response for the delete-team operation.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_delete_team",
        "arguments": {
          "chatId": "123"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Delete the Project Phoenix team in Team Messaging.
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## team_messaging_delete_webhook

Deletes an existing Team Messaging webhook.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `webhookId` | ✅ | Id of the webhook to delete. |

---

### Returns

Returns the raw RingCentral response for the delete-webhook operation.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_delete_webhook",
        "arguments": {
          "webhookId": "webhook-1"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Delete the Team Messaging webhook with id webhook-1.
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## team_messaging_get_adaptive_card

Reads a known Team Messaging adaptive card by id. To read multiple cards in one call, pass a single comma-separated string of ids rather than an array.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `cardId` | ✅ | Adaptive card id to read (e.g. `"card-1"`). For multiple cards, pass one comma-separated string, e.g. `"card-1,card-2"`. |

---

### Returns

Returns the raw Team Messaging adaptive card response.

| Field | Description |
|-------|-------------|
| `id` | Adaptive card id. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_get_adaptive_card",
        "arguments": {
          "cardId": "card-1"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Show me the adaptive card with id card-1.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## team_messaging_get_chat

Reads a known Team Messaging chat by id.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `chatId` | ✅ | Id of the chat to read. |

---

### Returns

Returns the raw RingCentral response for the get-chat operation.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_get_chat",
        "arguments": {
          "chatId": "123"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Show me the details of Team Messaging chat 123.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## team_messaging_get_company_info

Gets Team Messaging company information for a known company id. This is distinct from RingCentral platform account information — use this only for Team Messaging company-level data.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `companyId` | ✅ | Team Messaging company id to read (e.g. `"company-1"`). |

---

### Returns

Returns the raw Team Messaging company information.

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_get_company_info",
        "arguments": {
          "companyId": "company-1"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Get the Team Messaging company info for company-1.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## team_messaging_get_conversation

Reads a known Team Messaging conversation by chat id.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `chatId` | ✅ | Team Messaging conversation chat id to read. |

---

### Returns

Returns the raw RingCentral response for the get-conversation operation.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_get_conversation",
        "arguments": {
          "chatId": "123"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Show me the Team Messaging conversation with id 123.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## team_messaging_get_data_export_task

Reads a known Team Messaging data export task by id.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `taskId` | ✅ | Id of the data export task to read. |

---

### Returns

Returns the raw RingCentral response for the get-data-export-task operation.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_get_data_export_task",
        "arguments": {
          "taskId": "task-1"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Check the status of my Team Messaging data export task task-1.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## team_messaging_get_event

Reads a known Team Messaging event by id.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `eventId` | ✅ | Team Messaging event id(s) to read, always passed as an array even for a single id, e.g. `["event-1"]`. |

---

### Returns

Returns the raw Team Messaging event response.

| Field | Description |
|-------|-------------|
| `id` | Team Messaging event id. |
| `title` | Event title. |
| `startTime` | Event start time, required when updating the event. |
| `endTime` | Event end time, required when updating the event. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_get_event",
        "arguments": {
          "eventId": ["event-1"]
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Show me the details of my Team Messaging event event-1.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## team_messaging_get_everyone_chat

Gets the company-wide "Everyone" Team Messaging chat.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Read-only

---

### Parameters

This tool takes no user-supplied parameters.

---

### Returns

Returns the raw RingCentral response for the get-everyone-chat operation.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_get_everyone_chat",
        "arguments": {}
      }
    }
    ```

=== "Claude prompt"

    ```
    Show me the Everyone chat in Team Messaging.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## team_messaging_get_note

Reads a known Team Messaging note by id.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `noteId` | ✅ | Id of the note to read. |

---

### Returns

Returns the raw RingCentral response for the get-note operation.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_get_note",
        "arguments": {
          "noteId": "note-1"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Show me the "Meeting notes" note from Team Messaging.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## team_messaging_get_post

Reads a single known post from a known Team Messaging chat.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `chatId` | ✅ | Team Messaging chat id containing the post. |
| `postId` | ✅ | Id of the post to read. |

---

### Returns

Returns the raw RingCentral response for the get-post operation.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_get_post",
        "arguments": {
          "chatId": "123",
          "postId": "post-1"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Show me post post-1 in the Project Phoenix chat.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## team_messaging_get_task

Reads a single known Team Messaging task by id.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `taskId` | ✅ | Team Messaging task id to read (e.g. `"task-1"`). |

---

### Returns

Returns the raw Team Messaging task response.

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_get_task",
        "arguments": {
          "taskId": "task-1"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Show me my "Review contract" task in Team Messaging.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## team_messaging_get_team

Reads a known Team Messaging team by its team chat id. Use this rather than the generic chat or conversation reader when the user explicitly asks about a team.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `chatId` | ✅ | Team Messaging team chat id to read (e.g. `"123"`). Not an SMS conversation or message-store id. |

---

### Returns

Returns the raw Team Messaging team response.

| Field | Description |
|-------|-------------|
| `id` | Team Messaging team chat id. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_get_team",
        "arguments": {
          "chatId": "123"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Show me the details of the Project Phoenix team in Team Messaging.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## team_messaging_get_webhook

Reads a known Team Messaging webhook by id.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `webhookId` | ✅ | Team Messaging webhook id(s) to read, always passed as an array even for a single id, e.g. `["webhook-1"]`. |

---

### Returns

Returns the raw Team Messaging webhook response.

| Field | Description |
|-------|-------------|
| `id` | Team Messaging webhook id. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_get_webhook",
        "arguments": {
          "webhookId": ["webhook-1"]
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Show me the Team Messaging webhook with id webhook-1.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## team_messaging_join_team

Joins the authenticated user to a known Team Messaging team.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `chatId` | ✅ | Team Messaging team chat id to join. |

---

### Returns

Returns the raw RingCentral response for the join-team operation.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_join_team",
        "arguments": {
          "chatId": "123"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Join the Project Phoenix team in Team Messaging.
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## team_messaging_leave_team

Removes the authenticated user from a known Team Messaging team.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `chatId` | ✅ | Team Messaging team chat id to leave. |

---

### Returns

Returns the raw RingCentral response for the leave-team operation.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_leave_team",
        "arguments": {
          "chatId": "123"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Leave the Project Phoenix team in Team Messaging.
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## team_messaging_list_chat_tasks

Lists tasks in a known Team Messaging chat, optionally filtered by status, assignee, creator, or creation time. A request for "pending tasks" maps to a status filter of `["Pending"]`.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `chatId` | ✅ | Team Messaging chat id whose tasks should be listed (e.g. `"123"`). |
| `status` | — | Task status filter array, one or more of `Pending`, `InProgress`, `Completed`, e.g. `["Pending"]`. |
| `assignmentStatus` | — | Assignment status filter. |
| `assigneeStatus` | — | Assignee status filter. |
| `creatorId` | — | Array of creator user ids to filter by. |
| `assigneeId` | — | Array of assignee user ids to filter by. |
| `creationTimeFrom` | — | Lower bound for task creation time. |
| `creationTimeTo` | — | Upper bound for task creation time. |
| `pageToken` | — | Token for fetching another page of task records. |
| `recordCount` | — | Maximum number of task records to return. |

---

### Returns

Returns the raw Team Messaging task records for the chat.

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_list_chat_tasks",
        "arguments": {
          "chatId": "123",
          "status": ["Pending"]
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    List all pending tasks in the Project Phoenix chat.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## team_messaging_list_chats

Lists Team Messaging chats, optionally filtered by type (Direct, Personal, Group, Team, or Everyone). Not for SMS/message-store conversations.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `type` | — | Chat type filter array, one or more of `Personal`, `Direct`, `Group`, `Team`, `Everyone`, e.g. `["Direct"]`. |
| `recordCount` | — | Maximum number of chats to return (e.g. `5`). Use only when a limit is requested. |
| `pageToken` | — | Token for fetching another page of chats. |

---

### Returns

Returns the raw Team Messaging chat records.

| Field | Description |
|-------|-------------|
| `records[].id` | Team Messaging chat id. |
| `records[].type` | Team Messaging chat type. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_list_chats",
        "arguments": {
          "type": ["Direct"]
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    List my direct Team Messaging chats.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## team_messaging_list_conversations

Lists Team Messaging conversations for the authenticated user. This is also the right tool to check whether the user has had recent or past conversations with a named person — resolve the person first, then compare their id/email against the returned conversation members. There is no date-range filter on this endpoint, so filtering by a specific period (e.g. "last week") must be done client-side against the returned timestamps after fetching enough records.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `recordCount` | — | Maximum number of conversations to fetch (e.g. `100`). Use a larger value when checking recent history since date filtering happens after the response is returned. |
| `pageToken` | — | Token for fetching another page of conversations. |

---

### Returns

Returns the raw Team Messaging conversation records for the authenticated user.

| Field | Description |
|-------|-------------|
| `records[].id` | Team Messaging conversation chat id. |
| `records[].type` | Conversation type such as Direct or Group. |
| `records[].members[]` | Participant ids or objects — compare with resolved directory user ids for person-specific questions. |
| `records[].lastModifiedTime` | Conversation update timestamp, useful for filtering relative dates such as "last week". |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_list_conversations",
        "arguments": {
          "recordCount": 100
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Have I had any Team Messaging conversations with John Smith recently?
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## team_messaging_list_data_export_tasks

Lists Team Messaging data export tasks.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `status` | — | Filter by data export task status. |
| `page` | — | Page number to fetch. |
| `perPage` | — | Number of records to return per page. |

---

### Returns

Returns the raw RingCentral response for the list-data-export-tasks operation.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_list_data_export_tasks",
        "arguments": {}
      }
    }
    ```

=== "Claude prompt"

    ```
    List my Team Messaging data export tasks.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## team_messaging_list_favorite_chats

Lists the authenticated user's favorited Team Messaging chats.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `recordCount` | — | Maximum number of favorite chats to return. |

---

### Returns

Returns the raw RingCentral response for the list-favorite-chats operation.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_list_favorite_chats",
        "arguments": {}
      }
    }
    ```

=== "Claude prompt"

    ```
    List my favorite Team Messaging chats.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## team_messaging_list_group_events

Lists Team Messaging events that belong to a known group. Use `team_messaging_list_user_events` instead when the request is about the authenticated user's own events rather than a specific group's events.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `groupId` | ✅ | Team Messaging group id whose events should be listed (e.g. `"123"`). |

---

### Returns

Returns the raw Team Messaging group event records.

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_list_group_events",
        "arguments": {
          "groupId": "123"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    List the events in the Project Phoenix group chat.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## team_messaging_list_notes

Lists notes in a known Team Messaging chat, with optional filters for creation time, creator, and status.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `chatId` | ✅ | Team Messaging chat id whose notes should be listed. |
| `creationTimeTo` | — | Upper bound for note creation time. |
| `creationTimeFrom` | — | Lower bound for note creation time. |
| `creatorId` | — | Filter by note creator id. |
| `status` | — | Filter by note status. |
| `pageToken` | — | Token for fetching another page of notes. |
| `recordCount` | — | Maximum number of notes to return. |

---

### Returns

Returns the raw RingCentral response for the list-notes operation.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_list_notes",
        "arguments": {
          "chatId": "123"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    List the notes in the Project Phoenix chat.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## team_messaging_list_posts

Lists posts in a known Team Messaging chat.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `chatId` | ✅ | Team Messaging chat id whose posts should be listed. |
| `recordCount` | — | Maximum number of posts to return. |
| `pageToken` | — | Token for fetching another page of posts. |

---

### Returns

Returns the raw RingCentral response for the list-posts operation.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_list_posts",
        "arguments": {
          "chatId": "123",
          "recordCount": 20
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Show me the last 20 posts in the Project Phoenix chat.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## team_messaging_list_recent_chats

Lists the authenticated user's recent Team Messaging chats.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `type` | — | Filter by chat type. |
| `recordCount` | — | Maximum number of recent chats to return. |

---

### Returns

Returns the raw RingCentral response for the list-recent-chats operation.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_list_recent_chats",
        "arguments": {
          "recordCount": 10
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Show me my recent Team Messaging chats.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## team_messaging_list_teams

Lists Team Messaging teams.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `recordCount` | — | Maximum number of teams to return. |
| `pageToken` | — | Token for fetching another page of teams. |

---

### Returns

Returns the raw RingCentral response for the list-teams operation.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_list_teams",
        "arguments": {}
      }
    }
    ```

=== "Claude prompt"

    ```
    List all the Team Messaging teams I'm a member of.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## team_messaging_list_user_events

Lists Team Messaging events for the authenticated user. Use `team_messaging_list_group_events` instead for events scoped to a specific group.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `recordCount` | — | Maximum number of user events to return (e.g. `20`). |
| `pageToken` | — | Token for fetching another page of user events. |

---

### Returns

Returns the raw Team Messaging user event records.

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_list_user_events",
        "arguments": {
          "recordCount": 20
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    List my upcoming Team Messaging events.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## team_messaging_list_webhooks_in_group

Lists Team Messaging webhooks in a known group. Use `team_messaging_list_webhooks` instead when the request is about all of the authenticated user's webhooks rather than one group's webhooks.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `groupId` | ✅ | Team Messaging group id whose webhooks should be listed (e.g. `"123"`). |

---

### Returns

Returns the raw Team Messaging group webhook records.

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_list_webhooks_in_group",
        "arguments": {
          "groupId": "123"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    List the webhooks configured for the Project Phoenix group chat.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## team_messaging_list_webhooks

Lists Team Messaging webhooks for the authenticated user. Use `team_messaging_list_webhooks_in_group` instead for webhooks scoped to a specific group.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Read-only

---

### Parameters

This tool takes no user-supplied parameters.

---

### Returns

Returns the raw Team Messaging webhook records.

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_list_webhooks",
        "arguments": {}
      }
    }
    ```

=== "Claude prompt"

    ```
    List all of my Team Messaging webhooks.
    ```

---

!!! info "Permission"
    This tool requires **read** access.

---

## team_messaging_lock_note

Locks a known Team Messaging note, preventing further edits.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `noteId` | ✅ | Id of the note to lock. |

---

### Returns

Returns the raw RingCentral response for the lock-note operation.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_lock_note",
        "arguments": {
          "noteId": "note-1"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Lock the "Meeting notes" note in Team Messaging.
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## team_messaging_publish_note

Publishes a known Team Messaging note, sharing it with the chat.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `noteId` | ✅ | Id of the note to publish. |

---

### Returns

Returns the raw RingCentral response for the publish-note operation.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_publish_note",
        "arguments": {
          "noteId": "note-1"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Publish the "Meeting notes" note in Team Messaging.
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## team_messaging_remove_chat_from_favorites

Removes an existing Team Messaging chat from the authenticated user's favorites. This only changes favorite status — it does not delete the chat or team.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `chatId` | ✅ | Existing Team Messaging chat id to remove from favorites (e.g. `"123"`). Not an SMS conversation or message-store id. |

---

### Returns

Returns the raw unfavorite response.

| Field | Description |
|-------|-------------|
| `id` | Team Messaging chat id whose favorite status changed. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_remove_chat_from_favorites",
        "arguments": {
          "chatId": "123"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Remove the Project Phoenix chat from my Team Messaging favorites.
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## team_messaging_remove_team_members

Removes one or more known users from a known Team Messaging team. This only removes specific members — use `team_messaging_archive_team` or `team_messaging_delete_team` to remove the whole team, and resolve any free-form names to a user id or email before calling this tool.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `chatId` | ✅ | Team Messaging team chat id (e.g. `"123"`). |
| `body` | ✅ | Members to remove, as an object with a `members` array of user id or email objects, e.g. `{"members":[{"id":"1021461048"}]}`. |

---

### Returns

Returns the raw Team Messaging team member remove response.

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_remove_team_members",
        "arguments": {
          "chatId": "123",
          "body": {
            "members": [{ "id": "1021461048" }]
          }
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Remove John Smith from the Project Phoenix team.
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## team_messaging_suspend_webhook

Suspends an active Team Messaging webhook.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `webhookId` | ✅ | Id of the webhook to suspend. |

---

### Returns

Returns the raw RingCentral response for the suspend-webhook operation.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_suspend_webhook",
        "arguments": {
          "webhookId": "webhook-1"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Suspend the Team Messaging webhook with id webhook-1.
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## team_messaging_unarchive_team

Unarchives a previously archived Team Messaging team.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `chatId` | ✅ | Team Messaging team chat id to unarchive. |

---

### Returns

Returns the raw RingCentral response for the unarchive-team operation.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_unarchive_team",
        "arguments": {
          "chatId": "123"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Unarchive the Project Phoenix team in Team Messaging.
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## team_messaging_unlock_note

Unlocks a previously locked Team Messaging note, allowing edits again.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `noteId` | ✅ | Id of the note to unlock. |

---

### Returns

Returns the raw RingCentral response for the unlock-note operation.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_unlock_note",
        "arguments": {
          "noteId": "note-1"
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Unlock the "Meeting notes" note in Team Messaging.
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## team_messaging_update_adaptive_card

Updates a known Team Messaging adaptive card. Include only the fields being changed or required by the schema — avoid adding empty optional body content just to satisfy the shape.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `cardId` | ✅ | Adaptive card id to update (e.g. `"card-1"`). |
| `body` | ✅ | Structured adaptive card update body, e.g. `{"type":"AdaptiveCard","version":"1.3"}`. |

---

### Returns

Returns the raw Team Messaging adaptive card response.

| Field | Description |
|-------|-------------|
| `id` | Adaptive card id. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_update_adaptive_card",
        "arguments": {
          "cardId": "card-1",
          "body": {
            "type": "AdaptiveCard",
            "version": "1.3"
          }
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Update the adaptive card card-1 to version 1.3.
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## team_messaging_update_event

Updates a known Team Messaging event. The update body uses the same schema as event creation and requires `title`, `startTime`, and `endTime` — when only changing the title/subject of an event, its existing start and end times should be preserved rather than omitted.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `eventId` | ✅ | Team Messaging event id to update (e.g. `"event-1"`). |
| `body` | ✅ | Structured event update body including `title`, `startTime`, and `endTime`, e.g. `{"title":"Updated standup","startTime":"2026-07-16T09:00:00Z","endTime":"2026-07-16T09:30:00Z"}`. |

---

### Returns

Returns the raw Team Messaging event response.

| Field | Description |
|-------|-------------|
| `id` | Team Messaging event id. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_update_event",
        "arguments": {
          "eventId": "event-1",
          "body": {
            "title": "Updated standup",
            "startTime": "2026-07-16T09:00:00Z",
            "endTime": "2026-07-16T09:30:00Z"
          }
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Rename my "Team standup" event to "Updated standup" in Team Messaging.
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## team_messaging_update_everyone_chat

Updates display settings (such as the display name) for the company-wide "Everyone" Team Messaging chat. At least one display setting must be included — an empty body is not accepted.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `body` | — | Everyone chat display settings update body with at least one setting, e.g. `{"name":"Everyone"}`. |

---

### Returns

Returns the raw everyone chat update response.

| Field | Description |
|-------|-------------|
| `id` | Everyone chat id. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_update_everyone_chat",
        "arguments": {
          "body": {
            "name": "Everyone"
          }
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Update the Everyone chat display name in Team Messaging.
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## team_messaging_update_note

Updates a known Team Messaging note. Optionally release the note's edit lock as part of the update.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `noteId` | ✅ | Id of the note to update. |
| `releaseLock` | — | Whether to release the note's edit lock as part of the update. |
| `body` | ✅ | Structured request body with the fields to update, per the RingCentral note schema. |

---

### Returns

Returns the raw RingCentral response for the update-note operation.

| Field | Description |
|-------|-------------|
| `id` | Resource id returned by the RingCentral API when present. |

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_update_note",
        "arguments": {
          "noteId": "note-1",
          "body": {
            "text": "Updated meeting notes."
          }
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Update my "Meeting notes" note to add the latest action items.
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## team_messaging_update_post

Updates the text or body of a known Team Messaging post in a known chat. Both the chat id and post id are required.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `chatId` | ✅ | Team Messaging chat id containing the post (e.g. `"123"`). |
| `postId` | ✅ | Team Messaging post id to update (e.g. `"post-1"`). |
| `body` | ✅ | Structured post update body, e.g. `{"text":"Updated launch note"}`. |

---

### Returns

Returns the raw Team Messaging post update response.

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_update_post",
        "arguments": {
          "chatId": "123",
          "postId": "post-1",
          "body": {
            "text": "Updated launch note"
          }
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Update my last post in the Project Phoenix chat to say "Updated launch note".
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## team_messaging_update_task

Updates fields of a known Team Messaging task, such as its subject. Use `team_messaging_complete_task` instead to mark a task as complete.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `taskId` | ✅ | Team Messaging task id to update (e.g. `"task-1"`). |
| `body` | — | Structured task update body, e.g. `{"subject":"Review updated contract"}`. |

---

### Returns

Returns the raw Team Messaging task update response.

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_update_task",
        "arguments": {
          "taskId": "task-1",
          "body": {
            "subject": "Review updated contract"
          }
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Change the subject of my task task-1 to "Review updated contract".
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## team_messaging_update_team

Updates settings for a known Team Messaging team, including renaming it. Use `team_messaging_join_team`, `team_messaging_leave_team`, `team_messaging_archive_team`, or `team_messaging_delete_team` for those specific actions instead, and use `team_messaging_update_everyone_chat` to update the Everyone chat's display settings.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `chatId` | ✅ | Team Messaging team chat id to update (e.g. `"123"`). |
| `body` | ✅ | Structured team update body, e.g. `{"name":"Project Phoenix Renamed"}`. |

---

### Returns

Returns the raw RingCentral response for the update-team operation.

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "team_messaging_update_team",
        "arguments": {
          "chatId": "123",
          "body": {
            "name": "Project Phoenix Renamed"
          }
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Rename the Project Phoenix team to "Project Phoenix Renamed" in Team Messaging.
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

## upload_team_messaging_file

Uploads a file to RingCentral Team Messaging — for example a generated image, PDF, or other document. This uploads file content only; it does not create a post. If the file should appear in a chat, use the returned file information as an attachment on a subsequent call to `send_team_messaging_post`.

**Server:** [RingEx Chat](../servers/ringex-chat.md)  
**Access:** Write

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `teamMessagingChatId` | — | Team Messaging chat id (group id) to associate the uploaded file with (e.g. `"123456789"`). Not an SMS conversation id. |
| `name` | — | File name for the uploaded file, including an extension when known (e.g. `"report.pdf"`). |
| `file` | — | Structured file reference (download URL, file id, MIME type, file name) for the file to upload. This is the preferred input for all uploads and is required for image uploads. |
| `contentBase64` | — | Legacy fallback: raw base64-encoded bytes for non-image files, used only when a `file` reference is unavailable. Not for images or file paths/URLs. |
| `content` | — | Plain-text compatibility fallback for simple inline text file content. Not for binary files or images. |

---

### Returns

Returns the raw Team Messaging file upload response. Use the returned file information as an attachment when calling `send_team_messaging_post` if the file should be posted to a chat.

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "upload_team_messaging_file",
        "arguments": {
          "teamMessagingChatId": "123456789",
          "name": "report.pdf",
          "file": {
            "download_url": "https://chatgpt.example/files/temp",
            "file_id": "file_123",
            "mime_type": "application/pdf",
            "file_name": "report.pdf"
          }
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Upload this report as a PDF to the project-phoenix Team Messaging chat.
    ```

---

!!! info "Permission"
    This tool requires **write** access.

---

