# Communication Analytics

Turn your call history into actionable intelligence. Query call volume trends, duration patterns, busiest hours, and transcript content — without building a report or writing a query.

## What it does

RingCentral stores a complete log of every call made across your organization. The RingCentral MCP server exposes that data to your AI, which can slice it any way you ask — by time range, direction, extension, or contact — and surface patterns that would take hours to find manually.

## Examples

### Weekly call summary

<div class="rc-chat">
  <div class="rc-chat__user">
    <div class="rc-chat__bubble rc-chat__bubble--user">
      How many calls did I make last week, and what was the average duration?
    </div>
  </div>
  <div class="rc-chat__ai">
    <div class="rc-chat__avatar">AI</div>
    <div class="rc-chat__bubble rc-chat__bubble--ai">
      <p>Here's your call summary for May 4–10:</p>
      <ul>
        <li><strong>47 calls</strong> total — 29 outbound, 18 inbound</li>
        <li>Average duration: <strong>8m 32s</strong></li>
        <li>Longest: 41 min with Brightpath Inc. (May 7)</li>
        <li>Busiest day: Tuesday — 14 calls</li>
      </ul>
      <p class="rc-chat__follow-up">Want me to break this down by contact or time of day?</p>
    </div>
  </div>
</div>

### Peak hour analysis

<div class="rc-chat">
  <div class="rc-chat__user">
    <div class="rc-chat__bubble rc-chat__bubble--user">
      Which hours of the day see the most inbound calls? Last 30 days.
    </div>
  </div>
  <div class="rc-chat__ai">
    <div class="rc-chat__avatar">AI</div>
    <div class="rc-chat__bubble rc-chat__bubble--ai">
      <p>Your peak inbound hours for April 12 – May 12:</p>
      <ul>
        <li>Morning peak: <strong>9–11 AM</strong> — 38% of inbound volume</li>
        <li>Afternoon peak: <strong>2–4 PM</strong> — 29%</li>
        <li>Quietest: 12–1 PM and after 5 PM</li>
      </ul>
      <p>Monday and Tuesday consistently see the highest inbound volume.</p>
      <p class="rc-chat__follow-up">Want a day-of-week breakdown alongside the hourly data?</p>
    </div>
  </div>
</div>

### Account conversation history

<div class="rc-chat">
  <div class="rc-chat__user">
    <div class="rc-chat__bubble rc-chat__bubble--user">
      Find all calls with Acme Corp from the last 90 days and summarize what was discussed.
    </div>
  </div>
  <div class="rc-chat__ai">
    <div class="rc-chat__avatar">AI</div>
    <div class="rc-chat__bubble rc-chat__bubble--ai">
      <p>Found 11 calls with Acme Corp between Feb 11 – May 12. Based on transcripts:</p>
      <ul>
        <li>Contract renewal discussed across 6 calls</li>
        <li>Support escalation in March (3 calls)</li>
        <li>New product interest surfaced in April</li>
      </ul>
      <p>Last call: April 29 — you discussed moving to an annual plan. No decision recorded yet.</p>
      <p class="rc-chat__follow-up">Want the full transcript for any of these?</p>
    </div>
  </div>
</div>

## Tools called

| Step | Tool | Description |
|---|---|---|
| 1 | `rcGetCallLogs` | Retrieve call records filtered by date range, direction, or contact |
| 2 | *(AI synthesis)* | Aggregate, group, and surface patterns from the returned records |

## Prerequisites

- RingCentral MCP server connected to your AI client
- Active RingCentral account with call history
- For transcript access: RingSense AI or call recording enabled on your account

!!! info "Date ranges"
    The `rcGetCallLogs` tool supports filtering by `dateFrom` and `dateTo`. For large date ranges, your AI client may make multiple paginated calls automatically.
