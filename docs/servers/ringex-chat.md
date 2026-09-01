# RingEX Chat

<div class="rc-spec-sheet">
<div class="rc-spec-row"><span class="rc-spec-row__label">Endpoint</span><span class="rc-spec-row__value"><code>https://mcp.labs.ringcentral.com/ringex/v1.1.0/team-chat</code><button class="rc-copy" data-copy="https://mcp.labs.ringcentral.com/ringex/v1.1.0/team-chat" aria-label="Copy endpoint URL" title="Copy endpoint URL"><svg class="rc-copy__icon--copy" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg><svg class="rc-copy__icon--check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg></button></span></div>
<div class="rc-spec-row"><span class="rc-spec-row__label">Status</span><span class="rc-spec-row__value"><span class="rc-status rc-status--preview">Preview</span></span></div>
<div class="rc-spec-row"><span class="rc-spec-row__label">Transport</span><span class="rc-spec-row__value">SSE over HTTPS</span></div>
<div class="rc-spec-row"><span class="rc-spec-row__label">Auth</span><span class="rc-spec-row__value">OAuth2</span></div>
</div>

---

## About

RingEX Chat gives your AI assistant access to RingCentral Team Messaging (Glip): chats, direct and group conversations, teams, and posts. It's one of three servers that replace the original monolithic RingCentral MCP server — this one covers team collaboration.

See the [Changelog](../changelog.md) for what's changed across versions — including the v1.1.0 tool-surface consolidation (65 tools down to 9) and the move of Team Chat data-export tools to [RingEX Admin](ringex-admin.md).

---

## Connecting

See the [RingEX Chat Setup guide](ringex-chat-setup.md) for step-by-step instructions for Claude, ChatGPT, and Codex.

For other MCP clients (Cursor, etc.), add this server the same way you'd add any remote MCP server, using the endpoint above.

---

## Available tools

9 tools are available on this server — down from 65 prior to v1.1.0. Write tools each take a `resource`/`action` (or `action`-only) discriminator that dispatches to one of several underlying operations; see the [Tools reference](../tools/ringex-chat.md) for the full breakdown per tool.

| Tool | Access | Description |
|------|:---:|-------------|
| [`about_ringcentral_mcp_tools`](../tools/ringex-chat.md#about_ringcentral_mcp_tools) | Read | List all available tools and permissions for this server |
| [`find_person`](../tools/ringex-chat.md#find_person) | Read | Resolve a person by name, email, extension, phone number, or exact Team Chat person ID |
| [`read_team_chat`](../tools/ringex-chat.md#read_team_chat) | Read | List or retrieve chats, posts, files, Adaptive Cards, notes, tasks, events, and incoming webhooks |
| [`send_post`](../tools/ringex-chat.md#send_post) | Write | Send a post — or a thread reply — to a chat or resolved person, optionally with file/image attachments |
| [`manage_post`](../tools/ringex-chat.md#manage_post) | Write | Update or delete an existing post |
| [`manage_adaptive_card`](../tools/ringex-chat.md#manage_adaptive_card) | Write | Create, update, or delete an Adaptive Card (version 1.3) |
| [`manage_team`](../tools/ringex-chat.md#manage_team) | Write | Create, update, archive, unarchive, or delete a team; join/leave; add/remove members; favorite/unfavorite a chat; update the Everyone chat |
| [`manage_chat_item`](../tools/ringex-chat.md#manage_chat_item) | Write | Create, update, complete, publish, lock/unlock, or delete a note, task, or event |
| [`manage_incoming_webhook`](../tools/ringex-chat.md#manage_incoming_webhook) | Write | Create, activate, suspend, or delete an incoming webhook |

!!! note "Data export moved"
    `team_messaging_create_data_export_task`, `_get_data_export_task`, and `_list_data_export_tasks` are no longer available here. Data export is now handled by [RingEX Admin](ringex-admin.md).

---

## Getting started

1. **Connect** — Add the server URL above to your AI client.
2. **Verify** — Ask your assistant to list your team messaging chats to confirm the connection is active.
3. **Use** — Ask your AI assistant to catch you up on a chat, post an update, manage tasks/notes/events, or administer teams and webhooks.

---

## Tool discovery

```bash
curl https://mcp.labs.ringcentral.com/ringex/v1.1.0/team-chat \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}'
```
