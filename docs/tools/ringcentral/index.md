# RingCentral MCP Tools

Tools provided by the [RingCentral MCP](../../servers/rc-labs-mcp.md) server (`https://mcp.labs.ringcentral.com/ringex`). This server exposes 23 tools covering team messaging, call log, messages, directory search, presence, extension management, and AI-generated call notes.

**CRM required:** No — all tools operate against the authenticated user's RingCentral account directly.

---

## Meta & discovery

Tools for understanding what the server can do and routing user requests to the right tool.

| Tool | Description |
|------|-------------|
| [gatekeeper_select_tool](gatekeeper-select-tool.md) | Translates a natural-language request into the most appropriate MCP tool call |
| [platform_get_capabilities](platform-get-capabilities.md) | Returns a help-style summary of all available API endpoints and tools |
| [platform_list_get_operations](platform-list-get-operations.md) | Lists all supported read-only GET operations and their input schemas |
| [platform_list_post_operations](platform-list-post-operations.md) | Lists all supported POST operations and their request body schemas |
| [profile_get_current_extension](profile-get-current-extension.md) | Returns the RingCentral extension for the authenticated bearer token |

---

## Generic operations

Dynamic dispatch tools for calling any supported RingCentral Platform endpoint by operation name.

| Tool | Description |
|------|-------------|
| [platform_call_get_operation](platform-call-get-operation.md) | Executes any supported read-only RingCentral Platform GET operation |
| [platform_call_post_operation](platform-call-post-operation.md) | Executes any supported RingCentral Platform POST operation |

---

## Team messaging

Tools for working with RingCentral Team Messaging (formerly Glip) chats, conversations, teams, and posts.

| Tool | Description |
|------|-------------|
| [platform_create_glip_conversation_new](platform-create-glip-conversation-new.md) | Create or open a direct or group conversation |
| [platform_create_glip_post_new](platform-create-glip-post-new.md) | Create a post in a chat |
| [platform_list_glip_chats_new](platform-list-glip-chats-new.md) | List all chats the authenticated user belongs to |
| [platform_list_glip_conversations_new](platform-list-glip-conversations-new.md) | List direct and group conversations |
| [platform_list_glip_teams_new](platform-list-glip-teams-new.md) | List teams the authenticated user is a member of |
| [platform_read_glip_conversation_new](platform-read-glip-conversation-new.md) | Get details about a specific conversation |
| [platform_read_glip_posts_new](platform-read-glip-posts-new.md) | List posts in a chat |
| [platform_read_glip_team_new](platform-read-glip-team-new.md) | Get details about a specific team |

---

## Messages

Tools for reading SMS, fax, voicemail, and pager messages from the message store.

| Tool | Description |
|------|-------------|
| [platform_list_messages](platform-list-messages.md) | List messages in a user's message store |
| [platform_read_message](platform-read-message.md) | Get one or more messages by ID |
| [platform_read_message_content](platform-read-message-content.md) | Download the binary content of a message attachment |

---

## Call log

| Tool | Description |
|------|-------------|
| [platform_read_user_call_log](platform-read-user-call-log.md) | List call log records for a user's extension |

---

## Extension & presence

| Tool | Description |
|------|-------------|
| [platform_read_extension](platform-read-extension.md) | Get details about a RingCentral extension |
| [platform_read_unified_presence](platform-read-unified-presence.md) | Get the unified presence status for an extension |

---

## AI

| Tool | Description |
|------|-------------|
| [platform_read_ai_notes](platform-read-ai-notes.md) | Get AI-generated notes for a telephony session |

---

## Directory

| Tool | Description |
|------|-------------|
| [platform_search_directory_entries](platform-search-directory-entries.md) | Search the company directory for extensions and users |
