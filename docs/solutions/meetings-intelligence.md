# Meetings Intelligence

Stop losing track of what was decided, who owns what, and what was promised. Let AI search your meeting history, extract to-dos, and keep you accountable across every recorded session.

## What it does

RingCentral stores recordings, transcripts, and AI summaries for every RingCentral Video meeting. The MCP server makes that archive searchable and actionable — your AI can find past meetings by topic or participant, extract decisions and action items from a specific session, and surface anything that's gone unresolved.

## Examples

### Extract meeting decisions

<div class="rc-chat">
  <div class="rc-chat__user">
    <div class="rc-chat__bubble rc-chat__bubble--user">
      What were the key decisions from my Q2 business review last Thursday?
    </div>
  </div>
  <div class="rc-chat__ai">
    <div class="rc-chat__avatar">AI</div>
    <div class="rc-chat__bubble rc-chat__bubble--ai">
      <p>From your Q2 Business Review (May 7, 94 min, 8 attendees):</p>
      <p><strong>Decisions made:</strong></p>
      <ul>
        <li>Expand enterprise tier pricing by 15% in Q3</li>
        <li>Pause APAC launch until Q4</li>
        <li>Sarah to lead the customer advisory board initiative</li>
      </ul>
      <p><strong>Action items assigned to you:</strong></p>
      <ul>
        <li>Draft revised pricing deck by May 21</li>
        <li>Schedule 1:1 with APAC team lead</li>
      </ul>
      <p class="rc-chat__follow-up">Want the full transcript or just your open action items?</p>
    </div>
  </div>
</div>

### Search by topic

<div class="rc-chat">
  <div class="rc-chat__user">
    <div class="rc-chat__bubble rc-chat__bubble--user">
      Find all meetings where we discussed the API roadmap in the last 60 days.
    </div>
  </div>
  <div class="rc-chat__ai">
    <div class="rc-chat__avatar">AI</div>
    <div class="rc-chat__bubble rc-chat__bubble--ai">
      <p>Found 4 meetings mentioning the API roadmap (Mar 13 – May 12):</p>
      <ul>
        <li><strong>Platform Sync</strong> — Mar 13: decided v2 auth ships in Q2</li>
        <li><strong>Eng Standup</strong> — Apr 1: rate limit issue flagged</li>
        <li><strong>Customer Advisory Board</strong> — Apr 22: 3 customers asked for webhooks</li>
        <li><strong>Roadmap Review</strong> — May 8: webhooks added to Q3 backlog</li>
      </ul>
      <p>Webhooks came up in 3 of 4 meetings.</p>
      <p class="rc-chat__follow-up">Want a summary of the webhook discussions across all four?</p>
    </div>
  </div>
</div>

### Open action item tracking

<div class="rc-chat">
  <div class="rc-chat__user">
    <div class="rc-chat__bubble rc-chat__bubble--user">
      List every action item assigned to me from meetings this month that I haven't marked as done.
    </div>
  </div>
  <div class="rc-chat__ai">
    <div class="rc-chat__avatar">AI</div>
    <div class="rc-chat__bubble rc-chat__bubble--ai">
      <p>Found 5 open action items assigned to you in May:</p>
      <ul>
        <li>Draft revised pricing deck — due May 21 (from Q2 Review, May 7)</li>
        <li>Schedule 1:1 with APAC team lead (from Q2 Review, May 7)</li>
        <li>Share onboarding plan with Apex Group (from CS Sync, May 9)</li>
        <li>Review webhook spec from Eng (from Roadmap Review, May 8)</li>
        <li>Send NDA to Meridian contact (from Sales Sync, May 6)</li>
      </ul>
      <p class="rc-chat__follow-up">Want me to sort these by due date or flag the most overdue?</p>
    </div>
  </div>
</div>

## Tools called

| Step | Tool | Description |
|---|---|---|
| 1 | *(Meeting search)* | Find meeting records by date, participant, or keyword |
| 2 | *(Transcript / summary read)* | Retrieve the transcript or AI-generated summary |
| 3 | *(AI synthesis)* | Extract decisions, action items, and open questions |

## Prerequisites

- RingCentral MCP server connected to your AI client
- RingCentral Video with recording enabled on your account
- RingSense AI enabled for automatic summaries and transcripts

!!! info "Transcript quality"
    Action item and decision extraction works best with full transcripts. AI summaries alone may miss nuance — if precision matters, enable full transcript capture in your RingCentral Video settings.
