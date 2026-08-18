---
name: fax-inbox
description: Presents the authenticated RingEX Phone user's fax inbox as a clickable list of recent faxes, then reads back the selected fax's sender, time, and cover-page text when available. Excludes SMS and voicemail, and cannot retrieve the fax document body itself. Use when the user asks to see their faxes, check for a new fax, or find out who sent a fax.
---

<!-- --8<-- [start:body] -->
# Fax Inbox

## Goal

Give the user a browsable view of recent faxes — who sent one, when, and any cover-page text —
without making them dig through a phone app. This skill has a hard limitation worth stating
up front: no tool on this server can retrieve or OCR the actual fax document content, only
metadata and cover-page text. Be upfront about that rather than implying more access than exists.

## Trigger examples

- "Do I have any new faxes?"
- "Show me my fax inbox."
- "Who sent that fax this morning?"
- "Any faxes from this week I haven't seen?"

## Scope boundary

- Fax only. Never include SMS or voicemail records, even if the user says "messages" generically —
  if they explicitly ask for SMS or voicemail, say this skill doesn't cover that and point to
  `sms-inbox` or `voicemail-inbox` instead of quietly including it.
- Read-only. This skill never deletes, marks read/unread, or forwards a fax — there is no tool
  exposed on this server for those actions.
- **Cannot read the fax document itself.** `get_my_message_detail` never returns attachment ids,
  URIs, or binary/base64 content, and `get_my_communication_inbox`'s `keyword` filter only matches
  fax cover-page text — it does not search the fax PDF/OCR content. If the user wants the actual
  document contents, say plainly that this skill only surfaces metadata and cover-page text, and
  suggest they open the fax directly in the RingCentral app or online account.

## Workflow

1. **Pull recent fax activity.** Call `get_my_communication_inbox` with `messageTypes: ["Fax"]`
   (SMS and voicemail are separate `messageTypes` values and must not be requested). Default the
   window to the last 14 days unless the user asks for a different range, and pass
   `readStatus: "Unread"` only if the user specifically asked for unread/new faxes.

2. **Resolve sender names.** For each fax's sender number, try `search_my_contacts` (personal
   address book) then `resolve_directory_person` (company directory); fall back to the raw phone
   number if neither resolves.

3. **Sort and present as a choice.** Sort newest first.
      - If there are 2–4 recent faxes, use a structured multiple-choice prompt (the
        `AskUserQuestion` tool, where available): one option per fax, labeled with the resolved
        sender name, with the timestamp (and page count, if the record includes one) as the
        description.
      - If there are more than 4, or fewer than 2 (zero or one), list them as a plain-text ranked
        list instead — a multiple-choice prompt can't show more than 4 options, and a single fax
        doesn't need a picker at all (just confirm and proceed to step 4).
      - If nothing was found in the window, say so and offer to check a wider date range instead of
        guessing at prior activity.

4. **Fetch the selected fax's detail.** Take the `messageId` of the chosen fax and call
   `get_my_message_detail`. This returns metadata and, if the fax had one, cover-page text — never
   the document's page images, PDF, or OCR'd body text.

5. **Render the result.** Show the sender (resolved name or raw number), the timestamp, and the
   cover-page text if present. If there's no cover-page text, say so plainly, and remind the user
   this skill can't surface the fax's actual document content — that requires opening it directly
   in RingCentral.

## Guidance

- Never invent a fax's sender, timestamp, or cover-page text — if a field is missing, say it's
  unavailable.
- Never imply the fax document itself was read, summarized, or searched — only metadata and
  cover-page text are ever available through this skill.
- Never fold SMS or voicemail into this view.
<!-- --8<-- [end:body] -->
