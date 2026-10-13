# RingEX Meetings

<div class="rc-spec-sheet">
<div class="rc-spec-row"><span class="rc-spec-row__label">Endpoint</span><span class="rc-spec-row__value"><code>https://mcp.labs.ringcentral.com/ringex/video</code><button class="rc-copy" data-copy="https://mcp.labs.ringcentral.com/ringex/video" aria-label="Copy endpoint URL" title="Copy endpoint URL"><svg class="rc-copy__icon--copy" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg><svg class="rc-copy__icon--check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg></button></span></div>
<div class="rc-spec-row"><span class="rc-spec-row__label">Status</span><span class="rc-spec-row__value"><span class="rc-status rc-status--experimental">Experimental</span></span></div>
<div class="rc-spec-row"><span class="rc-spec-row__label">Transport</span><span class="rc-spec-row__value">SSE over HTTPS</span></div>
<div class="rc-spec-row"><span class="rc-spec-row__label">Auth</span><span class="rc-spec-row__value">OAuth2</span></div>
</div>

!!! warning "Experimental server"
    RingEX Meetings is an experimental server. Its endpoint, tool names, and input schemas may change — or the server may be withdrawn — without the 14-day notice period described in the [deprecation policy](../changelog.md#deprecation-policy). Don't build production integrations against it yet. Call `tools/list` at runtime rather than hard-coding the tool surface.

!!! note "Endpoint path still says `video`"
    The server is named RingEX Meetings, but it is deployed at `…/ringex/video`. Use the endpoint exactly as shown above — `…/ringex/meetings` is not a valid URL.

---

## About

RingEX Meetings gives your AI assistant access to RingCentral Meetings: your past meeting history, the artifacts those meetings produced — Live Transcript text, main-room chat, and recordings — and reusable meeting spaces you can create and delete.

It joins [RingEX Phone](ringex-phone.md), [RingEX Chat](ringex-chat.md), and [RingEX Admin](ringex-admin.md) in the RingEX family. The split is by communication mode: Phone covers telephony and the message store, Chat covers Team Messaging (Glip), Admin covers account administration, and Meetings covers video meetings.

Every tool is scoped to the authenticated user. There are no account-wide or admin selectors on this server — you see the meetings you have access to, and nothing else.

See the [Changelog](../changelog.md) for what's changed across versions.

---

## Connecting

See the [RingEX Meetings Setup guide](ringex-meetings-setup.md) for step-by-step instructions for Claude, ChatGPT, and Codex.

For other MCP clients (Cursor, etc.), add this server the same way you'd add any remote MCP server, using the endpoint above.

---

## Available tools

8 tools are available on this server — six read tools and two write tools. Reads are bounded: history is returned one page at a time, and transcript, chat, and recording tools each cap how much content they return per call.

| Tool | Access | Description |
|------|:---:|-------------|
| [`about_ringcentral_mcp_tools`](../tools/ringex-meetings.md#about_ringcentral_mcp_tools) | Read | List all available tools and permissions for this server |
| [`create_meeting_space`](../tools/ringex-meetings.md#create_meeting_space) | Write | Create a reusable, time-agnostic meeting space and return its join URL |
| [`delete_meeting_space`](../tools/ringex-meetings.md#delete_meeting_space) | Write | Delete a meeting space you own, via a two-step preview/confirm gate |
| [`get_meeting_chat`](../tools/ringex-meetings.md#get_meeting_chat) | Read | Get main-room chat text for one past meeting |
| [`get_meeting_recording`](../tools/ringex-meetings.md#get_meeting_recording) | Read | Return one recording as a native MCP binary resource |
| [`get_meeting_summary`](../tools/ringex-meetings.md#get_meeting_summary) | Read | Get details, participant context, and artifact availability for one meeting |
| [`get_meeting_transcript`](../tools/ringex-meetings.md#get_meeting_transcript) | Read | Get post-meeting Live Transcript text for one meeting |
| [`search_meeting_history`](../tools/ringex-meetings.md#search_meeting_history) | Read | Search one page of your past meetings, returning metadata only |

---

## How the tools fit together

The read tools are designed to be used in sequence, and the split is deliberate: searching your history should never drag transcript or recording content into the conversation.

1. **`search_meeting_history`** finds candidate meetings in a date range and returns compact metadata plus *artifact availability* — which meetings have recordings or notes. It never returns transcript, chat, or recording content.
2. **`get_meeting_summary`** takes one `meetingId` from that result and returns details, participant context, and the summary embedded in the meeting record — still without fetching the heavier artifacts.
3. **`get_meeting_transcript`**, **`get_meeting_chat`**, and **`get_meeting_recording`** fetch one artifact each, for one meeting, on demand.

So the normal path is search → summary → fetch one artifact. Start with a narrow date range rather than a wide one; `dateFrom` and `dateTo` are both required on `search_meeting_history` for exactly this reason.

---

## Content handling

These tools read material from RingCentral media endpoints, which is handled with a few deliberate constraints:

- **Signed URLs are never returned.** The transcript, chat, and recording tools follow trusted expiring RingCentral content links server-side and return the content itself. Private chat URLs, protected media URLs, and access tokens are not copied into the response.
- **Recording bytes stay binary.** `get_meeting_recording` returns a native MCP binary resource, not base64 embedded in structured JSON, and caps at 8 MiB per call.
- **Text is truncated, not silently dropped.** `get_meeting_transcript` and `get_meeting_chat` default to 20,000 characters and allow up to 50,000. Long meetings will be cut off at that boundary.

!!! note "Meeting artifacts aren't always present"
    Transcript, chat, and recording content only exists if those features were enabled and the meeting actually produced them. Check artifact availability in `search_meeting_history` or `get_meeting_summary` before fetching — it saves a round trip on meetings that have nothing to return.

---

## Write tools

Two tools on this server have side effects, and both are narrower than they first appear.

`create_meeting_space` creates a **reusable, date- and time-agnostic meeting space** — the RingCentral Meetings equivalent of a standing room. It returns a participant join URL. It does *not* schedule a calendar event and does *not* send invitations to anyone; distributing the join URL is up to you.

`delete_meeting_space` is gated behind a two-step confirmation. Call it with `action: "preview"` first, show the resolved space to the user, and only after explicit approval call `action: "confirm"` with the short-lived `confirmationToken` the preview returned. It refuses to delete your Personal Meeting ID (PMI) and refuses spaces you don't own.

---

## Getting started

1. **Connect** — Add the server URL above to your AI client.
2. **Verify** — Ask your assistant to list your meetings from the last week to confirm the connection is active.
3. **Use** — Ask your AI assistant to recap a meeting, pull its transcript or chat, or create a reusable meeting space.

---

## Tool discovery

```bash
curl https://mcp.labs.ringcentral.com/ringex/video \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}'
```
