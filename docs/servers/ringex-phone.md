# RingEx Phone

**Endpoint:** `https://mcp.labs.ringcentral.com/ringex/phone`  
**Status:** 🟡 Labs / Beta · New  
**Transport:** SSE over HTTPS

---

## About

RingEx Phone gives your AI assistant access to telephony data: call logs, AI-generated call notes, and messages (SMS, fax, voicemail, and pager) from the message store. It's one of three servers that replace the original monolithic RingCentral MCP server — this one covers the phone and messaging side.

!!! warning "Labs status"
    This server is part of RingCentral Labs and is not covered by RingCentral's standard SLA. Tools may be renamed, modified, or removed without prior notice. Use in production environments with caution.

!!! info "Migrating from RingCentral MCP"
    If you previously used any of the telephony or messaging tools on the deprecated RingCentral MCP server, point your client at this endpoint instead. Tool names changed during the split — the generic dispatch tools (`gatekeeper_select_tool`, `platform_call_get_operation`, `platform_call_post_operation`, `platform_list_get_operations`, `platform_list_post_operations`) were removed in favor of dedicated, purpose-named tools. Common renames:

    | Old tool | New tool |
    |------|------|
    | `platform_read_user_call_log` | `list_user_call_log` |
    | `platform_list_messages` | `list_message_store_records` |
    | `platform_read_message` | `read_message_store_record` |
    | `platform_read_message_content` | `read_message_store_content` |
    | `platform_read_extension` / `profile_get_current_extension` | `read_extension_profile` |
    | `platform_read_unified_presence` | `read_user_presence` |
    | `platform_read_ai_notes` | `read_call_ai_notes` |
    | `platform_search_directory_entries` | `search_directory_entries` |

    Run `about_ringcentral_mcp_tools` for the authoritative current list.

---

## Connecting

See the [RingEx Phone Setup guide](ringex-phone-setup.md) for step-by-step instructions for Claude, ChatGPT, and Codex.

For other MCP clients (Cursor, etc.), add this server the same way you'd add any remote MCP server, using the endpoint above.

---

## Available tools

24 tools are available on this server.

| Tool | Requires CRM | Description |
|------|:---:|-------------|
| [`about_ringcentral_mcp_tools`](../tools/ringex-phone.md#about_ringcentral_mcp_tools) | — | List all available tools and permissions for this server |
| [`list_message_store_records`](../tools/ringex-phone.md#list_message_store_records) | — | List message-store records |
| [`list_user_call_log`](../tools/ringex-phone.md#list_user_call_log) | — | List user call log |
| [`message_store_create_smsmessage`](../tools/ringex-phone.md#message_store_create_smsmessage) | — | Send SMS |
| [`platform_get_account_info_v2`](../tools/ringex-phone.md#platform_get_account_info_v2) | — | Get account info |
| [`platform_list_administered_sites`](../tools/ringex-phone.md#platform_list_administered_sites) | — | List user administered sites |
| [`platform_list_answering_rules`](../tools/ringex-phone.md#platform_list_answering_rules) | — | List call handling rules |
| [`platform_list_contacts`](../tools/ringex-phone.md#platform_list_contacts) | — | List contacts |
| [`platform_list_directory_entries`](../tools/ringex-phone.md#platform_list_directory_entries) | — | Get company directory entries |
| [`platform_list_extension_phone_numbers`](../tools/ringex-phone.md#platform_list_extension_phone_numbers) | — | Get extension phone number list |
| [`platform_list_favorite_contacts`](../tools/ringex-phone.md#platform_list_favorite_contacts) | — | List favorite contacts |
| [`platform_read_call_recording`](../tools/ringex-phone.md#platform_read_call_recording) | — | Get call recording |
| [`platform_read_call_recording_content`](../tools/ringex-phone.md#platform_read_call_recording_content) | — | Get call recording content |
| [`platform_read_contact`](../tools/ringex-phone.md#platform_read_contact) | — | Get user contact(s) |
| [`platform_read_directory_entry`](../tools/ringex-phone.md#platform_read_directory_entry) | — | Get corporate directory entry |
| [`platform_read_user_call_record`](../tools/ringex-phone.md#platform_read_user_call_record) | — | Get user call record(s) |
| [`platform_read_user_presence_status`](../tools/ringex-phone.md#platform_read_user_presence_status) | — | Get user presence status |
| [`read_call_ai_notes`](../tools/ringex-phone.md#read_call_ai_notes) | — | Read call AI notes |
| [`read_extension_profile`](../tools/ringex-phone.md#read_extension_profile) | — | Read extension profile |
| [`read_message_store_content`](../tools/ringex-phone.md#read_message_store_content) | — | Read message-store content |
| [`read_message_store_record`](../tools/ringex-phone.md#read_message_store_record) | — | Read message-store record |
| [`read_user_presence`](../tools/ringex-phone.md#read_user_presence) | — | Read user presence |
| [`search_directory_entries`](../tools/ringex-phone.md#search_directory_entries) | — | Search directory entries |
| [`team_messaging_get_person`](../tools/ringex-phone.md#team_messaging_get_person) | — | Get Team Messaging person |

---

## Getting started

1. **Connect** — Add the server URL above to your AI client.
2. **Verify** — Ask your assistant to show your recent call log to confirm the connection is active.
3. **Use** — Ask your AI assistant to look up calls, voicemails, SMS, or AI-generated call notes. Tool names differ from the deprecated server — see the migration note above.

---

## Tool discovery

```bash
curl https://mcp.labs.ringcentral.com/ringex/phone \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}'
```
