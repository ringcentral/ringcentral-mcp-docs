# Customer Engagement

Reach customers faster and stay on top of inbound activity. Initiate calls via RingOut, send and read SMS threads, and triage voicemails — all through your AI client.

## What it does

The RingCentral MCP server gives your AI the ability to act on your communications stack, not just read from it. Your AI can place outbound calls, send SMS messages, read incoming texts, and surface unheard voicemails — enabling fully conversational customer engagement workflows without switching between apps.

## Examples

### Make a call via RingOut

<div class="rc-chat">
  <div class="rc-chat__user">
    <div class="rc-chat__bubble rc-chat__bubble--user">
      Call Sarah Chen at Brightpath using my RingCentral number.
    </div>
  </div>
  <div class="rc-chat__ai">
    <div class="rc-chat__avatar">AI</div>
    <div class="rc-chat__bubble rc-chat__bubble--ai">
      <p>Initiating RingOut to Sarah Chen at Brightpath Inc.</p>
      <ul>
        <li>Dialing: +1 415-554-9823</li>
        <li>Using your extension x3041</li>
        <li>Your desk phone will ring first, then connect you</li>
      </ul>
      <p>Call connecting now.</p>
    </div>
  </div>
</div>

### Send an SMS

<div class="rc-chat">
  <div class="rc-chat__user">
    <div class="rc-chat__bubble rc-chat__bubble--user">
      Send an SMS to Marcus Okonkwo: "Hi Marcus, just following up on our call yesterday. Let me know if you have any questions."
    </div>
  </div>
  <div class="rc-chat__ai">
    <div class="rc-chat__avatar">AI</div>
    <div class="rc-chat__bubble rc-chat__bubble--ai">
      <p>Message sent to Marcus Okonkwo (+1 510-223-7741).</p>
      <p><em>"Hi Marcus, just following up on our call yesterday. Let me know if you have any questions."</em></p>
      <p>Sent at 10:47 AM. This is your 4th SMS exchange with Marcus. His last reply was 3 days ago.</p>
    </div>
  </div>
</div>

### Triage voicemails

<div class="rc-chat">
  <div class="rc-chat__user">
    <div class="rc-chat__bubble rc-chat__bubble--user">
      What voicemails have I received today? Summarize each one.
    </div>
  </div>
  <div class="rc-chat__ai">
    <div class="rc-chat__avatar">AI</div>
    <div class="rc-chat__bubble rc-chat__bubble--ai">
      <p>3 voicemails received today:</p>
      <ul>
        <li><strong>9:02 AM — Brightpath Inc.</strong> — "Calling about the proposal you sent. Please call back when you can." (41 sec)</li>
        <li><strong>11:18 AM — Unknown number</strong> — No message left.</li>
        <li><strong>2:34 PM — Diego Reyes</strong> — "Available Thursday afternoon if you want to reconnect." (28 sec)</li>
      </ul>
      <p class="rc-chat__follow-up">Want me to help prioritize follow-ups or draft reply messages?</p>
    </div>
  </div>
</div>

## Tools called

| Step | Tool | Description |
|---|---|---|
| 1 | `rcGetCallLogs` | Identify missed calls, voicemails, or recent activity |
| 2 | *(SMS read)* | Retrieve inbound/outbound SMS threads |
| 3 | *(SMS send)* | Compose and send an SMS message |
| 4 | *(RingOut)* | Initiate an outbound call via RingCentral |

## Prerequisites

- RingCentral MCP server connected to your AI client
- Active RingCentral account with SMS and calling permissions
- For RingOut: a registered device on your RingCentral extension

!!! warning "Outbound actions require confirmation"
    Prompts that send messages or place calls are irreversible. Most AI clients will ask for your approval before executing any tool that writes or acts.
