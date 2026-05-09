# CRM Integration Workflow

This guide walks through the most common real-world workflow: automatically logging RingCentral call activity into your CRM using AI.

---

## Overview

```
┌─────────────┐     rcGetCallLogs      ┌──────────────────┐
│  RingCentral │ ◄────────────────────  │                  │
│  Platform   │ ────────────────────►  │   AI Assistant   │
└─────────────┘                        │   (Claude, etc.) │
                                       │                  │
┌─────────────┐   findContactByPhone   │                  │
│  CRM        │ ◄────────────────────  │                  │
│  Platform   │ ────────────────────►  │                  │
└─────────────┘                        │                  │
       ▲          createCallLog        │                  │
       └──────────────────────────────  └──────────────────┘
```

---

## Workflow 1 — End-of-day call logging

Log all of today's calls to your CRM in one step.

**Prompt:**
```
Log all of my RingCentral calls from today to Salesforce. 
For each call, look up the caller in the CRM and attach the log to their record.
```

**What happens under the hood:**

1. `rcGetCallLogs` — fetches today's calls
2. For each call record:
   - `findContactByPhone` — resolves the caller to a CRM contact
   - `createCallLog` — posts the activity with `incomingData` + `contactId`

---

## Workflow 2 — Inbound caller identification

Identify a caller and surface their CRM record before you pick up.

**Prompt:**
```
Someone is calling from +1 415 555 0123. Who is it and what's their latest CRM activity?
```

**What happens:**

1. `findContactByPhone("+14155550123")` — returns name, company, CRM URL
2. AI summarises their record and recent notes

---

## Workflow 3 — Post-call note with summary

After a call, dictate a note and have it logged automatically.

**Prompt:**
```
I just finished a call with Jane Smith. 
Log it to Salesforce with this note: 
"Discussed Q3 renewal. She's interested in upgrading to Enterprise. 
Will send proposal by Friday."
```

**What happens:**

1. `findContactByName("Jane Smith")` — resolves CRM ID
2. `rcGetCallLogs` (last 1 hour) — finds the matching call record
3. `createCallLog` — posts log with `incomingData` + `contactId` + `note`

---

## Workflow 4 — Unknown caller → create and log

Handle calls from contacts not yet in your CRM.

**Prompt:**
```
I just got a call from +1 650 555 9999 — a new prospect named Alex Johnson. 
Create them as a contact in Salesforce and log the call with note: 
"First inbound inquiry. Interested in Team plan."
```

**What happens:**

1. `findContactByPhone("+16505559999")` → empty result
2. `createContact({ phoneNumber: "+16505559999", newContactName: "Alex Johnson" })`
3. `rcGetCallLogs` — fetches the call record
4. `createCallLog` — logs against the new contact

---

## Best practices

- **Always run `getSessionInfo` at workflow start** to confirm both RC and CRM sessions are active before attempting write operations.
- **Batch by day, not by week** — `rcGetCallLogs` has a 7-day max window. Daily logging avoids hitting limits.
- **Include a `note`** — structured notes make CRM records far more useful than raw telephony data alone.
- **Use `incomingData` for accuracy** — passing the raw RC call record via `incomingData.logInfo` ensures duration, direction, and timestamps are correctly populated.

---

## Error handling

| Error | Likely cause | Resolution |
|-------|-------------|------------|
| `Authentication failed` | CRM session expired | Call `logout` then reconnect |
| `Contact not found` | Phone number not in CRM | Use `createContact` first |
| `Duplicate log` | Same call logged twice | Check CRM for existing activity before calling `createCallLog` |
| `Invalid phone format` | Number not in E.164 | Prefix with `+` and country code |
