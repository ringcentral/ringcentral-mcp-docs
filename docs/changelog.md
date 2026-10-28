# Changelog

All notable changes to RingCentral MCP servers are documented here.

---

## [Unreleased]

### All RingEX servers — Removed
- `about_ringcentral_mcp_tools` has been removed from RingEX Phone, Chat, Meetings, and Admin. Call `tools/list` to enumerate the tools and schemas a server exposes.
- Tool counts are now 11 (Phone), 8 (Chat), 7 (Meetings), and 31 (Admin).

### RingEX Admin — Added
- Five read-only tools for company calls and recording: `read_company_call_log`, `read_company_active_calls`, `read_company_call_analytics`, `read_company_call_recordings`, and `read_call_recording_settings`. See the [RingEX Admin tools reference](tools/ringex-admin.md).

### RingEX Meetings — Added (Experimental)
- New experimental server published at `https://mcp.labs.ringcentral.com/ringex/video`, covering RingCentral Meetings. It joins RingEX Phone, Chat, and Admin as the fourth server in the RingEX family, split by communication mode. Note that the endpoint path is `/ringex/video`, not `/ringex/meetings`.
- 7 tools: `search_meeting_history`, `get_meeting_summary`, `get_meeting_transcript`, `get_meeting_chat`, `get_meeting_recording`, `create_meeting_space`, and `delete_meeting_space`.
- All tools are scoped to the authenticated user — there are no account-wide or admin selectors on this server.
- Reads are bounded and layered: `search_meeting_history` requires both `dateFrom` and `dateTo` and returns metadata plus artifact availability only; transcript and chat cap at 50,000 characters (default 20,000); recordings cap at 8 MiB and are returned as native MCP binary resources rather than base64 in JSON.
- Signed URLs, access tokens, and protected media URLs are never returned — artifact tools follow trusted expiring RingCentral content links server-side and return only the content.
- `delete_meeting_space` requires a two-step `preview` → `confirm` flow with a short-lived `confirmationToken`, and refuses PMI and non-owned spaces.
- `create_meeting_space` creates a reusable, time-agnostic space and returns a join URL — it does not schedule a calendar event or send invitations.
- **Experimental:** the endpoint, tool names, and input schemas may change, or the server may be withdrawn, without the 14-day notice described in the deprecation policy below. See the [RingEX Meetings server docs](servers/ringex-meetings.md).

### RingEX Phone — Changed (v1.1.0)
- Endpoint moved to `https://mcp.labs.ringcentral.com/ringex/phone` (simplified from versioned URL).
- Tool surface consolidated from 24 tools down to 12: `about_ringcentral_mcp_tools`, `get_my_phone`, `resolve_directory_person`, `search_my_contacts`, `get_my_call_activity`, `get_my_call_insight`, `get_my_call_recording_metadata`, `search_my_call_insights`, `get_my_communication_inbox`, `get_my_message_detail`, `get_my_sms_thread`, and `send_sms`. All previous `platform_*`/`read_*`/`list_*` tools were removed.
- Every tool is now scoped to the authenticated user only — account, extension, and pagination selectors are no longer exposed as parameters.
- `resolve_directory_person` is new — replaces `platform_list_directory_entries`, `platform_read_directory_entry`, and `search_directory_entries` with read-only lookup/resolution scoped to finding a person to call or text.
- `team_messaging_get_person` is no longer exposed here; use RingEX Chat's `find_person` for Team Chat person resolution.
- `send_sms` requires host-side confirmation of sender, recipient, and exact text before sending, and rejects retries that reuse a `requestId`.
- See the [RingEX Phone server docs](servers/ringex-phone.md#deprecated-tools) for the complete list of deprecated tools and their replacements.

### RingEX Chat — Changed (v1.1.0)
- Endpoint moved to `https://mcp.labs.ringcentral.com/ringex/v1.1.0/team-chat`.
- Tool surface consolidated from 65 tools down to 9: `about_ringcentral_mcp_tools`, `find_person`, `read_team_chat`, `send_post`, `manage_post`, `manage_adaptive_card`, `manage_team`, `manage_chat_item`, and `manage_incoming_webhook`. The 64 previous `team_messaging_*`/`open_team_messaging_conversation`/`upload_team_messaging_file`/`send_team_messaging_post` tools were removed.
- Write tools now take a `resource`/`action` (or `action`-only) discriminator instead of one tool per operation.
- `find_person` is new — resolves a person by name, email, extension, phone number, or exact Team Chat person ID.
- `team_messaging_create_data_export_task`, `_get_data_export_task`, and `_list_data_export_tasks` moved to RingEX Admin.

### RingEX Phone, Chat, Admin — Added
- Three new servers published, replacing the monolithic RingCentral MCP server:
  - **RingEX Phone** — `https://mcp.labs.ringcentral.com/ringex/phone` (call log, AI call notes, SMS/fax/voicemail messages)
  - **RingEX Chat** — `https://mcp.labs.ringcentral.com/ringex/team-chat` (Team Messaging / Glip)
  - **RingEX Admin** — `https://mcp.labs.ringcentral.com/ringex/admin` (tool discovery, generic operations, extension, presence, directory)
- Tool names changed as part of the split: generic dispatch tools (`gatekeeper_select_tool`, `platform_call_get_operation`, `platform_call_post_operation`, `platform_list_get_operations`, `platform_list_post_operations`) were removed in favor of dedicated, purpose-named tools, and Glip tools were renamed to the `team_messaging_*` convention.

### RingCentral MCP — Removed
- The deprecated monolithic `https://mcp.labs.ringcentral.com/ringex` server and its documentation have been removed. Use RingEX Phone, Chat, and Admin above instead.

### App Connect
- `findContactByPhone` — improve phone number normalisation for international formats
- `rcGetCallLogs` — add support for filtering by call direction (`Inbound` / `Outbound`)

---

## [1.1.0] — 2025-04-15

### App Connect — Added
- **`createContact`** — create new CRM contacts directly from an AI conversation
- **`findContactByPhone`** — look up CRM contacts by phone number (complements `findContactByName`)
- **`getPublicConnectors`** — list available CRM connector integrations

### App Connect — Changed
- `createCallLog` now accepts `incomingData.logInfo` as a direct pass-through from `rcGetCallLogs` records

---

## [1.0.0] — 2025-03-01

### App Connect — Initial release
- `getSessionInfo`
- `getHelp`
- `findContactByName`
- `createCallLog`
- `rcGetCallLogs`
- `logout`

### RingCentral MCP — Initial release
- Server published at `https://mcp.labs.ringcentral.com`
- Tool discovery endpoint active

---

## Deprecation policy

- Tools will be marked **deprecated** in the changelog and tool description at least **30 days** before removal.
- Breaking parameter changes will be announced with a **14-day** notice.
- Deprecated tools return a `deprecation_warning` field in their response.
