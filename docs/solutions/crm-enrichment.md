# CRM Enrichment

Automate CRM hygiene through natural language. Log calls, capture leads, look up contacts, and attach conversation notes — without ever leaving your AI client.

## What it does

After a sales call or customer conversation, keeping your CRM up to date is tedious but critical. With App Connect, your AI can handle the entire post-call workflow: finding the right contact record, logging the call with duration and notes, and creating a new lead if no record exists — all from a single prompt.

## Examples

### Log a post-call note

<div class="rc-chat">
  <div class="rc-chat__user">
    <div class="rc-chat__bubble rc-chat__bubble--user">
      Log my last call with Sarah Chen at Brightpath. Duration was 18 minutes. She's evaluating our enterprise plan and wants a demo next week.
    </div>
  </div>
  <div class="rc-chat__ai">
    <div class="rc-chat__avatar">AI</div>
    <div class="rc-chat__bubble rc-chat__bubble--ai">
      <p>Done — call logged to Sarah Chen's record at Brightpath Inc.</p>
      <ul>
        <li>Duration: 18 minutes (outbound)</li>
        <li>Note added: Evaluating enterprise plan, demo requested</li>
        <li>Logged: today at 2:14 PM</li>
      </ul>
      <p class="rc-chat__follow-up">I didn't find an open opportunity for this account. Want me to create one?</p>
    </div>
  </div>
</div>

### Look up a contact

<div class="rc-chat">
  <div class="rc-chat__user">
    <div class="rc-chat__bubble rc-chat__bubble--user">
      Find the contact record for Marcus Okonkwo at Vertex Inc. When did we last speak?
    </div>
  </div>
  <div class="rc-chat__ai">
    <div class="rc-chat__avatar">AI</div>
    <div class="rc-chat__bubble rc-chat__bubble--ai">
      <p>Found Marcus Okonkwo — VP of Sales at Vertex Inc.</p>
      <p>Last contact: May 2 (12-minute outbound call). You have 3 logged interactions total. Most recent note: <em>"Interested in scaling to 50+ seats."</em></p>
      <p class="rc-chat__follow-up">Want me to log a new call or add a note to his record?</p>
    </div>
  </div>
</div>

### Create a new lead

<div class="rc-chat">
  <div class="rc-chat__user">
    <div class="rc-chat__bubble rc-chat__bubble--user">
      New prospect — James Wu, +1 650-441-3809, interested in the API tier. Create a lead.
    </div>
  </div>
  <div class="rc-chat__ai">
    <div class="rc-chat__avatar">AI</div>
    <div class="rc-chat__bubble rc-chat__bubble--ai">
      <p>New lead created for James Wu.</p>
      <ul>
        <li>Phone: +1 650-441-3809</li>
        <li>Interest: API tier</li>
        <li>Status: New lead</li>
        <li>Added to your default CRM workspace</li>
      </ul>
      <p class="rc-chat__follow-up">Would you like me to set a follow-up reminder or add any notes?</p>
    </div>
  </div>
</div>

## Tools called

| Step | Tool | Description |
|---|---|---|
| 1 | `findContactByName` or `findContactByPhone` | Locate the existing CRM record |
| 2 | `createCallLog` | Write the call entry with duration, direction, and notes |
| 3 | `createContact` | Create a new record if no match is found |

## Prerequisites

- App Connect MCP server connected to your AI client
- A supported CRM platform configured in App Connect
- Valid RingCentral session active

!!! note "Supported CRM platforms"
    Use [`getPublicConnectors`](../tools/app-connect/get-public-connectors.md) to see the full list of CRM platforms currently supported by App Connect.
