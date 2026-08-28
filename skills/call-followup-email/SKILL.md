---
name: call-followup-email
description: >-
  Turns a recent RingEX phone call into a drafted (and optionally sent)
  follow-up email. Pulls the call from the user's RingEX call history,
  resolves who was on the other end and their email address, drafts a
  follow-up that references the call (using the AI call summary/insight when
  one exists), and sends it through whatever email tool is actually
  available — or hands back a ready-to-send draft if none is connected. Use
  this whenever the user wants to follow up on a phone call by email —
  phrases like "email them about that call", "send a follow-up to the
  person I just talked to", "draft a recap for my call with [name]", "I told
  a customer I'd send them something after we hung up", or "can you write a
  follow-up for my 2pm call" — even if they don't mention RingCentral, call
  history, or name a specific email tool. Do not use this for drafting
  emails unrelated to a phone call, or for logging/summarizing a call
  without producing an email (that's ringex-calls or ringex-meetings).
---

<!-- --8<-- [start:body] -->
# Call Follow-Up Email

## What this does

Bridges two things that don't naturally talk to each other: RingEX call history and whatever email tool the user happens to have. The workflow is always the same shape — find the call, find the person and their email, draft something specific (not generic), then get it out the door however is actually possible for this user, today, with whatever they have connected.

The email-sending step is the part most likely to vary between users, so treat "send an email" as a capability to be discovered at runtime, not a specific tool to assume. See "Step 4" below — this is the crux of the skill.

## Step 1: Find the call

Pull recent call activity with `get_my_call_activity`. Default to the last 10 calls across both directions (inbound and outbound) — that covers "the call I just had" and "that call from earlier" without over-asking. If the user already named a person, a rough time ("this morning," "yesterday"), or said "the call I just finished," narrow to that instead of showing a full list.

Before presenting the list, enrich each candidate with whether it has a **recording** (`get_my_call_recording_metadata`) and a **transcript/AI summary** (`get_my_call_insight`) — one call to each tool per candidate, using the call id from `get_my_call_activity`. This costs a handful of extra tool calls up front, but it's worth it: whether a call has a transcript is the single biggest predictor of whether Step 3 can write something specific versus something generic, so the user should see that signal *before* they pick, not discover it after. Show it plainly next to each call, e.g. "🎙️ recorded, 📝 transcript" or "no recording/transcript — call notes only," so the user can weigh that against "this is the call I actually want to follow up on."

Present the candidates and let the user pick one (use `AskUserQuestion` when there's more than one plausible match — phone number, name if known, date/time, duration, direction, and the recording/transcript indicator). If there's exactly one obvious match to what the user described, don't force a pointless confirmation click; just proceed and say which call you picked — but still mention its recording/transcript status so they know what kind of follow-up to expect.

## Step 2: Resolve the other party and their email

This is the step to be honest about, because the tools don't fully cooperate here:

- `search_my_contacts` (RingEX personal address book) can look up the counterpart's **name** by phone number, but its output explicitly excludes email addresses — it's a phone-focused projection only. It will never hand you an email, no matter who's in the address book.
- If a CRM-style connector is connected (Salesforce, HubSpot, Google Contacts, etc.), check there next — a contact record with a phone number often carries an email too. Don't assume one is connected; check what's actually available first (see the discovery pattern in Step 4 — the same "check what's there, don't guess" logic applies to contact lookup, not just sending).
- If nothing resolves an email, just ask the user for it directly. This is the common case today, not a fallback of last resort — say so plainly rather than implying the lookup failed when really no tool for this exists yet.

Do not invent or guess an email address (e.g. from a name + company domain guess). Wrong guesses sent externally are worse than asking.

**Contact creation is out of scope for now.** The only personal-address-book tool available (`search_my_contacts`) is read-only by design — it cannot create or update entries. If a write-capable contacts connector shows up later (via the Step 4 discovery pattern), this would be the natural place to add "save this new contact" as a step. Until then, if the customer isn't in any address book, just mention to the user that they may want to save this contact themselves — don't claim to have saved it.

## Step 3: Draft the email

Pull whatever context makes the email specific rather than generic:

- Call date/time and duration, always.
- The transcript/AI summary from `get_my_call_insight`, if Step 1 found one — use it to reference actual topics discussed rather than writing "great speaking with you today" filler. If Step 1 showed no transcript for the selected call, don't re-check; just fall back to date/duration only and say so ("no transcript for this call, so this draft is fairly generic — want to add anything from memory before I finalize it?") rather than silently producing a thin email.

Keep the tone matched to what a business follow-up after a real phone call sounds like: warm but brief, references something concrete from the call, ends with a clear next step if one was discussed. Show the user the full draft — To, Subject, Body — before doing anything else with it. Never send on the first pass; the draft is always a checkpoint.

## Step 4: Find a way to actually send it

This is the part to get right, because hardcoding "use Gmail" or "use Outlook" breaks for anyone who doesn't have that connected. Instead:

1. **Check what's already available.** Look at the currently available tools/skills for anything that can send an email (not just search one — sending is the bar). If exactly one send-capable option exists, use it. If more than one, ask the user which to use.
2. **If nothing is available, search for one.** Use the MCP registry search for email-capable connectors (Outlook/Microsoft 365, Gmail, or similar) and offer to connect one via the suggest-connector mechanism. This puts a real "Connect" action in front of the user rather than a dead end.
3. **Always keep the no-connector path alive.** Whether the user declines to connect something or nothing suitable exists, the skill should still be useful: hand back the finished draft (To/Subject/Body) as text so the user can paste it into whatever email client they actually use. A drafted email the user sends themselves beats a skill that fails outright because a specific plugin wasn't installed.

Never treat a missing email connector as a hard failure. It's a fork in the road, not a dead end.

## Step 5: Confirm and act

Because this produces a customer-facing, externally-visible message, use the same discipline as other outbound-messaging skills in this environment (see `ringex-send`, `send-sms`): restate the recipient, restate the full content, and get an explicit go-ahead before sending anything. If sending isn't possible (Step 4 fell through to draft-only), there's nothing to confirm-and-send — just deliver the draft.

## Known limitations (as of when this was written)

- No connected tool can create/update a personal contact record — contact auto-creation is intentionally not implemented. Revisit once a write-capable contacts connector is confirmed.
- No connected tool reliably returns a contact's email from a phone number — expect to ask the user for the email address in most cases rather than resolving it silently.
- Whether any given email connector can *send* (vs. only search/read mail) should be verified at connect time, not assumed from its name.
<!-- --8<-- [end:body] -->
