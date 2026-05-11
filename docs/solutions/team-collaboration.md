# Team Collaboration

Search your team's message history, send messages to channels or direct conversations, and maintain full context across your internal communications — without leaving your AI client.

## What it does

RingCentral Team Messaging stores the full history of every direct message and group conversation in your organization. The MCP server makes that history available to your AI, which can search across channels, surface relevant threads, and send new messages on your behalf — keeping you in the loop without constant context-switching.

## Examples

### Catch up on a channel thread

<div class="rc-chat">
  <div class="rc-chat__user">
    <div class="rc-chat__bubble rc-chat__bubble--user">
      What did the engineering team discuss about the rate limit issue in #platform-eng this week?
    </div>
  </div>
  <div class="rc-chat__ai">
    <div class="rc-chat__avatar">AI</div>
    <div class="rc-chat__bubble rc-chat__bubble--ai">
      <p>Here's what was shared in #platform-eng this week about rate limits:</p>
      <ul>
        <li><strong>Tuesday:</strong> Diego flagged that 3 enterprise customers hit the 1,000 req/min ceiling. Kevin confirmed it's a known limitation. No ticket opened yet.</li>
        <li><strong>Wednesday:</strong> Mei shared a proposed fix — tiered limits by plan. Thread got 7 reactions but no decision recorded.</li>
      </ul>
      <p class="rc-chat__follow-up">No resolution reached. Want me to draft a message asking for a decision, or create a Jira ticket?</p>
    </div>
  </div>
</div>

### Send a channel message

<div class="rc-chat">
  <div class="rc-chat__user">
    <div class="rc-chat__bubble rc-chat__bubble--user">
      Send a message to the #releases channel: "v2.4.1 is live. Changelog is in the docs."
    </div>
  </div>
  <div class="rc-chat__ai">
    <div class="rc-chat__avatar">AI</div>
    <div class="rc-chat__bubble rc-chat__bubble--ai">
      <p>Message posted to #releases:</p>
      <p><em>"v2.4.1 is live. Changelog is in the docs."</em></p>
      <p>Sent at 3:12 PM. 4 team members are currently active in that channel.</p>
    </div>
  </div>
</div>

### Cross-channel search

<div class="rc-chat">
  <div class="rc-chat__user">
    <div class="rc-chat__bubble rc-chat__bubble--user">
      Has anyone mentioned the Apex Group deal in any channel in the last two weeks?
    </div>
  </div>
  <div class="rc-chat__ai">
    <div class="rc-chat__avatar">AI</div>
    <div class="rc-chat__bubble rc-chat__bubble--ai">
      <p>Found 6 mentions of Apex Group across 3 channels (Apr 28 – May 12):</p>
      <ul>
        <li><strong>#sales</strong> (3 mentions): Tyler noted they're in legal review. Bonnie asked if they need a custom SLA.</li>
        <li><strong>#exec-updates</strong> (2 mentions): Deal flagged as high-priority in weekly update.</li>
        <li><strong>#customer-success</strong> (1 mention): Onboarding plan drafted but not shared with Apex yet.</li>
      </ul>
      <p class="rc-chat__follow-up">Bonnie's custom SLA question hasn't been answered. Want me to surface that thread?</p>
    </div>
  </div>
</div>

## Tools called

| Step | Tool | Description |
|---|---|---|
| 1 | *(Message search)* | Search team chat history by keyword, channel, or participant |
| 2 | *(Message read)* | Retrieve a specific thread or conversation |
| 3 | *(Message send)* | Post a new message to a channel or direct conversation |

## Prerequisites

- RingCentral MCP server connected to your AI client
- Active RingCentral account with Team Messaging enabled
- Appropriate permissions to read and post in the target channels

!!! warning "Sending messages requires confirmation"
    Like all write actions, sending a team message is irreversible. Your AI client will typically ask for your approval before posting on your behalf.
