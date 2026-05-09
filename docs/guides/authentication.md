# Authentication

RingCentral MCP servers use a two-layer authentication model. This page explains how each layer works and how to troubleshoot common auth issues.

---

## Layer 1 — RingCentral identity

All tools require an active RingCentral session. Authentication uses **OAuth 2.0** via your existing RingCentral account.

### How it works

When you connect an MCP server to your AI client, the client initiates an OAuth handshake with RingCentral. You'll be redirected to RingCentral's login page, and upon success, the client receives a session token that is automatically passed with every tool call.

### Token lifecycle

| Token | Lifetime | Refresh |
|-------|----------|---------|
| Access token | 60 minutes | Automatic (silent) |
| Refresh token | 7 days | Requires re-authentication |

If your refresh token expires, you'll need to re-authenticate by disconnecting and reconnecting the server in your AI client's integration settings.

---

## Layer 2 — CRM connection

Tools marked **⚠️ REQUIRES CRM CONNECTION** additionally require a linked CRM account. This is a separate OAuth flow with your CRM provider.

### Supported CRM platforms

- Salesforce
- HubSpot
- Zoho CRM
- Microsoft Dynamics 365 *(beta)*

### Connecting a CRM

=== "Via Claude.ai"

    1. In a conversation, ask: *"Connect my Salesforce account to RingCentral"*
    2. The assistant will guide you through the App Connect portal
    3. Complete the Salesforce OAuth login
    4. Return to the conversation — the assistant will confirm the connection

=== "Via App Connect Portal"

    1. Go to [app.ringcentral.com](https://app.ringcentral.com) → **App Connect**
    2. Click **Add CRM Integration**
    3. Choose your CRM platform
    4. Authorize with your CRM credentials
    5. Return to your AI client — the connection will be active

### Verifying CRM connection

```
Check my session status.
```

Look for `"crmConnected": true` and the `crmPlatform` name in the response.

---

## Required permissions

### RingCentral

Your RingCentral account needs the following permissions for full functionality:

| Permission | Required for |
|------------|-------------|
| `ReadCallLog` | `rcGetCallLogs` |
| `ReadAccounts` | `getSessionInfo` |

### CRM (Salesforce example)

| Object | Permissions |
|--------|-------------|
| Contact | Read, Create |
| Task / Activity | Read, Create |

---

## Troubleshooting

### "Authentication failed" on CRM tools

Your CRM session may have expired. Run:

```
Disconnect my CRM and reconnect it.
```

Or call `logout` then re-authenticate via the App Connect portal.

### "Insufficient permissions" error

Your RingCentral account or CRM user role may lack required permissions. Contact your RingCentral or CRM administrator to grant the permissions listed above.

### OAuth redirect not completing

- Ensure pop-ups are not blocked in your browser
- Try authenticating from the App Connect portal directly rather than through the AI client
- If using Claude Desktop, authentication may need to be completed in a browser window

---

!!! info "SSO environments"
    If your RingCentral account uses SSO (SAML/OIDC), the OAuth flow will redirect through your identity provider. Complete the SSO login as normal — the token exchange happens automatically afterward.
