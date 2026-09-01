/*
 * Copy-to-clipboard buttons for server endpoint URLs (.rc-copy).
 *
 * Each button carries the text to copy in a `data-copy` attribute. On click,
 * we write that text to the clipboard and toggle a `.rc-copy--copied` class
 * for ~1.4s so the icon swaps from a copy glyph to a checkmark (see
 * stylesheets/extra.css for the two-icon swap rules).
 *
 * Delegated at the document level so it keeps working across Material's
 * instant-loading page swaps without needing to be re-initialized per page.
 */
(function () {
  var RESET_DELAY_MS = 1400;

  function fallbackCopy(text) {
    var textarea = document.createElement("textarea");
    textarea.value = text;
    textarea.setAttribute("readonly", "");
    textarea.style.position = "absolute";
    textarea.style.left = "-9999px";
    document.body.appendChild(textarea);
    textarea.select();
    try {
      document.execCommand("copy");
    } catch (err) {
      /* no-op: nothing more we can do */
    }
    document.body.removeChild(textarea);
  }

  function markCopied(button) {
    button.classList.add("rc-copy--copied");
    window.clearTimeout(button._rcCopyTimeout);
    button._rcCopyTimeout = window.setTimeout(function () {
      button.classList.remove("rc-copy--copied");
    }, RESET_DELAY_MS);
  }

  document.addEventListener("click", function (event) {
    var button = event.target.closest(".rc-copy");
    if (!button) return;

    var text = button.getAttribute("data-copy");
    if (!text) return;

    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () {
        markCopied(button);
      }, function () {
        fallbackCopy(text);
        markCopied(button);
      });
    } else {
      fallbackCopy(text);
      markCopied(button);
    }
  });
})();
