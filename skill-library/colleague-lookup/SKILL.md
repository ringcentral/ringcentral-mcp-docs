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
  resolves to exactly one exact match — never guess at someone's presence from an ambiguous match.

## Workflow

1. **Classify the query.** Determine whether the user gave a name, a department, a job title
   ("role"), or a phone number.

2. **Name query.** Call `resolve_directory_person` with `{ "kind": "name", "value": "…" }`
   (`includePresence: true` if the user cares about availability).
      - Single exact match → use it directly.
      - Multiple candidates → disambiguate: 2–4 candidates use a structured multiple-choice prompt
        (the `AskUserQuestion` tool, where available), labeled with each candidate's distinguishing
        detail (department/title); more than 4 → a plain-text ranked list.
      - No match in the company directory → fall back to `search_my_contacts` with
        `{ "kind": "name", "value": "…" }` in case it's a personal contact rather than a colleague,
        and say clearly which pool the result (or lack of one) came from.

3. **Department or job-title query.** Call `resolve_directory_person` with
   `{ "kind": "department", "value": "…" }` or `{ "kind": "role", "value": "…" }` — "role" means job
   title, not an administrative permission. This typically returns more than one person; present
   the list rather than picking one arbitrarily.

4. **Phone-number query.** Call `search_my_contacts` with
   `{ "kind": "phone_number", "value": "+1…" }` (E.164 format). If nothing matches, say plainly
   that this skill can only check the personal address book for a number — not the company
   directory — rather than implying the lookup was exhaustive.

5. **Render the result.** Show name, extension/phone, department/title, and presence (only if it
   came back). Be explicit about the source: "from the company directory" vs. "from your personal
   contacts."

## Guidance

- Never fabricate an extension, phone number, department, title, or presence value — if it wasn't
  returned, say so.
- Never blend the company directory and personal contacts into one undifferentiated answer — the
  user should always know which pool a result came from.
- Never claim presence for an ambiguous match — resolve to one person first, or say presence isn't
  available yet.
- Treat "role" strictly as job title in this context, never as an admin permission level.
<!-- --8<-- [end:body] -->
