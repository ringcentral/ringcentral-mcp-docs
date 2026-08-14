---
title: Skill Library
description: Pre-built AI skills for RingCentral MCP servers.
hide:
  - toc
---

# Skill Library

Ready-to-use skills that give AI assistants structured workflows for common RingCentral tasks. Each skill defines trigger phrases, a tool-call workflow, and an output format — drop it into your AI platform's skill or plugin system to enable the workflow out of the box.

??? info "Learn how to install a skill"
    Every skill below is a single portable `SKILL.md` file. Use the **Download SKILL.md** button on a skill's page to save it, then load it into your AI platform of choice:

    === "Claude"

        1. Turn on **Code execution and file creation** — for Free/Pro/Max, in [Settings → Capabilities](https://claude.ai/settings/capabilities); for Team/Enterprise, an Owner enables it (plus **Skills**) in [Organization settings → Skills](https://claude.ai/admin-settings/skills).
        2. Go to [Customize → Skills](https://claude.ai/customize/skills) and click **+** → **Create skill**.
        3. Select **Upload a skill**.
        4. Zip the skill's folder — the folder itself, not the loose `SKILL.md` file — and upload the ZIP.
        5. Toggle the skill on, then test it with a prompt matching its trigger phrases.

        Custom skills are private to your account unless a Team/Enterprise Owner provisions or you share them. See the [full Claude skills guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude) for details.

    === "ChatGPT"

        1. In the sidebar select **Plugins**, then open the **Skills** tab (or go straight to [chatgpt.com/skills](https://chatgpt.com/skills)).
        2. Click **Create**, then **Upload from your computer**.
        3. Choose the skill's folder (or a ZIP of it) — ChatGPT scans it before enabling it.
        4. Once the scan clears, the skill is installed and ChatGPT uses it automatically when a prompt matches.

        Personal Skills require a Business, Enterprise, Healthcare, or Edu ChatGPT plan; Enterprise/Edu admins may need to turn Skills on for your role first. See the [full ChatGPT skills guide](https://help.openai.com/en/articles/20001066-skills-in-chatgpt) for details.

<div class="rc-solutions-grid">

  <a href="daily-communications-digest/" class="rc-sol-card">
    <span class="rc-sol__icon">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3zm7 11a7 7 0 0 1-14 0H3a9 9 0 0 0 8 8.94V23h2v-2.06A9 9 0 0 0 21 12h-2z"/></svg>
    </span>
    <div class="rc-sol__num">01</div>
    <div class="rc-sol__title">Daily Communications Digest</div>
    <span class="rc-sol__meta">Server: RingEX Phone</span>
    <p class="rc-sol__desc">Turn a day's calls, SMS, and voicemail on RingEX Phone into a prioritized follow-up report.</p>
    <span class="rc-sol__link">View skill →</span>
  </a>

  <a href="send-sms/" class="rc-sol-card">
    <span class="rc-sol__icon">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M20 2H4a2 2 0 0 0-2 2v18l4-4h14a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2zM6 9h12v2H6zm0-3h12v2H6z"/></svg>
    </span>
    <div class="rc-sol__num">02</div>
    <div class="rc-sol__title">Send SMS</div>
    <span class="rc-sol__meta">Server: RingEX Phone</span>
    <p class="rc-sol__desc">Text one person from a RingEX Phone number you own, with sender disambiguation and a mandatory send confirmation.</p>
    <span class="rc-sol__link">View skill →</span>
  </a>

  <a href="sms-inbox/" class="rc-sol-card">
    <span class="rc-sol__icon">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M4 4h16a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H8l-4.6 3.45A1 1 0 0 1 2 20.65V5a1 1 0 0 1 1-1zm3 5h10v2H7V9zm0 4h7v2H7v-2z"/></svg>
    </span>
    <div class="rc-sol__num">03</div>
    <div class="rc-sol__title">SMS Inbox</div>
    <span class="rc-sol__meta">Server: RingEX Phone</span>
    <p class="rc-sol__desc">Browse recent SMS/MMS conversations, pick one, and read it back as a formatted text-message stream.</p>
    <span class="rc-sol__link">View skill →</span>
  </a>

  <a href="voicemail-inbox/" class="rc-sol-card">
    <span class="rc-sol__icon">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3zm7 11a7 7 0 0 1-14 0H3a9 9 0 0 0 8 8.94V23h2v-2.06A9 9 0 0 0 21 12h-2z"/></svg>
    </span>
    <div class="rc-sol__num">04</div>
    <div class="rc-sol__title">Voicemail Inbox</div>
    <span class="rc-sol__meta">Server: RingEX Phone</span>
    <p class="rc-sol__desc">Browse recent voicemail, pick one, and read back the caller, time, and verified transcription.</p>
    <span class="rc-sol__link">View skill →</span>
  </a>

  <a href="fax-inbox/" class="rc-sol-card">
    <span class="rc-sol__icon">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M6 2h9l5 5v13a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2zm8 1.5V7h3.5L14 3.5zM8 12h8v1.5H8V12zm0 3h8v1.5H8V15zm0 3h5v1.5H8V18z"/></svg>
    </span>
    <div class="rc-sol__num">05</div>
    <div class="rc-sol__title">Fax Inbox</div>
    <span class="rc-sol__meta">Server: RingEX Phone</span>
    <p class="rc-sol__desc">Browse recent faxes and read back the sender, time, and cover-page text when available.</p>
    <span class="rc-sol__link">View skill →</span>
  </a>

  <a href="call-recap/" class="rc-sol-card">
    <span class="rc-sol__icon">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M6.6 10.8c1.6 3.2 4.4 6 7.6 7.6l2.5-2.5c.3-.3.8-.4 1.2-.3 1.3.4 2.7.7 4.1.7.7 0 1.2.5 1.2 1.2V21c0 .7-.5 1.2-1.2 1.2C10.5 22.4 1.6 13.5 1.6 2.9c0-.7.5-1.2 1.2-1.2h3.6c.7 0 1.2.5 1.2 1.2 0 1.4.2 2.8.7 4.1.1.4 0 .9-.3 1.2L6.6 10.8z"/></svg>
    </span>
    <div class="rc-sol__num">06</div>
    <div class="rc-sol__title">Call Recap</div>
    <span class="rc-sol__meta">Server: RingEX Phone</span>
    <p class="rc-sol__desc">Find a specific call and recap it with AI notes, transcript content, and recording status.</p>
    <span class="rc-sol__link">View skill →</span>
  </a>

  <a href="colleague-lookup/" class="rc-sol-card">
    <span class="rc-sol__icon">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 12a5 5 0 1 0 0-10 5 5 0 0 0 0 10zm0 2c-4.4 0-9 2.2-9 5v2h18v-2c0-2.8-4.6-5-9-5z"/></svg>
    </span>
    <div class="rc-sol__num">07</div>
    <div class="rc-sol__title">Colleague Lookup</div>
    <span class="rc-sol__meta">Server: RingEX Phone</span>
    <p class="rc-sol__desc">Find a colleague by name, department, title, or number, disambiguating when there's more than one match.</p>
    <span class="rc-sol__link">View skill →</span>
  </a>

  <a href="post-to-chat/" class="rc-sol-card">
    <span class="rc-sol__icon">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M2 3l20 9-20 9 4-9-4-9zm5.6 9l-2.2 5 12.5-5H7.6zm0-2h10.3L5.4 5l2.2 5z"/></svg>
    </span>
    <div class="rc-sol__num">08</div>
    <div class="rc-sol__title">Post to Chat</div>
    <span class="rc-sol__meta">Server: RingEX Chat</span>
    <p class="rc-sol__desc">Send a Team Chat post to a resolved person or channel, with destination resolution and a mandatory confirm step.</p>
    <span class="rc-sol__link">View skill →</span>
  </a>

  <a href="read-team-chat/" class="rc-sol-card">
    <span class="rc-sol__icon">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M4 4h16a1 1 0 0 1 1 1v11a1 1 0 0 1-1 1H9l-4.5 3.4A1 1 0 0 1 3 19.6V5a1 1 0 0 1 1-1zm3 5v2h10V9H7zm0 4v2h7v-2H7z"/></svg>
    </span>
    <div class="rc-sol__num">09</div>
    <div class="rc-sol__title">Read Team Chat</div>
    <span class="rc-sol__meta">Server: RingEX Chat</span>
    <p class="rc-sol__desc">Browse recent chats or jump to a named channel, and read a formatted post stream or catch-up digest.</p>
    <span class="rc-sol__link">View skill →</span>
  </a>

</div>

---

!!! tip "Using a skill"
    Each skill page includes the full `SKILL.md` source, pulled directly from the skill's source file. Copy it as-is into your AI platform's skill system, or adapt the tool names to match the MCP server you've connected.
