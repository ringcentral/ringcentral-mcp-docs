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
