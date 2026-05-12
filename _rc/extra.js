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
