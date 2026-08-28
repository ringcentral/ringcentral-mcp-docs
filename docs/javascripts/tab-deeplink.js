/*
 * Deep-linking for pymdownx tabbed blocks (ChatGPT / Claude / Codex setup tabs, etc).
 *
 * Material's built-in tab-restore script only recognizes hashes that match the
 * auto-generated input id (e.g. "#__tabbed_1_2"), which isn't something anyone
 * can predict or hand-write a link to. It also gets overridden by the
 * "content.tabs.link" cross-page sync, which remembers the last tab label a
 * visitor picked (via localStorage) and re-applies it on every page load —
 * so even a correct hash link can get silently clobbered.
 *
 * This adds a readable "#tab-<Label>" convention, e.g.:
 *   https://mcp.labs.ringcentral.com/docs/servers/ringex-chat-setup/#tab-Claude
 *
 * It matches case-insensitively against each tab's visible label text and
 * runs after the page has parsed (so it always wins over the localStorage
 * sync above it), selecting the matching tab in every tabbed-set on the page.
 */
(function () {
  function selectTabFromHash() {
    var match = window.location.hash.match(/^#tab-(.+)$/);
    if (!match) return;

    var wanted = decodeURIComponent(match[1]).trim().toLowerCase();
    var found = null;

    document.querySelectorAll(".tabbed-set").forEach(function (set) {
      var labels = set.querySelector(".tabbed-labels");
      if (!labels) return;

      Array.prototype.forEach.call(labels.getElementsByTagName("label"), function (label) {
        if (label.textContent.trim().toLowerCase() === wanted) {
          var input = document.getElementById(label.htmlFor);
          if (input) {
            input.checked = true;
            if (!found) found = label;
          }
        }
      });
    });

    if (found) {
      found.scrollIntoView({ block: "center" });
    }
  }

  selectTabFromHash();
  window.addEventListener("hashchange", selectTabFromHash);
})();
