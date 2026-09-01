# RingEX Phone

<div class="rc-spec-sheet">
<div class="rc-spec-row"><span class="rc-spec-row__label">Endpoint</span><span class="rc-spec-row__value"><code>https://mcp.labs.ringcentral.com/ringex/v1.1.0/phone</code><button class="rc-copy" data-copy="https://mcp.labs.ringcentral.com/ringex/v1.1.0/phone" aria-label="Copy endpoint URL" title="Copy endpoint URL"><svg class="rc-copy__icon--copy" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg><svg class="rc-copy__icon--check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg></button></span></div>
<div class="rc-spec-row"><span class="rc-spec-row__label">Status</span><span class="rc-spec-row__value"><span class="rc-status rc-status--preview">Preview</span></span></div>
<div class="rc-spec-row"><span class="rc-spec-row__label">Transport</span><span class="rc-spec-row__value">SSE over HTTPS</span></div>
<div class="rc-spec-row"><span class="rc-spec-row__label">Auth</span><span class="rc-spec-row__value">OAuth2</span></div>
</div>

---

## About

RingEX Phone gives your AI assistant access to telephony data: call activity and AI-generated call insights, messages (SMS, voicemail, and fax) from the message store, directory/contact lookup, and the user's own phone profile. It's one of three servers that replace the original monolithic RingCentral MCP server — this one covers the phone and messaging side.

See the [Changelog](../changelog.md) for what's changed across versions.

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
