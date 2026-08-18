---
name: colleague-lookup
description: Looks up a colleague by name, department, job title, or phone number across the company directory and the authenticated RingEX Phone user's personal contacts, disambiguating when more than one match is found. Use when the user asks for someone's extension, title, department, or availability, or wants to find a colleague in the directory or their own contacts.
---

<!-- --8<-- [start:body] -->
# Colleague Lookup

## Goal

Answer "who is this person / how do I reach them" quickly and correctly, being explicit about
which pool of data an answer came from — the company directory is not the same thing as the
user's personal address book, and the two tools that read them accept different selectors.

## Trigger examples

- "What's John's extension?"
- "Is Sarah available right now?"
- "Find Ada Lovelace in the directory."
- "What team is Priya on?"
- "Do I have a personal contact saved for +1 415 555 1234?"
- "Who's the manager of the support department?"

## Scope boundary

- Read-only lookup. This skill never edits, adds, or removes a contact or directory entry — there
  is no such tool exposed on this server.
- `resolve_directory_person` (company directory) only accepts a `name`, `department`, or `role`
  (job title) selector — it does **not** accept a phone number. `search_my_contacts` (personal
  address book) accepts `name` or `phone_number`. If the user gives a phone number and wants to
  know whose it is, this skill can only check the personal address book — say so rather than
  implying a directory-wide reverse lookup exists.
- Presence (availability) is only returned by `resolve_directory_person` when the selector
  resolves to exactly one exact match — never guess at someone's presence from an ambiguous match
  or a department/role roster. When the first call can't return presence for that reason, this
  skill proactively resolves the specific person by exact name afterward so presence can still be
  shown by default — see the Workflow below.

## Workflow

1. **Classify the query.** Determine whether the user gave a name, a department, a job title
   ("role"), or a phone number.

2. **Name query.** Call `resolve_directory_person` with `{ "kind": "name", "value": "…" }` and
   `includePresence: true` — presence is a default part of this skill's answer, not something the
   user has to ask for separately.
      - Single exact match → presence comes back on this same call; use it directly.
      - Multiple candidates → disambiguate using the `AskUserQuestion` tool as the primary,
        preferred method whenever it's available and there are 2–4 candidates: one option per
        candidate, each labeled with its distinguishing detail (department/title, and phone number
        if titles/departments collide). Only fall back to a plain-text ranked list when
        `AskUserQuestion` isn't available or there are more than 4 candidates. Once the user picks
        one, issue a follow-up `resolve_directory_person` call with
        `{ "kind": "name", "value": "<that person's exact full name>" }` and `includePresence: true`
        to fetch their presence — the first, ambiguous call never carries presence, so this
        follow-up is required, not optional.
      - No match in the company directory → fall back to `search_my_contacts` with
        `{ "kind": "name", "value": "…" }` in case it's a personal contact rather than a colleague,
        and say clearly which pool the result (or lack of one) came from. Note that
        `search_my_contacts` never returns presence, regardless of match count.

3. **Department or job-title query.** Call `resolve_directory_person` with
   `{ "kind": "department", "value": "…" }` or `{ "kind": "role", "value": "…" }` — "role" means job
   title, not an administrative permission. This typically returns a roster of more than one
   person, which never carries presence. Present the roster rather than picking one arbitrarily;
   if the user then singles out one person from that roster (by name, or by responding to an
   `AskUserQuestion` prompt built from the roster when it has 2–4 members), resolve that person by
   exact name with `includePresence: true` to surface their presence, the same as the follow-up in
   step 2.

4. **Phone-number query.** Call `search_my_contacts` with
   `{ "kind": "phone_number", "value": "+1…" }` (E.164 format). If nothing matches, say plainly
   that this skill can only check the personal address book for a number — not the company
   directory — rather than implying the lookup was exhaustive. Presence is never available for a
   result from this tool.

5. **Render the result.** Show name, extension/phone, department/title, and presence. Presence
   should be present by default whenever the result resolved to a single exact directory match
   (either directly or via the step 2/3 follow-up); when it's genuinely unavailable — because the
   result came from `search_my_contacts`, or the user never narrowed a roster/candidate list down
   to one person — say so plainly rather than omitting the field silently. Be explicit about the
   source: "from the company directory" vs. "from your personal contacts."

## Guidance

- Never fabricate an extension, phone number, department, title, or presence value — if it wasn't
  returned, say so.
- Never blend the company directory and personal contacts into one undifferentiated answer — the
  user should always know which pool a result came from.
- Never claim presence for an ambiguous match or a roster — resolve to one exact person first via a
  follow-up `resolve_directory_person` call, don't guess or interpolate from a related entry.
- Treat presence as a default expectation of this skill, not an optional extra: always pass
  `includePresence: true`, and always take the extra follow-up call to get a single exact match
  when the first result was ambiguous, rather than stopping at the roster/candidate list.
- Prefer `AskUserQuestion` over a plain-text list whenever there are 2–4 candidates and the tool is
  available — this is the primary disambiguation method this skill should use, not a fallback.
- Treat "role" strictly as job title in this context, never as an admin permission level.
<!-- --8<-- [end:body] -->
