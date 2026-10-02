---
title: Test Link Variations
description: Testing different approaches to render markdown links within HTML blocks
hide:
  - navigation
  - toc
---

# Test Link Variations

Testing different HTML/markdown combinations to find the recipe that works with mkdocs-material's md_in_html extension.

## Version 1: Span with markdown="1" - inline, no blank lines

<span markdown="1">[Link 1](./test-link-variations.md)</span>

---

## Version 2: Span with markdown="1" - inline, with blank lines

<span markdown="1">

[Link 2](./test-link-variations.md)

</span>

---

## Version 3: Div with markdown="1" - block, no blank lines

<div markdown="1">[Link 3](./test-link-variations.md)</div>

---

## Version 4: Div with markdown="1" - block, with blank lines

<div markdown="1">

[Link 4](./test-link-variations.md)

</div>

---

## Version 5: Div with class and markdown="1" - block, with blank lines

<div class="rc-sol__link" markdown="1">

[Link 5](./test-link-variations.md)

</div>

---

## Version 6: Nested divs - outer has markdown="1"

<div markdown="1">
<div class="rc-sol__link">

[Link 6](./test-link-variations.md)

</div>
</div>

---

## Version 7: Nested divs - inner has markdown="1"

<div>
<div class="rc-sol__link" markdown="1">

[Link 7](./test-link-variations.md)

</div>
</div>

---

## Version 8: Nested divs - both have markdown="1"

<div markdown="1">
<div class="rc-sol__link" markdown="1">

[Link 8](./test-link-variations.md)

</div>
</div>

---

## Version 9: Div with style and markdown="1" - block, with blank lines

<div style="padding: 10px; border: 1px solid red;" markdown="1">

[Link 9](./test-link-variations.md)

</div>

---

## Version 10: Span inside div - outer has markdown="1"

<div markdown="1">
<span class="rc-sol__link">

[Link 10](./test-link-variations.md)

</span>
</div>

---

## Version 11: Span inside div - inner span has markdown="1"

<div>
<span class="rc-sol__link" markdown="1">

[Link 11](./test-link-variations.md)

</span>
</div>

---

## Version 12: Div with display: flex and markdown="1"

<div style="display: flex; gap: 10px;" markdown="1">

[Link 12a](./test-link-variations.md)

[Link 12b](./test-link-variations.md)

</div>

---

## Version 13: Plain markdown link (baseline)

[Link 13](./test-link-variations.md)

---

## Version 14: HTML a tag with href

<a href="./test-link-variations.md">Link 14</a>

---

## Version 15: Div with class, style, and markdown="1"

<div class="rc-sol__link" style="display: inline-block; padding: 10px; background: #f0f0f0;" markdown="1">

[Link 15](./test-link-variations.md)

</div>

---

## Version 16: Block quote style - multiple markdown links

<div markdown="1">

- [Link 16a](./test-link-variations.md)
- [Link 16b](./test-link-variations.md)
- [Link 16c](./test-link-variations.md)

</div>

---

## Version 17: Paragraph with markdown="1"

<p markdown="1">[Link 17](./test-link-variations.md)</p>

---

## Version 18: Card structure similar to your page - outer markdown="1"

<div class="rc-sol-card" markdown="1">
<div class="rc-sol__title">My Card</div>
<div class="rc-sol__desc">Description here</div>

[Link 18](./test-link-variations.md)

</div>

---

## Version 19: Card structure - inner link div with markdown="1"

<div class="rc-sol-card">
<div class="rc-sol__title">My Card</div>
<div class="rc-sol__desc">Description here</div>
<div class="rc-sol__link" markdown="1">

[Link 19](./test-link-variations.md)

</div>
</div>

---

## Version 20: Grid structure - outer markdown="1", nested card with inner link div markdown="1"

<div class="rc-solutions-grid" markdown="1">

<div class="rc-sol-card">
<div class="rc-sol__title">My Card</div>
<div class="rc-sol__link" markdown="1">

[Link 20](./test-link-variations.md)

</div>
</div>

</div>
