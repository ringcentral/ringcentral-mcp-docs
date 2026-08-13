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

1. Use the past 24 hours by default unless the user gives a different time range.
2. Call `list_user_call_log` for recent inbound, outbound, and missed calls.
3. Call `list_message_store_records` with SMS-focused filters for recent text messages.
4. Call `list_message_store_records` with voicemail-focused filters for recent voicemail records.
5. Use `read_message_store_record` and `read_message_store_content` when voicemail or message
   details are needed to understand the action item.
6. Use `search_directory_entries`, `platform_list_contacts`, `platform_read_contact`,
   `read_extension_profile`, or `team_messaging_get_person` only when useful to identify people.
7. Use `read_user_presence` or `platform_read_user_presence_status` only when presence helps decide
   whether to call, text, or defer.
8. Summarize patterns across all records before writing the report.

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
