# Servers Overview

RingCentral currently publishes two MCP servers. Both implement the [Model Context Protocol](https://modelcontextprotocol.io) specification and are reachable over HTTPS using Server-Sent Events (SSE) transport.

---

## Server registry

| Server | URL | Status | Tools |
|--------|-----|--------|-------|
| RingCentral MCP | `https://mcp.labs.ringcentral.com` | 🟡 Labs / Beta | — |
| App Connect | `https://unified-crm-extension.labs.ringcentral.com/mcp` | 🟢 Available | 9 |

---

## Transport & protocol

Both servers use **SSE (Server-Sent Events)** transport over HTTPS, which is the recommended transport for remote MCP servers. Clients connect by sending an HTTP `POST` to the server URL with a JSON-RPC 2.0 body.

```bash
# Discover tools on any server
curl -X POST https://<server-url> \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}'
```

---

## Authentication model

- **RingCentral MCP** — no authentication required for tool discovery; some tools may require a valid RingCentral session.
- **App Connect** — tools marked ⚠️ **REQUIRES CRM CONNECTION** require the user to have authenticated with both RingCentral and a supported CRM platform.

---

## Versioning policy

Labs servers follow a rolling-release model. Breaking changes will be announced in the [Changelog](../changelog.md) with at least 14 days notice. Stable tools are versioned via `api-version` query parameter where applicable.
