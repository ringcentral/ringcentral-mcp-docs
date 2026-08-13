---
name: send-post
description: Sends a single RingCentral Team Chat post to a resolved person or a known chat/channel on behalf of the authenticated RingEX Chat user, with destination resolution and a mandatory preview/confirm step before posting. Use when the user asks to post in a channel, message someone on Team Chat/Glip, reply in a thread, or send an update to a team — not for SMS/text messages.
---

<!-- --8<-- [start:body] -->
# Send Post

## Goal

Send one Team Chat post — to a person or a channel — with the exact destination and text
confirmed before anything is posted. `send_post` is a write tool; this skill exists to make that
confirmation automatic rather than optional, the same discipline `send-sms` applies to texting.

## Trigger examples

- "Post in the sales channel that the demo is confirmed."
- "Message Ana on Team Chat and ask if she's free."
- "Reply to that thread with 'acknowledged.'"
- "Tell the engineering team the deployment finished."

## Scope boundary

- This is RingCentral Team Chat (Glip) only — never use this for SMS/text messages (that's
  `send-sms`) or for creating Adaptive Cards, tasks, notes, or events (those are separate tools:
  `manage_adaptive_card`, `manage_chat_item`).
- One destination, one message, per invocation. If the user wants the same update sent to several
  channels or people, confirm each destination and message individually rather than broadcasting
  silently.
- Editing or deleting a post already sent is out of scope for this skill (that's `manage_post`).

## Workflow

1. **Resolve the destination.**
      - **Sending to a person:** call `find_person` with a `query` (name, email, extension, or
        phone number). A single exact match returns a `personId` directly. A candidate list means
        it's ambiguous — disambiguate with a structured multiple-choice prompt (the
        `AskUserQuestion` tool, where available) for 2–4 candidates, or a plain-text list for more
        than 4. A `not_found` result means don't guess — ask the user for a more specific
        identifier (email, extension, or exact name).
      - **Sending to a channel/team:** if the user already gave a `chatId`, use it directly.
        Otherwise use `read_team_chat` (`resource: "chat"`, `action: "list"`) to find a chat whose
        name matches what the user said. If more than one chat plausibly matches, disambiguate the
        same way as above rather than guessing which one they meant.

2. **Determine if this is a thread reply.** If the user is replying within an existing
   conversation thread, identify the parent post's id (from context or from
   `read_team_chat`/`resource: "post"`) and plan to pass it as `threadId`.

3. **Draft the exact message text.** Preserve the user's intended meaning and tone — don't
   editorialize, expand, or add signatures/salutations they didn't ask for. Note any file/image
   attachments the user wants included, but only if the content is already available to attach —
   never fabricate or guess at an attachment.

4. **Preview and confirm before sending — never send silently.**
      - Echo back, verbatim: the resolved destination (person's name or chat/channel name), whether
        it's a thread reply, and the exact message text.
      - Wait for an explicit yes/confirm. A vague continuation of the conversation is not
        confirmation.

5. **Send.** Call `send_post` with `chatId` or `personId`, `text`, and `threadId`/`files` if
   applicable.

6. **Handle the result.**
      - On success, confirm briefly: where it was posted (or who it was sent to) and the text.
      - On failure, report it plainly. If attachments were involved, note that the result reports
        per-step status and any already-uploaded attachment ids — so a retry doesn't need to
        re-upload files that already succeeded.
      - On an unclear result, tell the user the post status is unconfirmed rather than assuming it
        went through or silently retrying.

## Guidance

- Never post without an explicit, informed confirmation of destination and text.
- Never guess a person's `personId` or a channel's `chatId` from a name — resolve it or ask.
- Never treat SMS and Team Chat as interchangeable — this skill only ever calls `send_post`, never
  `send_sms`.
- One destination and message per confirmation — don't fan a single approval out across multiple
  sends.
<!-- --8<-- [end:body] -->
