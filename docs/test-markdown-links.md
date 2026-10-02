---
title: Test - Markdown Links with Inline Spans
description: Testing markdown conversion approach
---

# Test: Markdown Links with Inline Spans

Testing the new approach: keeping `<span>` elements inline and adding `markdown="inline"` with markdown link syntax.

## Claude Cards (from docs/solutions/claude.md)

<div class="rc-solutions-grid rc-solutions-grid--iconbadge">

  <a href="https://claude.ai/directory/ringcentral-chat" class="rc-sol-card" target="_blank" rel="noopener">
    <span class="rc-sol__icon"><i class="fa-solid fa-comment-dots"></i></span>
    <div class="rc-sol__title">RingCentral Chat connector</div>
    <p class="rc-sol__desc">Team messaging in Claude — catch up on chats, search history, and post updates on your behalf.</p>
    <span class="rc-sol__link">Set up →</span>
    <div markdown="1" style="display: none;">
[Claude Chat Connector](https://claude.ai/directory/ringcentral-chat)
    </div>
  </a>

</div>

## ChatGPT Cards (from docs/solutions/chatgpt.md)

<div class="rc-solutions-grid rc-solutions-grid--iconbadge">

  <a href="https://chatgpt.com/plugins/plugin_asdk_app_6a5163accce48191ab3fac53d63cb197?q=ringcentral" class="rc-sol-card" target="_blank" rel="noopener">
    <span class="rc-sol__icon"><i class="fa-solid fa-phone"></i></span>
    <div class="rc-sol__title">RingCentral Phone plugin</div>
    <p class="rc-sol__desc">Call logs, AI call notes, SMS, fax, and voicemail — directly inside ChatGPT. No manual setup required.</p>
    <span class="rc-sol__link">Install plugin →</span>
    <div markdown="1" style="display: none;">
[ChatGPT Phone Plugin](https://chatgpt.com/plugins/plugin_asdk_app_6a5163accce48191ab3fac53d63cb197?q=ringcentral)
    </div>
  </a>

</div>

## Test Notes

- Check if cards render with correct layout (side-by-side)
- Verify link text appears clickable
- Inspect if mkdocs processes the markdown links for validation
- Confirm no layout breaking from span elements
