# RingEX Meetings — Tools Reference

Full reference for every tool available on the [RingEX Meetings](../servers/ringex-meetings.md) server. Eight tools cover meeting history, meeting artifacts (transcript, chat, recording), and reusable meeting spaces.

Tools are listed alphabetically — use the on-page navigation ("On this page") to jump to a specific tool.

!!! warning "Experimental server"
    RingEX Meetings is experimental. Tool names and input schemas may change without the usual notice period. Treat the tables below as guidance and call `tools/list` for the authoritative schema.

!!! tip "Exact schemas live in `tools/list`"
    The tables below document every parameter and what it does, but the authoritative required/optional fields, enums, and bounds for a given tool are always visible by calling `tools/list` on the server.

---

## about_ringcentral_mcp_tools

Call this first when you want to know what a RingEX MCP server can do, what tools are available, or which RingCentral tasks are supported. Returns a concise overview of the available tool categories and representative tool names for the connected server.

**Available on:** [RingEX Phone](../servers/ringex-phone.md) · [RingEX Chat](../servers/ringex-chat.md) · [RingEX Admin](../servers/ringex-admin.md) · [RingEX Meetings](../servers/ringex-meetings.md)  
**Access:** Read-only

---

### Parameters

This tool takes no parameters.

---

### Returns

| Field | Type | Description |
|-------|------|-------------|
| `summary` | `string` | A short description of what the connected server can help with. On RingEX Meetings, this notes that the server exposes RingCentral Platform API meeting operations, scoped to the tools enabled for the current endpoint. |
| `categories` | `array` | A list of capability categories, each with: `category` (name), `examples` (example use cases), and `representativeTools` (a sample of tool names in that category). RingEX Meetings returns a single category, which the server currently labels `Video`. |
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
    Run this tool right after connecting a new RingEX server to confirm which capabilities and tools are exposed, before calling `tools/list` for exact schemas.

---

## create_meeting_space

Creates a reusable, date- and time-agnostic RingCentral meeting space for the authenticated user, and returns a participant join URL.

**Server:** [RingEX Meetings](../servers/ringex-meetings.md)  
**Access:** Write

!!! note "Not a calendar invitation"
    This tool creates a standing meeting space only. It does **not** schedule a calendar event and does **not** send invitations to anyone. Distributing the returned join URL is up to you.

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `name` | — | A name for the meeting space, 1–256 characters. Omit it to create an unnamed space. |

---

### Returns

The created meeting space, including its identifier and a participant join URL. Use the returned bridge identifier with [`delete_meeting_space`](#delete_meeting_space) if you later want to remove it.

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "create_meeting_space",
        "arguments": { "name": "Platform API office hours" }
      }
    }
    ```

=== "Claude prompt"

    ```
    Create a reusable RingCentral meeting space called "Platform API office hours"
    and give me the join link.
    ```

---

## delete_meeting_space

Deletes one reusable RingCentral meeting space owned by the authenticated user, behind a two-step confirmation gate.

**Server:** [RingEX Meetings](../servers/ringex-meetings.md)  
**Access:** Write

!!! warning "Two-step confirmation required"
    Call `action: "preview"` first and show the resolved space to the user. Only after explicit approval, call `action: "confirm"` with the short-lived `confirmationToken` returned by the preview and the **same** `bridgeId`. Your Personal Meeting ID (PMI) and spaces you don't own are always refused.

---

### Supported actions

The input is a strict discriminated union — select exactly one variant and do not mix fields between them.

| Action | Required | Optional | Notes |
|--------|----------|----------|-------|
| `preview` | `bridgeId` | *(none)* | Resolves the space and returns it along with a short-lived `confirmationToken`. Deletes nothing. |
| `confirm` | `bridgeId`, `confirmationToken` | *(none)* | Performs the deletion. The `bridgeId` must match the one used in the preview. |

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `action` | ✅ | Either `preview` or `confirm`. |
| `bridgeId` | ✅ | A RingCentral meeting or bridge identifier returned by a RingEX Meetings tool. 1–256 characters. |
| `confirmationToken` | — | Required for `action: "confirm"` only. The short-lived UUID returned by `preview` for this exact bridge. |

---

### Examples

=== "1. Preview"

    ```json
    {
      "action": "preview",
      "bridgeId": "br-7f21c9"
    }
    ```

=== "2. Confirm"

    ```json
    {
      "action": "confirm",
      "bridgeId": "br-7f21c9",
      "confirmationToken": "3f2a1b4c-5d6e-4f70-8a9b-0c1d2e3f4a5b"
    }
    ```

=== "Claude prompt"

    ```
    Delete my "Platform API office hours" meeting space — show me what you're
    about to delete first.
    ```

---

## get_meeting_chat

Gets bounded main-room chat text for one accessible past RingCentral meeting. The tool verifies meeting access, reads only the trusted RingCentral media chat resource, and never returns the private chat URL.

**Server:** [RingEX Meetings](../servers/ringex-meetings.md)  
**Access:** Read-only

!!! note "Main room only"
    This returns the main-room chat. Breakout room chat and direct messages exchanged during the meeting are not included.

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `meetingId` | ✅ | Meeting id returned by [`search_meeting_history`](#search_meeting_history). 1–256 characters. |
| `maxCharacters` | — | Maximum characters of chat text to return. Minimum `1000`, maximum `50000`, default `20000`. Longer chats are truncated at this boundary. |

---

### Returns

The main-room chat text for the meeting, truncated to `maxCharacters`. The private chat resource URL is never included in the response.

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "get_meeting_chat",
        "arguments": {
          "meetingId": "mtg-4821",
          "maxCharacters": 20000
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Pull the chat from yesterday's platform sync — did anyone drop a link in it?
    ```

---

## get_meeting_recording

Returns one bounded RingCentral meeting recording as a native MCP binary resource. Recording bytes and protected media URLs are never copied into structured JSON.

**Server:** [RingEX Meetings](../servers/ringex-meetings.md)  
**Access:** Read-only

!!! note "One recording per call"
    If a meeting has multiple recordings, the first call tells you which `recordingId` values exist. Call again with a single `recordingId` to fetch a specific one.

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `meetingId` | ✅ | Meeting id returned by [`search_meeting_history`](#search_meeting_history). 1–256 characters. |
| `recordingId` | — | A specific recording to fetch, when the meeting has more than one. 1–256 characters. |
| `maxBytes` | — | Maximum bytes to return. Minimum `1024`, maximum and default `8388608` (8 MiB). |
| `passcode` | — | Passcode for a meeting that requires one. 1–256 characters. |
| `publicMeetingId` | — | Public meeting identifier, when accessing the meeting via its public id. Up to 2048 characters. |

---

### Returns

The recording as a native MCP binary resource, capped at `maxBytes`. Protected media URLs are not returned.

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "get_meeting_recording",
        "arguments": { "meetingId": "mtg-4821" }
      }
    }
    ```

=== "Claude prompt"

    ```
    Get me the recording of my 2pm meeting yesterday.
    ```

---

## get_meeting_summary

Gets bounded details for one accessible RingCentral meeting. Returns the summary embedded in meeting details, participant context, and artifact availability — without fetching transcript, chat, recording, insight, or CES Generated Notes content.

**Server:** [RingEX Meetings](../servers/ringex-meetings.md)  
**Access:** Read-only

!!! tip "Check availability before fetching"
    This is the cheapest way to find out whether a meeting actually has a transcript, chat, or recording. Call it before reaching for [`get_meeting_transcript`](#get_meeting_transcript), [`get_meeting_chat`](#get_meeting_chat), or [`get_meeting_recording`](#get_meeting_recording).

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `meetingId` | ✅ | Meeting id returned by [`search_meeting_history`](#search_meeting_history). 1–256 characters. |

---

### Returns

Meeting details including the embedded summary, participant context, and which artifacts are available for the meeting. Artifact *content* is never included — fetch it with the dedicated tool.

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "get_meeting_summary",
        "arguments": { "meetingId": "mtg-4821" }
      }
    }
    ```

=== "Claude prompt"

    ```
    Who was on the platform sync yesterday, and does it have a transcript?
    ```

---

## get_meeting_transcript

Gets bounded post-meeting Live Transcript text for one accessible RingCentral meeting. The tool requests only transcription material, follows trusted expiring RingCentral content links, and omits signed URLs, tokens, and unrelated participant metadata.

**Server:** [RingEX Meetings](../servers/ringex-meetings.md)  
**Access:** Read-only

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `meetingId` | ✅ | Meeting id returned by [`search_meeting_history`](#search_meeting_history). 1–256 characters. |
| `maxCharacters` | — | Maximum characters of transcript text to return. Minimum `1000`, maximum `50000`, default `20000`. Long meetings are truncated at this boundary. |
| `passcode` | — | Passcode for a meeting that requires one. 1–256 characters. |
| `publicMeetingId` | — | Public meeting identifier, when accessing the meeting via its public id. Up to 2048 characters. |

---

### Returns

Live Transcript text for the meeting, truncated to `maxCharacters`. Signed URLs, tokens, and unrelated participant metadata are omitted.

---

### Example

=== "MCP JSON-RPC"

    ```json
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "get_meeting_transcript",
        "arguments": {
          "meetingId": "mtg-4821",
          "maxCharacters": 50000
        }
      }
    }
    ```

=== "Claude prompt"

    ```
    Get the transcript of my platform sync and pull out the action items.
    ```

---

## search_meeting_history

Searches one bounded page of the authenticated user's accessible past meetings. Returns compact metadata and artifact availability only — never transcript, Generated Notes, chat, or recording content.

**Server:** [RingEX Meetings](../servers/ringex-meetings.md)  
**Access:** Read-only

!!! note "Start here"
    This is the entry point for every read workflow on this server. The `meetingId` values it returns are what the other read tools take. Use [`get_meeting_summary`](#get_meeting_summary) once you've selected a meeting.

---

### Parameters

| Parameter | Required | Description |
|-----------|:--------:|-------------|
| `dateFrom` | ✅ | Inclusive beginning of the meeting-history window, as an ISO 8601 date-time (e.g. `2026-10-01T00:00:00Z`). |
| `dateTo` | ✅ | Inclusive end of the meeting-history window, as an ISO 8601 date-time. |
| `text` | — | Free-text search across the meetings in the window. 1–256 characters. |
| `materials` | — | Filter to meetings that produced a given artifact. One of `Recordings` or `Notes`. |
| `pageSize` | — | Results per page. Minimum `1`, maximum `50`, default `25`. |
| `pageToken` | — | Token from a previous response, to fetch the next page. Up to 2048 characters. |

!!! tip "Both dates are required"
    `dateFrom` and `dateTo` are mandatory by design — the tool will not scan your entire meeting history. Narrow the window first, then page through it.

---

### Returns

One page of meetings, each with compact metadata and artifact availability, plus a page token for fetching the next page when more results exist. No artifact content is returned — not transcript, Generated Notes, chat, or recording. Call `tools/list` for the exact response shape.

---

### Examples

=== "Last 7 days"

    ```json
    {
      "dateFrom": "2026-10-06T00:00:00Z",
      "dateTo": "2026-10-13T23:59:59Z"
    }
    ```

=== "Only meetings with recordings"

    ```json
    {
      "dateFrom": "2026-09-01T00:00:00Z",
      "dateTo": "2026-10-13T23:59:59Z",
      "materials": "Recordings",
      "pageSize": 50
    }
    ```

=== "Text search"

    ```json
    {
      "dateFrom": "2026-09-01T00:00:00Z",
      "dateTo": "2026-10-13T23:59:59Z",
      "text": "roadmap review"
    }
    ```

=== "Claude prompt"

    ```
    Find my meetings from the last two weeks that have recordings.
    ```

---

[← Back to RingEX Meetings](../servers/ringex-meetings.md)
