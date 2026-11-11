# breadcrumbs-grok

The Grok adapter of breadcrumbs. It gives `identify` (the client name that means Grok) and `setup` (the line that adds the breadcrumbs MCP server to Grok).

- Needs: breadcrumbs-common.
- Use: `python -m breadcrumbs core setup grok` prints the setup line.
- Test: `PYTHONPATH=../breadcrumbs-common:. python -m unittest discover -s tests`.

MIT licence. Part of breadcrumbs-agency.
