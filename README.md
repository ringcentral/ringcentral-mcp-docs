# RingCentral MCP Server Documentation

MkDocs-Material documentation site for RingCentral's MCP servers.

## Local development

```bash
# Install dependencies
pip install -r requirements.txt

# Serve with live reload
mkdocs serve

# Build static site
mkdocs build
```

The dev server runs at **http://127.0.0.1:8000** by default.

## Deploy to GitHub Pages

```bash
mkdocs gh-deploy
```

## Project structure

```
rc-mcp-docs/
├── mkdocs.yml                   # Site config, nav, theme
├── requirements.txt
└── docs/
    ├── index.md                 # Home page
    ├── changelog.md
    ├── stylesheets/
    │   └── extra.css            # RingCentral brand overrides
    ├── servers/
    │   ├── index.md             # Server registry overview
    │   └── app-connect.md
    ├── tools/
    │   ├── app-connect.md        # Consolidated tools reference
    │   ├── ringex-phone.md       # Consolidated tools reference
    │   ├── ringex-chat.md        # Consolidated tools reference
    │   └── ringex-admin.md       # Consolidated tools reference
    └── guides/
        ├── quickstart.md
        ├── connecting-to-claude.md
        ├── crm-workflow.md
        └── authentication.md
```

## Contributing

1. Add or edit markdown files under `docs/`
2. Update `nav:` in `mkdocs.yml` for new pages
3. Run `mkdocs serve` to preview
4. Open a PR — the CI pipeline will build and validate

## License

© RingCentral, Inc. All rights reserved.
