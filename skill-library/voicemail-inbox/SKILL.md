---
name: voicemail-inbox
description: Presents the authenticated RingEX Phone user's voicemail inbox as a clickable list of recent messages, then reads back the selected voicemail's caller, time, and verified transcription when available. Excludes SMS and fax. Use when the user asks to see their voicemails, check for new voicemail, read a voicemail transcript, or catch up on missed voicemail.
---

<!-- --8<-- [start:body] -->
# Voicemail Inbox

## Goal

Give the user a browsable view of recent voicemails — who called, when, and what they said —
without making them dig through a phone app. This is read-only and text-based: there is no audio
playback, only the message's metadata and, when available, a verified transcription.

## Trigger examples

- "Do I have any new voicemails?"
- "Show me my voicemail inbox."
- "Read me that voicemail from earlier today."
- "Any unread voicemail from this week?"
- "What did Sarah say in her voicemail?"

## Scope boundary

- Voicemail only. Never include SMS or fax records, even if the user says "messages" generically —
  if they explicitly ask for SMS or fax, say this skill doesn't cover that and point to `sms-inbox`
  or `fax-inbox` instead of quietly including it.
- Read-only. This skill never deletes, marks read/unread, or replies to a voicemail — there is no
  tool exposed on this server for those actions.
- Text-based only. There is no audio playback tool — never imply the assistant "played" anything;
  it read the transcription.

## Workflow

1. **Pull recent voicemail activity.** Call `get_my_communication_inbox` with
   `messageTypes: ["VoiceMail"]` (SMS and fax are separate `messageTypes` values and must not be
   requested). Default the window to the last 14 days unless the user asks for a different range,
   and pass `readStatus: "Unread"` only if the user specifically asked for unread/new voicemail.

2. **Resolve caller names.** For each voicemail's sender number, try `search_my_contacts`
   (personal address book) then `resolve_directory_person` (company directory); fall back to the
   raw phone number if neither resolves.

3. **Sort and present as a choice.** Sort newest first.
      - If there are 2–4 recent voicemails, use a structured multiple-choice prompt (the
        `AskUserQuestion` tool, where available): one option per voicemail, labeled with the
        resolved caller name, with the timestamp (and duration, if the record includes one) as the
        description.
      - If there are more than 4, or fewer than 2 (zero or one), list them as a plain-text ranked
        list instead — a multiple-choice prompt can't show more than 4 options, and a single
        voicemail doesn't need a picker at all (just confirm and proceed to step 4).
      - If nothing was found in the window, say so and offer to check a wider date range instead of
        guessing at prior activity.

4. **Fetch the selected voicemail's detail.** Take the `messageId` of the chosen voicemail and
   call `get_my_message_detail`. This may return a verified transcription; it never returns
   attachment ids, URIs, or audio/binary content.

5. **Render the result.** Show the caller (resolved name or raw number), the timestamp, and the
   transcription text if one came back. If no transcription is available for that voicemail, say
   so plainly rather than guessing at the content or leaving the field blank without explanation.

6. **Offer to continue.** If the user was checking unread voicemail and more than one came back,
   offer to go through them one at a time rather than dumping every transcription at once.

## Guidance

- Never invent a voicemail's caller, timestamp, or transcription content — if a field is missing,
  say it's unavailable.
- Never fold SMS or fax into this view, and never claim to have played audio — this skill only
  reads text-based metadata and transcription.
- Keep the voicemail list step fast and skimmable; save full transcription rendering for after a
  voicemail is chosen.
<!-- --8<-- [end:body] -->
