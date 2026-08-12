# RingEX Phone

**Endpoint:** `https://mcp.labs.ringcentral.com/ringex/v1.1.0/phone`  
**Status:** 🟡 Labs / Beta · Updated  
**Transport:** SSE over HTTPS

---

## About

RingEX Phone gives your AI assistant access to telephony data: call activity and AI-generated call insights, messages (SMS, voicemail, and fax) from the message store, directory/contact lookup, and the user's own phone profile. It's one of three servers that replace the original monolithic RingCentral MCP server — this one covers the phone and messaging side.

!!! info "v1.1.0 — tool surface consolidated"
    This server's 24 fine-grained `platform_*`/`read_*`/`list_*` tools have been replaced with 12 workflow-oriented, personal-scope tools: `get_my_phone`, `resolve_directory_person`, `search_my_contacts`, `get_my_call_activity`, `get_my_call_insight`, `get_my_call_recording_metadata`, `search_my_call_insights`, `get_my_communication_inbox`, `get_my_message_detail`, `get_my_sms_thread`, `send_sms`, plus `about_ringcentral_mcp_tools`. Every tool is scoped to the authenticated user only — account, extension, and pagination selectors are no longer exposed as parameters.

!!! warning "Labs status"
    This server is part of RingCentral Labs and is not covered by RingCentral's standard SLA. Tools may be renamed, modified, or removed without prior notice. Use in production environments with caution.

---

## Connecting

**ChatGPT users:** the fastest way to get started is the official [RingCentral Phone plugin](https://chatgpt.com/plugins/plugin_asdk_app_6a5163accce48191ab3fac53d63cb197?q=ringcentral) — install it and authorize with RingCentral, no manual server setup needed.

See the [RingEX Phone Setup guide](ringex-phone-setup.md) for step-by-step instructions for Claude, ChatGPT, and Codex (including how to side-load the server manually if you can't use the plugin).

For other MCP clients (Cursor, etc.), add this server the same way you'd add any remote MCP server, using the endpoint above.

---

## Available tools

12 tools are available on this server — down from 24 prior to v1.1.0. All tools operate on the authenticated user's own data; see the [Tools reference](../tools/ringex-phone.md) for full parameter details.

| Tool | Access | Description |
|------|:---:|-------------|
| [`about_ringcentral_mcp_tools`](../tools/ringex-phone.md#about_ringcentral_mcp_tools) | Read | List all available tools and permissions for this server |
| [`get_my_phone`](../tools/ringex-phone.md#get_my_phone) | Read | Get my extension number, phone numbers, presence, business hours, and call-handling rules |
| [`resolve_directory_person`](../tools/ringex-phone.md#resolve_directory_person) | Read | Resolve a person in the company directory by name, department, or job title |
| [`search_my_contacts`](../tools/ringex-phone.md#search_my_contacts) | Read | Search my personal address book by name or phone number |
| [`get_my_call_activity`](../tools/ringex-phone.md#get_my_call_activity) | Read | Get my call activity for a date range — recent/missed/returned calls, talk time, callbacks |
| [`get_my_call_insight`](../tools/ringex-phone.md#get_my_call_insight) | Read | Get AI notes and transcript text for one of my calls |
| [`get_my_call_recording_metadata`](../tools/ringex-phone.md#get_my_call_recording_metadata) | Read | Check whether one of my calls has recording metadata |
| [`search_my_call_insights`](../tools/ringex-phone.md#search_my_call_insights) | Read | Search my calls by person, topic, and date window |
| [`get_my_communication_inbox`](../tools/ringex-phone.md#get_my_communication_inbox) | Read | Get my SMS, voicemail, and fax records for a date window |
| [`get_my_message_detail`](../tools/ringex-phone.md#get_my_message_detail) | Read | Read one SMS, voicemail, or fax record |
| [`get_my_sms_thread`](../tools/ringex-phone.md#get_my_sms_thread) | Read | Get a bounded window of one SMS conversation |
| [`send_sms`](../tools/ringex-phone.md#send_sms) | Write | Send one SMS from a number I own |

!!! note "Company directory management moved"
    `platform_list_directory_entries`, `platform_read_directory_entry`, and `search_directory_entries` are replaced by `resolve_directory_person`, which is read-only lookup/resolution scoped to finding a person to call or text — not directory administration. `team_messaging_get_person` is no longer exposed here; use [RingEX Chat](ringex-chat.md)'s `find_person` for Team Chat person resolution.

---

## Getting started

1. **Connect** — Add the server URL above to your AI client.
2. **Verify** — Ask your assistant to show your recent call log to confirm the connection is active.
3. **Use** — Ask your AI assistant to look up calls, voicemails, SMS, or AI-generated call notes.

---

## Tool discovery

```bash
curl https://mcp.labs.ringcentral.com/ringex/v1.1.0/phone \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}'
```
