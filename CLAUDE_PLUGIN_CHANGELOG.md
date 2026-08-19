# Changelog

## 0.3.0

Consolidated the RingEX Chat skill set into a single canonical, non-overlapping group:

- Broadened `read-team-chat` to also read notes, tasks, and events (not just posts), added the
  Chat/Personal/Direct/Group/Team/Everyone taxonomy and explicit "no unread/read-receipt/search"
  guidance, and folded in person lookup via `find_person`.
- Broadened `post-to-chat` to also edit and delete posts via `manage_post`, and documented file/
  image attachment handling.
- Added skill: `manage-notes` — find, create, update, publish, lock/unlock, or delete a Team Chat note.
- Added skill: `manage-events` — find, create, update, or delete a Team Chat event.
- Added skill: `manage-teams` — team lifecycle, membership, favorites, and the Everyone chat.
- Added skill: `manage-webhooks` — create, activate, suspend, or delete an incoming webhook.
- Added skill: `manage-adaptive-cards` — compose, post, update, or delete an Adaptive Card within
  RingCentral's supported contract (v1.3, Action.OpenUrl/Action.Submit only).

## 0.2.0

- Added skill: `manage-tasks` — find, create, update, complete/reopen, or delete a RingCentral Team Chat task.

## 0.1.0

Initial release.

- Bundled two MCP servers: `phone` and `team-chat` (RingEX v1.1.0).
- Added skills: `call-recap`, `sms-inbox`, `voicemail-inbox`, `fax-inbox`, `daily-communications-digest`, `colleague-lookup`, `send-sms`, `read-team-chat`, `post-to-chat`.
