# Coaching & Insights

Use AI to analyze your communication patterns, surface areas for improvement, and benchmark your outcomes against your own history — all grounded in real call data.

## What it does

When your AI has access to your full call history and transcripts, it can act as a communication coach rather than just a note-taker. It can identify patterns across dozens or hundreds of calls: which conversations lead to outcomes, how long your calls typically run, how often you follow up, and where your pacing or messaging could be sharper.

## Examples

### Sales call pattern analysis

<div class="rc-chat">
  <div class="rc-chat__user">
    <div class="rc-chat__bubble rc-chat__bubble--user">
      Review my last 20 outbound sales calls. What patterns come up in the ones that ended with a scheduled follow-up?
    </div>
  </div>
  <div class="rc-chat__ai">
    <div class="rc-chat__avatar">AI</div>
    <div class="rc-chat__bubble rc-chat__bubble--ai">
      <p>Analyzed 20 outbound calls from the past 6 weeks. Of the 8 that converted to a follow-up:</p>
      <ul>
        <li>Average duration was <strong>2.3× longer</strong> (14 min vs 6 min)</li>
        <li>You asked an open-ended question in the first 90 seconds</li>
        <li>Discovery covered budget, timeline, and decision process</li>
      </ul>
      <p>In calls without follow-ups, conversations focused on features before understanding the buyer's situation.</p>
      <p class="rc-chat__follow-up">Want specific examples of the opening questions that worked best?</p>
    </div>
  </div>
</div>

### Objection frequency

<div class="rc-chat">
  <div class="rc-chat__user">
    <div class="rc-chat__bubble rc-chat__bubble--user">
      What objections am I hearing most in my calls this month?
    </div>
  </div>
  <div class="rc-chat__ai">
    <div class="rc-chat__avatar">AI</div>
    <div class="rc-chat__bubble rc-chat__bubble--ai">
      <p>From 34 call transcripts in May, the top objections were:</p>
      <ul>
        <li><strong>"We already have a solution"</strong> — 12 mentions</li>
        <li><strong>"Not the right time / budget"</strong> — 9 mentions</li>
        <li><strong>"Need to involve my manager"</strong> — 7 mentions</li>
      </ul>
      <p>In 4 of the "not the right time" calls you moved to a follow-up. You have no recorded recovery strategy for the "already have a solution" objection.</p>
      <p class="rc-chat__follow-up">Want me to suggest some approaches based on what's worked in similar calls?</p>
    </div>
  </div>
</div>

### Topic flagging across calls

<div class="rc-chat">
  <div class="rc-chat__user">
    <div class="rc-chat__bubble rc-chat__bubble--user">
      Flag any calls in the last two weeks where the customer mentioned pricing, cancellation, or a competitor by name.
    </div>
  </div>
  <div class="rc-chat__ai">
    <div class="rc-chat__avatar">AI</div>
    <div class="rc-chat__bubble rc-chat__bubble--ai">
      <p>Found 6 calls matching those topics (Apr 28 – May 12):</p>
      <ul>
        <li><strong>Pricing mentioned:</strong> 4 calls — Brightpath (May 2), Vertex Inc. (May 5), two others</li>
        <li><strong>Competitor named:</strong> 2 calls — "Zoom Phone" came up in both</li>
        <li><strong>Cancellation:</strong> 0 mentions</li>
      </ul>
      <p class="rc-chat__follow-up">Want me to pull the transcript excerpts where these topics came up?</p>
    </div>
  </div>
</div>

## Tools called

| Step | Tool | Description |
|---|---|---|
| 1 | `rcGetCallLogs` | Retrieve call records and transcripts for the target period |
| 2 | *(AI synthesis)* | Pattern analysis, theme extraction, and coaching recommendations |

## Prerequisites

- RingCentral MCP server connected to your AI client
- RingSense AI or call recording enabled to generate transcripts
- Sufficient call history for meaningful analysis (10+ calls recommended)

!!! tip "Better results with transcripts"
    Coaching insights are significantly richer when transcript data is available. Without transcripts, analysis is limited to metadata like duration, direction, and time of day.
