# Changelog

All notable changes to RingCentral MCP servers are documented here.  
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [Unreleased]

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
