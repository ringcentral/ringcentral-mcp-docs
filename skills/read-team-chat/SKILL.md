---
name: read-team-chat
description: Lets the authenticated RingEX Chat user browse recent Team Chat chats and read a selected one as a formatted post stream, or jump straight to a named channel/person and catch up on what's new there. Read-only. Use when the user wants to catch up on Team Chat/Glip, see what's new in a channel, review recent posts, or read a specific conversation.
---

<!-- --8<-- [start:body] -->
# Read Team Chat

## Goal

Give the user a fast way to catch up on Team Chat: either a pick-a-chat browsing flow like
`sms-inbox`'s conversation list, or a direct jump into a named channel or person's direct chat.
Purely read-only — this skill never posts, replies, or manages anything (that's `send-post`,
`manage_post`, or `manage_chat_item`).

## Trigger examples

- "Catch me up on Team Chat."
- "What's new in the product-updates channel?"
- "Show me my recent Glip chats."
- "Read the last messages in the sales channel."
- "Did anyone post anything in my DM with Ben?"

## Scope boundary

- Read-only. This skill never sends a post, edits/deletes one, or manages a team/task/note/event —
  hand off to `send-post` (for posting) or the relevant `manage_*` tool if the user wants to act on
  what they read.
- Team Chat only — not SMS, voicemail, or fax (those are RingEX Phone skills).
- A chat's identity is the chat itself, not a person — a 1:1 direct chat and a group/team chat are
  never merged or confused with each other.

## Workflow

1. **Resolve which chat to read.**
      - If the user named a specific channel, team, or person, try to match it: for a person, call
        `find_person` to resolve them, then use `read_team_chat` (`resource: "chat"`,
        `action: "list"`) to find their direct chat, or `action: "get"` if a chat id is already
        known. For a named channel/team, use `read_team_chat` (`resource: "chat"`,
        `action: "list"`) and match by name.
      - If nothing specific was named, list recent chats: `read_team_chat`
        (`resource: "chat"`, `action: "list"`, `type: "recent"`), which returns them newest-active
        first.

2. **Present a choice if the destination is ambiguous or unnamed.**
      - If the user named a chat and there's exactly one match, proceed straight to step 3.
      - If there are 2–4 plausible matches (or, for a general "catch me up," 2–4 recent chats),
        use a structured multiple-choice prompt (the `AskUserQuestion` tool, where available), one
        option per chat, labeled with its name and a short recency cue.
      - If there are more than 4, list them as a plain-text ranked list by recency instead.
      - If nothing was found, say so rather than guessing at prior activity.

3. **Pull recent posts for the selected chat.** Call `read_team_chat`
   (`resource: "post"`, `action: "list"`, `chatId`, a `recordCount` of roughly 20). If that comes
   back thin (fewer than ~10 posts) and the user wants more history, increase `recordCount` and
   re-fetch rather than presenting a sparse result as complete.

4. **Resolve sender names.** If a post's sender is only an id, resolve it with `find_person`
   (`personId`) rather than showing a raw id.

5. **Render the stream.** Show posts oldest-to-newest, each as a labeled block (sender name,
   timestamp, text), with a blank line between posts so it reads like a conversation log. Note the
   presence of attachments, Adaptive Cards, or referenced tasks/notes/events inline (e.g.
   "[attachment: filename]", "[Adaptive Card]") rather than fetching their full content
   automatically — offer to pull one open if the user asks.

6. **Offer a digest, not just a raw log, when that's what was asked for.** If the user's ask was
   "catch me up" rather than "show me the messages," add a short summary on top of the raw stream:
   decisions made, open questions directed at the user, and anything that looks like an action
   item — but keep the underlying stream available since a summary can miss nuance.

## Guidance

- Never invent a post's sender, timestamp, or content — if a field is missing or a name can't be
  resolved, say so rather than guessing.
- Never conflate a 1:1 direct chat with a group/team chat just because a person appears in both.
- Never take a write action (post, edit, delete, manage) from within this skill — surface what to
  do next and hand off to the appropriate write skill/tool instead.
- Keep the chat-picker step fast and skimmable; save full post rendering and digesting for after a
  chat is chosen.
<!-- --8<-- [end:body] -->
