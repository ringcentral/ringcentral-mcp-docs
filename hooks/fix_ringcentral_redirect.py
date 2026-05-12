from pathlib import Path


SAFE_REDIRECT_JS = """\
console.log('extra.js loaded');
(function () {
  const legacyHost = 'ringcentral.github.io';
  const legacyPath = '/rc-unified-crm-extension';
  const canonicalHost = 'appconnect.labs.ringcentral.com';

  if (window.location.hostname !== legacyHost) {
    return;
  }

  if (!window.location.pathname.startsWith(legacyPath)) {
    return;
  }

  const nextUrl = new URL(window.location.href);
  nextUrl.hostname = canonicalHost;
  nextUrl.pathname = nextUrl.pathname.slice(legacyPath.length) || '/';

  if (nextUrl.href !== window.location.href) {
    window.location.replace(nextUrl.href);
  }
})();
"""


def on_post_build(config):
    extra_js = Path(config["site_dir"]) / "_rc" / "extra.js"
    extra_js.parent.mkdir(parents=True, exist_ok=True)
    extra_js.write_text(SAFE_REDIRECT_JS, encoding="utf-8")
