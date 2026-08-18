---
name: sms-inbox
description: Presents the authenticated RingEX Phone user's SMS and MMS inbox as a clickable list of recent conversations, then renders the selected conversation as a formatted text-message stream. Excludes voicemail and fax. Use when the user asks to see their texts, SMS inbox, message threads, who they've been texting, or to open a text conversation with someone.
---

<!-- --8<-- [start:body] -->
# SMS Inbox

## Goal

Give the user a browsable view of their personal text conversations: first a list of who they've
recently exchanged SMS/MMS with, then — once they pick someone — that conversation rendered like a
text-message stream. Voicemail and fax are never part of this skill. This is read-only; sending a
new message is a different skill (`send-sms`).

## Trigger examples

- "Show me my SMS inbox."
- "Who have I been texting recently?"
- "Open my text conversation with Sarah."
- "Show me that group text with the sales team."
- "Catch me up on my texts from this week."

## Scope boundary

- SMS and MMS only. Never include voicemail or fax records, even if the user says "messages" or
  "inbox" generically — if they explicitly ask for voicemail or fax, say this skill doesn't cover
  that instead of quietly including it.
- Read-only. This skill never sends, replies, marks read/unread, or deletes anything — hand off to
  `send-sms` if the user wants to reply.
- A group text (more than one other participant) is its own distinct conversation. Never merge a
  group thread into a participant's 1:1 thread just because they share a person, and never split a
  group thread into separate per-person conversations.

## Workflow

1. **Pull recent SMS/MMS activity.** Call `get_my_communication_inbox` with
   `messageTypes: ["SMS"]` (this covers both plain SMS and MMS text records — voicemail and fax
   are separate `messageTypes` values and must not be requested). Default the window to the last
   14 days unless the user asks for a different range.
2. **Group records into conversations.** A conversation's identity is the exact set of other
   participants (phone numbers) on the message, not a single number:
      - One other participant → a 1:1 conversation with that person.
      - More than one other participant → a group conversation, keyed by that whole set. A group
        thread with Sarah + Mike is a different conversation from a 1:1 thread with Sarah alone,
        even though Sarah is in both.
   - Sort conversations by their most recent message time, newest first.
3. **Resolve display names.** For each participant number, try `search_my_contacts` (personal
   address book) then `resolve_directory_person` (company directory); fall back to the raw phone
   number if neither resolves. Label a group conversation by joining participant names/numbers
   (e.g. "Sarah Kim, Mike Chen"); if there are more than 3 participants, show the first two names
   followed by "+N more".
4. **Present the conversation list as a choice.**
      - If there are 2–4 recent conversations, use a structured multiple-choice prompt (the
        `AskUserQuestion` tool, where available): one option per conversation, labeled with the
        resolved name(s), with the most recent message snippet and timestamp as the description.
      - If there are more than 4, or fewer than 2 (zero or one), list them as a plain-text ranked
        list instead — a multiple-choice prompt can't show more than 4 options, and a single
        conversation doesn't need a picker at all (just confirm and proceed to step 5).
      - If nothing was found in the window, say so and offer to check a wider date range instead of
        guessing at prior activity.
5. **Fetch the selected conversation.** Take any `messageId` belonging to that conversation and
   call `get_my_sms_thread` (`messageId`, `dateFrom`, `dateTo`), oldest message first. If the
   default window doesn't return at least ~10 messages, widen `dateFrom` further back (e.g. in
   30-day steps) and re-fetch rather than presenting a thin conversation as if it were complete.
6. **Trim and render.** Keep only the most recent ~10 messages. Render them as a text-message
   stream, oldest at the top, in this shape:

   ```
   Sarah Kim · Tue 2:14 PM
   Running 10 min late, sorry!

   You · Tue 2:15 PM
   No worries, see you soon

   Sarah Kim · Tue 2:16 PM
   😊
   ```

   - Label the user's own messages "You"; label others by their resolved name (or number if
     unresolved). In a group conversation, label each message with the specific sender — never
     collapse multiple participants under one label.
   - Put a blank line between each message so the stream reads like a chat log, not a wall of text.
   - `get_my_sms_thread` never returns MMS binary content — if a message carried an attachment,
     say so in place of the media (e.g. "[MMS attachment]") rather than omitting it silently or
     inventing a description of it.
   - If there are more than ~10 messages in the window, note that older messages exist and offer
     to go further back rather than silently truncating without saying so.

## Guidance

- Never invent a message's content, sender, or timestamp — if a field is missing, say it's
  unavailable.
- Never fold voicemail or fax into this view.
- Never merge or split conversations incorrectly — participant-set identity is the rule, not a
  single phone number.
- Keep the conversation list step fast and skimmable; save full message rendering for after a
  conversation is chosen.
<!-- --8<-- [end:body] -->
