---
name: send-sms
description: Sends a single person-to-person SMS on behalf of the authenticated RingEX Phone user, resolving the recipient, disambiguating the sending number, and confirming the exact message before sending. Use when the user asks to text someone, send an SMS, message a phone number, or reply to a text via RingEX Phone.
---

<!-- --8<-- [start:body] -->
# Send SMS

## Goal

Send one personal SMS from a number the authenticated user owns, with the exact sender,
recipient, and message text confirmed before anything is sent. `send_sms` is a write tool and is
customer-facing and irreversible once delivered — this skill exists to make the required
guardrails automatic rather than optional.

## Trigger examples

- "Text John and tell him I'm running late."
- "Send an SMS to +1 415 555 1234 saying the meeting moved to 3pm."
- "Reply to that text from Sarah with 'sounds good, see you then.'"
- "Message +14085559876 on RingEX."

## Scope boundary

- This skill is for one-off, person-to-person texting only — never bulk, campaign, marketing, or
  A2P messaging. If the request mentions "campaign," "bulk," "opt-out," "consent," "template," or
  "brand," this is the wrong tool; tell the user this skill doesn't cover business/A2P messaging
  rather than attempting a workaround.
- One recipient, one message, per invocation.

## Workflow

1. **Resolve the recipient's phone number.**
      - If the user gave a raw phone number, use it directly in E.164 format.
      - If the user named a person, resolve them first: try `search_my_contacts` (personal address
        book), then `resolve_directory_person` (company directory) if not found there. Never
        fabricate a phone number — if resolution is ambiguous or comes up empty, ask the user to
        clarify or provide the number directly.
2. **Determine the sending number.**
      - Call `get_my_phone` to see which of the authenticated user's numbers are SMS-capable.
      - If there is exactly one SMS-capable number, use it without asking.
      - If there are 2–4 SMS-capable numbers, ask which one to use with a structured
        multiple-choice prompt (the `AskUserQuestion` tool, where available) — one question
        ("Which number should this text be sent from?"), one option per number, each labeled with
        the phone number and any friendly name/type (e.g. "Personal line," "Business number"). If
        one number is clearly the user's primary/default, list it first and mark it
        "(Recommended)."
      - If there are more than 4 SMS-capable numbers, a structured multiple-choice prompt can't
        list them all (max 4 options) — instead list the numbers as plain text and ask the user to
        state which one to use.
      - On a platform without a structured multiple-choice/button tool, fall back to listing the
        numbered options as plain text and asking the user to pick one.
3. **Draft the exact message text.** Preserve the user's intended meaning and tone — don't
   editorialize, expand, or add signatures/disclaimers they didn't ask for.
4. **Preview and confirm before sending — never send silently.**
      - Echo back, verbatim: the sender number, the recipient number, and the exact message text.
      - Wait for an explicit yes/confirm. A vague continuation of the conversation is not
        confirmation.
5. **Send.**
      - Generate a fresh UUID for `requestId`.
      - Call `send_sms` with `senderPhoneNumber`, `recipientPhoneNumber`, `text`, and `requestId`.
6. **Handle the result.**
      - On success, confirm briefly: who it was sent to, from which number, and the text.
      - On failure, report it plainly. If the error suggests the number isn't SMS-capable, note
        that this is usually a number-type or carrier registration (TCR/10DLC) issue on that
        number, not something to retry blindly.
      - On an unknown/ambiguous result (timeout, unclear response), tell the user the delivery
        status is unconfirmed. Do not retry the same intended send with the same or a new
        `requestId` — surface the uncertainty and let the user decide whether to try again.

## Guidance

- Never send an SMS without an explicit, informed confirmation of sender, recipient, and text.
- Never guess a recipient's phone number from a name — resolve it or ask.
- Never guess which number to send from when more than one is available — ask, using a structured
  multiple-choice prompt when 4 or fewer options exist.
- Treat `requestId` reuse as unsafe after an ambiguous result — a duplicate send to a real person
  is a worse outcome than one unconfirmed send.
- Stay out of bulk/A2P/business messaging entirely; redirect the user if that's what they're
  asking for.
<!-- --8<-- [end:body] -->
