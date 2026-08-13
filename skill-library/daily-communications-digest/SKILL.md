---
name: daily-communications-digest
description: Produces a daily RingEX Phone communications digest from recent calls, SMS, voicemail, contacts, presence, and message-store data. Use when the user asks for a daily digest, morning briefing, catch-up report, missed communications, unresolved calls or texts, voicemail follow-up, or what to work on today.
---

<!-- --8<-- [start:body] -->
# Daily Communications Digest

## Goal

Help the user prepare for the day by reviewing personal RingEX Phone communications from the last
24 hours and turning them into a prioritized action report.

Focus on what needs attention, not on exhaustively listing every record.

## Trigger examples

- "Give me my daily communications digest."
- "What did I miss in RingEX over the last 24 hours?"
- "Summarize my calls, texts, and voicemails since yesterday morning."
- "What communications do I need to follow up on today?"
- "Show me unresolved calls, SMS, and voicemail from the past day."

## Workflow

1. Use the past 24 hours by default unless the user gives a different time range. Convert the
   window to ISO-8601 date-times with offset for `dateFrom`/`dateTo`.
2. Call `get_my_call_activity` (`dateFrom`, `dateTo`) for recent inbound, outbound, and missed
   calls, total talk time, and outstanding callbacks.
3. Call `get_my_communication_inbox` (`dateFrom`, `dateTo`, `messageTypes: ["SMS"]`) for recent
   text messages.
4. Call `get_my_communication_inbox` (`dateFrom`, `dateTo`, `messageTypes: ["VoiceMail"]`) for
   recent voicemail records.
5. Use `get_my_message_detail` (`messageId`) when a specific SMS or voicemail needs its full body
   or verified transcription to understand the action item. Use `get_my_sms_thread` (`messageId`,
   `dateFrom`, `dateTo`) when the full back-and-forth of a text conversation is needed for context.
6. Use `resolve_directory_person` (company directory, by name/department/role) or
   `search_my_contacts` (personal address book, by name/phone number) only when useful to identify
   a caller or contact. For Team Chat person resolution, use RingEX Chat's `find_person` instead —
   `team_messaging_get_person` no longer exists.
7. Use `get_my_phone` only when the user's own presence, business hours, or call-handling rules
   help decide whether to call, text, or defer.
8. Optionally use `get_my_call_insight` (`callId`) for AI notes/transcript on a specific call, or
   `get_my_call_recording_metadata` (`callId`) to check whether a call was recorded, when the call
   log alone doesn't give enough context.
9. Summarize patterns across all records before writing the report.

## What to identify

- Missed inbound calls without a later outbound call to the same person or number.
- Inbound SMS messages without a later user reply.
- Voicemail that has not clearly been addressed.
- Repeated contact attempts from the same person or number.
- Communications that mention urgency, deadlines, blockers, scheduling, customer issues, or needed
  decisions.
- Follow-ups that can be batched by person, account, customer, or topic.

## Output format

```md
# Daily Communications Digest

## Top Priorities
- [Most important follow-up and why it matters.]
- [Second most important follow-up.]

## Unreturned Calls
- [Caller/contact] called at [time]. Action: [call back, text, defer, or no action].

## Unanswered SMS
- [Contact/number] sent: [brief summary]. Action: [suggested response or next step].

## Voicemail Needing Attention
- [Caller/contact] left voicemail at [time]. Key point: [summary]. Action: [follow-up].

## Other Notable Activity
- [Useful context that is not urgent.]

## Suggested Plan
1. [Highest-priority response or call-back.]
2. [Next follow-up.]
3. [Lower-priority cleanup.]
```

## Guidance

- Be concise, practical, and action-oriented.
- Avoid dumping raw logs unless the user asks for them.
- Group related calls, texts, and voicemail from the same person together.
- State uncertainty when identity matching is unclear.
- Do not invent message contents, call outcomes, voicemail transcripts, or follow-up status.
- If tool results are empty, say that no relevant activity was found for the time range.
<!-- --8<-- [end:body] -->
