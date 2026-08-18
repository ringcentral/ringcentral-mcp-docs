---
name: call-recap
description: Finds a specific recent call in the authenticated RingEX Phone user's own call history and recaps it with AI notes, transcript excerpts, and whether it was recorded. Use when the user asks to recap a call, summarize what was discussed, check if a call was recorded, or find a call about a specific topic or person.
---

<!-- --8<-- [start:body] -->
# Call Recap

## Goal

Turn "what happened on that call" into a quick answer: who it was with, when, what the AI notes
or transcript say, and whether a recording exists. This is read-only — it never plays audio and
never exposes recording ids, URIs, or content locations, only whether a recording exists and in
what mode.

## Trigger examples

- "Recap my last call with Priya."
- "What did we discuss on the call with support this morning?"
- "Was my call with the vendor yesterday recorded?"
- "Find a call from last month where renewal pricing came up."
- "Summarize my calls from yesterday."

## Scope boundary

- Personal call history only — this skill never looks at anyone else's calls, and there is no
  account- or team-wide call log on this server (that lives on RingEX Admin).
- Read-only. Never claims to play, download, or attach recording audio — only
  `get_my_call_recording_metadata`'s safe projection (recording exists, and in what mode) is ever
  available.
- Not every call has AI notes or a transcript — that depends on whether AI call notes were enabled
  for that call. If neither is available, say so rather than fabricating a summary from the call's
  metadata alone.

## Workflow

1. **Establish the search window and any filters.** Default to today unless the user names a
   different range ("yesterday," "last month," "this week"). If the user names a person or a topic
   (e.g. "the call about renewal pricing"), prefer `search_my_call_insights` with `dateFrom`,
   `dateTo`, and `person` (phone number or extension) and/or `topic` — remember `topic` is a
   literal substring match against searchable AI content, not a semantic query, so mention that if
   the search comes up empty ("try a different phrase" rather than assuming nothing was said).

2. **If no person/topic was given, browse by activity instead.** Call `get_my_call_activity` with
   the resolved `dateFrom`/`dateTo` to get the aggregate view (recent/missed/returned calls) and
   use it to identify candidate calls to recap.

3. **Resolve names for candidates.** For each candidate call's counterpart number, try
   `search_my_contacts` then `resolve_directory_person`; fall back to the raw number if neither
   resolves.

4. **Present candidates as a choice** if more than one call could match:
      - 2–4 candidates → a structured multiple-choice prompt (the `AskUserQuestion` tool, where
        available), one option per call, labeled with the resolved name, direction, and time.
      - More than 4, or exactly one → a plain-text ranked list, or auto-proceed if there's only one
        unambiguous match.
      - No matches → say so and offer to widen the date range rather than guessing.

5. **Pull the recap for the selected call.** Using that call's id:
      - Call `get_my_call_insight` for AI notes and transcript text.
      - Call `get_my_call_recording_metadata` to check whether the call has recording metadata and
        in what mode (e.g. automatic/on-demand) — this never returns audio or a recording id/URI.

6. **Render the recap.** Show who the call was with, when, direction, the AI notes/transcript
   content if available, and a one-line recording status ("Recorded — automatic" / "No recording
   found"). If AI notes/transcript weren't available for that call, say so plainly instead of
   summarizing from call metadata alone.

## Guidance

- Never fabricate AI notes, transcript content, or recording status — report exactly what the
  tools returned, including when a field is absent.
- Never imply audio was accessed, played, or attached — recording metadata only confirms
  existence and mode.
- Treat `topic` searches as literal substring matches, not semantic search, when explaining
  results (or the lack of them) to the user.
- Stay within the user's own call history — this skill has no account- or team-wide scope.
<!-- --8<-- [end:body] -->
