---
title: Send SMS
description: Sends a person-to-person SMS via RingEX Phone, with sender disambiguation and mandatory send confirmation.
---

# Send SMS

[:material-download: Download SKILL.md](../assets/skill-downloads/send-sms.md.txt){ .md-button .md-button--primary download="send-sms-SKILL.md" }

**Skill ID:** `send-sms`
**Server:** [RingEX Phone](../servers/ringex-phone.md)

Sends a single SMS on behalf of the authenticated user — resolving the recipient, asking which number to send from when more than one is available, and confirming the exact sender, recipient, and text before calling the write tool. The full skill source below is pulled directly from its `SKILL.md` file, so it always reflects the current version.

---

--8<-- "send-sms/SKILL.md:body"

---

[← Back to Skill Library](index.md)
