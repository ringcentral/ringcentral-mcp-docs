# RingEx Chat

**Endpoint:** `https://mcp.labs.ringcentral.com/ringex/team-chat`  
**Status:** 🟡 Labs / Beta · New  
**Transport:** SSE over HTTPS

---

## About

RingEx Chat gives your AI assistant access to RingCentral Team Messaging (Glip): chats, direct and group conversations, teams, and posts. It's one of three servers that replace the original monolithic RingCentral MCP server — this one covers team collaboration.

!!! warning "Labs status"
    This server is part of RingCentral Labs and is not covered by RingCentral's standard SLA. Tools may be renamed, modified, or removed without prior notice. Use in production environments with caution.

!!! info "Migrating from RingCentral MCP"
    If you previously used any Team Messaging tool on the deprecated RingCentral MCP server, point your client at this endpoint instead. Tool names changed during the split — Glip tools were renamed to the `team_messaging_*` convention and the generic dispatch tools were removed. Common renames:

    | Old tool | New tool |
    |------|------|
    | `platform_list_glip_chats_new` | `team_messaging_list_chats` |
    | `platform_list_glip_conversations_new` | `team_messaging_list_conversations` |
    | `platform_list_glip_teams_new` | `team_messaging_list_teams` |
    | `platform_read_glip_conversation_new` | `team_messaging_get_conversation` |
    | `platform_read_glip_posts_new` | `team_messaging_list_posts` |
    | `platform_read_glip_team_new` | `team_messaging_get_team` |
    | `platform_create_glip_conversation_new` | `open_team_messaging_conversation` |
    | `platform_create_glip_post_new` | `send_team_messaging_post` |

    Run `about_ringcentral_mcp_tools` for the authoritative current list.

---

## Connecting

See the [RingEx Chat Setup guide](ringex-chat-setup.md) for step-by-step instructions for Claude, ChatGPT, and Codex.

For other MCP clients (Cursor, etc.), add this server the same way you'd add any remote MCP server, using the endpoint above.

---

## Available tools

65 tools are available on this server.

| Tool | Requires CRM | Description |
|------|:---:|-------------|
| [`about_ringcentral_mcp_tools`](../tools/ringex-chat.md#about_ringcentral_mcp_tools) | — | List all available tools and permissions for this server |
| [`open_team_messaging_conversation`](../tools/ringex-chat.md#open_team_messaging_conversation) | — | Open a Team Messaging conversation |
| [`send_team_messaging_post`](../tools/ringex-chat.md#send_team_messaging_post) | — | Send a Team Messaging post |
| [`upload_team_messaging_file`](../tools/ringex-chat.md#upload_team_messaging_file) | — | Upload a Team Messaging file |
| [`team_messaging_activate_webhook`](../tools/ringex-chat.md#team_messaging_activate_webhook) | — | Activate a webhook |
| [`team_messaging_add_chat_to_favorites`](../tools/ringex-chat.md#team_messaging_add_chat_to_favorites) | — | Add a chat to favorites |
| [`team_messaging_add_team_members`](../tools/ringex-chat.md#team_messaging_add_team_members) | — | Add team members |
| [`team_messaging_archive_team`](../tools/ringex-chat.md#team_messaging_archive_team) | — | Archive a team |
| [`team_messaging_complete_task`](../tools/ringex-chat.md#team_messaging_complete_task) | — | Complete a task |
| [`team_messaging_create_adaptive_card`](../tools/ringex-chat.md#team_messaging_create_adaptive_card) | — | Create an adaptive card |
| [`team_messaging_create_data_export_task`](../tools/ringex-chat.md#team_messaging_create_data_export_task) | — | Create a data export task |
| [`team_messaging_create_event`](../tools/ringex-chat.md#team_messaging_create_event) | — | Create an event |
| [`team_messaging_create_event_by_group_id`](../tools/ringex-chat.md#team_messaging_create_event_by_group_id) | — | Create an event by group ID |
| [`team_messaging_create_note`](../tools/ringex-chat.md#team_messaging_create_note) | — | Create a note |
| [`team_messaging_create_task`](../tools/ringex-chat.md#team_messaging_create_task) | — | Create a task |
| [`team_messaging_create_team`](../tools/ringex-chat.md#team_messaging_create_team) | — | Create a team |
| [`team_messaging_create_webhook_in_group`](../tools/ringex-chat.md#team_messaging_create_webhook_in_group) | — | Create a webhook in a group |
| [`team_messaging_delete_adaptive_card`](../tools/ringex-chat.md#team_messaging_delete_adaptive_card) | — | Delete an adaptive card |
| [`team_messaging_delete_event`](../tools/ringex-chat.md#team_messaging_delete_event) | — | Delete an event |
| [`team_messaging_delete_note`](../tools/ringex-chat.md#team_messaging_delete_note) | — | Delete a note |
| [`team_messaging_delete_post`](../tools/ringex-chat.md#team_messaging_delete_post) | — | Delete a post |
| [`team_messaging_delete_task`](../tools/ringex-chat.md#team_messaging_delete_task) | — | Delete a task |
| [`team_messaging_delete_team`](../tools/ringex-chat.md#team_messaging_delete_team) | — | Delete a team |
| [`team_messaging_delete_webhook`](../tools/ringex-chat.md#team_messaging_delete_webhook) | — | Delete a webhook |
| [`team_messaging_get_adaptive_card`](../tools/ringex-chat.md#team_messaging_get_adaptive_card) | — | Get an adaptive card |
| [`team_messaging_get_chat`](../tools/ringex-chat.md#team_messaging_get_chat) | — | Get a chat |
| [`team_messaging_get_company_info`](../tools/ringex-chat.md#team_messaging_get_company_info) | — | Get company info |
| [`team_messaging_get_conversation`](../tools/ringex-chat.md#team_messaging_get_conversation) | — | Get a conversation |
| [`team_messaging_get_data_export_task`](../tools/ringex-chat.md#team_messaging_get_data_export_task) | — | Get a data export task |
| [`team_messaging_get_event`](../tools/ringex-chat.md#team_messaging_get_event) | — | Get an event |
| [`team_messaging_get_everyone_chat`](../tools/ringex-chat.md#team_messaging_get_everyone_chat) | — | Get the Everyone chat |
| [`team_messaging_get_note`](../tools/ringex-chat.md#team_messaging_get_note) | — | Get a note |
| [`team_messaging_get_post`](../tools/ringex-chat.md#team_messaging_get_post) | — | Get a post |
| [`team_messaging_get_task`](../tools/ringex-chat.md#team_messaging_get_task) | — | Get a task |
| [`team_messaging_get_team`](../tools/ringex-chat.md#team_messaging_get_team) | — | Get a team |
| [`team_messaging_get_webhook`](../tools/ringex-chat.md#team_messaging_get_webhook) | — | Get a webhook |
| [`team_messaging_join_team`](../tools/ringex-chat.md#team_messaging_join_team) | — | Join a team |
| [`team_messaging_leave_team`](../tools/ringex-chat.md#team_messaging_leave_team) | — | Leave a team |
| [`team_messaging_list_chat_tasks`](../tools/ringex-chat.md#team_messaging_list_chat_tasks) | — | List tasks in a chat |
| [`team_messaging_list_chats`](../tools/ringex-chat.md#team_messaging_list_chats) | — | List chats |
| [`team_messaging_list_conversations`](../tools/ringex-chat.md#team_messaging_list_conversations) | — | List conversations |
| [`team_messaging_list_data_export_tasks`](../tools/ringex-chat.md#team_messaging_list_data_export_tasks) | — | List data export tasks |
| [`team_messaging_list_favorite_chats`](../tools/ringex-chat.md#team_messaging_list_favorite_chats) | — | List favorite chats |
| [`team_messaging_list_group_events`](../tools/ringex-chat.md#team_messaging_list_group_events) | — | List group events |
| [`team_messaging_list_notes`](../tools/ringex-chat.md#team_messaging_list_notes) | — | List notes |
| [`team_messaging_list_posts`](../tools/ringex-chat.md#team_messaging_list_posts) | — | List posts |
| [`team_messaging_list_recent_chats`](../tools/ringex-chat.md#team_messaging_list_recent_chats) | — | List recent chats |
| [`team_messaging_list_teams`](../tools/ringex-chat.md#team_messaging_list_teams) | — | List teams |
| [`team_messaging_list_user_events`](../tools/ringex-chat.md#team_messaging_list_user_events) | — | List user events |
| [`team_messaging_list_webhooks`](../tools/ringex-chat.md#team_messaging_list_webhooks) | — | List webhooks |
| [`team_messaging_list_webhooks_in_group`](../tools/ringex-chat.md#team_messaging_list_webhooks_in_group) | — | List webhooks in a group |
| [`team_messaging_lock_note`](../tools/ringex-chat.md#team_messaging_lock_note) | — | Lock a note |
| [`team_messaging_publish_note`](../tools/ringex-chat.md#team_messaging_publish_note) | — | Publish a note |
| [`team_messaging_remove_chat_from_favorites`](../tools/ringex-chat.md#team_messaging_remove_chat_from_favorites) | — | Remove a chat from favorites |
| [`team_messaging_remove_team_members`](../tools/ringex-chat.md#team_messaging_remove_team_members) | — | Remove team members |
| [`team_messaging_suspend_webhook`](../tools/ringex-chat.md#team_messaging_suspend_webhook) | — | Suspend a webhook |
| [`team_messaging_unarchive_team`](../tools/ringex-chat.md#team_messaging_unarchive_team) | — | Unarchive a team |
| [`team_messaging_unlock_note`](../tools/ringex-chat.md#team_messaging_unlock_note) | — | Unlock a note |
| [`team_messaging_update_adaptive_card`](../tools/ringex-chat.md#team_messaging_update_adaptive_card) | — | Update an adaptive card |
| [`team_messaging_update_event`](../tools/ringex-chat.md#team_messaging_update_event) | — | Update an event |
| [`team_messaging_update_everyone_chat`](../tools/ringex-chat.md#team_messaging_update_everyone_chat) | — | Update the Everyone chat |
| [`team_messaging_update_note`](../tools/ringex-chat.md#team_messaging_update_note) | — | Update a note |
| [`team_messaging_update_post`](../tools/ringex-chat.md#team_messaging_update_post) | — | Update a post |
| [`team_messaging_update_task`](../tools/ringex-chat.md#team_messaging_update_task) | — | Update a task |
| [`team_messaging_update_team`](../tools/ringex-chat.md#team_messaging_update_team) | — | Update a team |

---

## Getting started

1. **Connect** — Add the server URL above to your AI client.
2. **Verify** — Ask your assistant to list your team messaging chats to confirm the connection is active.
3. **Use** — Ask your AI assistant to catch you up on a chat, post an update, manage tasks/notes/events, or administer teams and webhooks. Tool names differ from the deprecated server — see the migration note above.

---

## Tool discovery

```bash
curl https://mcp.labs.ringcentral.com/ringex/team-chat \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}'
```
