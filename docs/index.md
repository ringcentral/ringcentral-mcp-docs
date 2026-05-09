# RingCentral MCP Servers

Welcome to the developer documentation for RingCentral's **Model Context Protocol (MCP) servers**. These servers expose RingCentral platform capabilities — telephony data, CRM integrations, and more — as structured tools that any MCP-compatible AI client (Claude, Cursor, Windsurf, etc.) can call directly.

---

## Available servers

<div class="card-grid" markdown>
<div class="card" markdown>

### 🔧 RingCentral Labs MCP

**URL:** `https://mcp.labs.ringcentral.com`

Experimental platform tools built by the RingCentral Labs team. Ideal for prototyping and developer exploration.

[View server →](servers/rc-labs-mcp.md)

</div>
<div class="card" markdown>

### 🔗 App Connect (Unified CRM)

**URL:** `https://unified-crm-extension.labs.ringcentral.com/mcp`

Bridges RingCentral telephony with your CRM platform. Sync call logs, look up contacts, and manage CRM records from any AI assistant.

[View server →](servers/app-connect.md)

</div>
</div>

---

## Quick navigation

| I want to… | Go to |
|---|---|
| Get started in 5 minutes | [Quickstart guide](guides/quickstart.md) |
| Connect a server to Claude | [Connecting to Claude](guides/connecting-to-claude.md) |
| Log calls to my CRM automatically | [CRM integration workflow](guides/crm-workflow.md) |
| Browse all App Connect tools | [App Connect reference](tools/app-connect/get-session-info.md) |
| Understand authentication | [Authentication](guides/authentication.md) |

---

## What is MCP?

The **Model Context Protocol** is an open standard that lets AI models communicate with external tools and data sources over a well-defined JSON-RPC interface. Each MCP server advertises a list of *tools* — typed function signatures with names, descriptions, and parameter schemas — that an AI client can discover and invoke.

```
AI Client  ──────── tools/list ──────────▶  MCP Server
           ◀──── tool definitions ────────
           ──────── tools/call ──────────▶
           ◀────── tool result ───────────
```

RingCentral's MCP servers let AI assistants take real actions — fetching call records, finding contacts, logging activity — without requiring custom integrations for every AI product.

---

!!! tip "New to MCP?"
    Start with the [Quickstart guide](guides/quickstart.md) to connect your first server in under 5 minutes.
