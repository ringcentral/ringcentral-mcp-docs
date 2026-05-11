# Changelog

All notable changes to RingCentral MCP servers are documented here.  
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [Unreleased]

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
