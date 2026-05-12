from pathlib import Path
import shutil


FOOTER_REPLACEMENTS = {
    'href="https://mcp.labs.ringcentral.com/docs/releases/">Release notes</a>':
        'href="https://mcp.labs.ringcentral.com/docs/changelog/">Changelog</a>',
    'href="https://github.com/ringcentral/rc-unified-crm-extension" target="_blank" rel="noopener">GitHub</a>':
        'href="https://github.com/ringcentral/ringcentral-mcp-docs" target="_blank" rel="noopener">GitHub</a>',
}


SAFE_REDIRECT_JS = """\
console.log('extra.js loaded');
(function () {
  const legacyHost = 'ringcentral.github.io';
  const legacyPath = '/ringcentral-mcp-docs';
  const canonicalHost = 'mcp.labs.ringcentral.com';
  const canonicalPath = '/docs';

  if (window.location.hostname !== legacyHost) {
    return;
  }

  if (!window.location.pathname.startsWith(legacyPath)) {
    return;
  }

  const nextUrl = new URL(window.location.href);
  nextUrl.hostname = canonicalHost;
  const remainingPath = nextUrl.pathname.slice(legacyPath.length);
  nextUrl.pathname = canonicalPath + (remainingPath || '/');

  if (nextUrl.href !== window.location.href) {
    window.location.replace(nextUrl.href);
  }
})();
"""


def _inline_redirect_in_404(site_dir):
    not_found = site_dir / "404.html"
    if not not_found.exists():
        return

    html = not_found.read_text(encoding="utf-8")
    marker = "<meta charset=\"utf-8\">"
    script = f"{marker}\n      <script>{SAFE_REDIRECT_JS}</script>"
    if marker in html and SAFE_REDIRECT_JS not in html:
        not_found.write_text(html.replace(marker, script, 1), encoding="utf-8")


def _copy_site_contents(site_dir, target_dir):
    if target_dir.exists():
        shutil.rmtree(target_dir)
    target_dir.mkdir(parents=True)
    for item in site_dir.iterdir():
        if item.name in {"docs", "ringcentral-mcp-docs"}:
            continue

        target = target_dir / item.name
        if item.is_dir():
            shutil.copytree(item, target)
        else:
            shutil.copy2(item, target)


def _mirror_site_under_docs(site_dir):
    _copy_site_contents(site_dir, site_dir / "docs")
    _copy_site_contents(site_dir, site_dir / "docs" / "docs")
    _copy_site_contents(site_dir, site_dir / "ringcentral-mcp-docs")
    _copy_site_contents(site_dir, site_dir / "ringcentral-mcp-docs" / "docs")


def on_post_build(config):
    site_dir = Path(config["site_dir"])
    (site_dir / "CNAME").write_text("mcp.labs.ringcentral.com\n", encoding="utf-8")

    extra_js = Path(config["site_dir"]) / "_rc" / "extra.js"
    extra_js.parent.mkdir(parents=True, exist_ok=True)
    extra_js.write_text(SAFE_REDIRECT_JS, encoding="utf-8")

    for html_file in site_dir.rglob("*.html"):
        html = html_file.read_text(encoding="utf-8")
        updated = html
        for old, new in FOOTER_REPLACEMENTS.items():
            updated = updated.replace(old, new)
        if updated != html:
            html_file.write_text(updated, encoding="utf-8")

    _inline_redirect_in_404(site_dir)
    _mirror_site_under_docs(site_dir)
