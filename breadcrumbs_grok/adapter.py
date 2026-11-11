"""The adapter of the package breadcrumbs_grok: Grok gives its entry of the harness table of core.py.
ports.load() imports this module by the name of its package (breadcrumbs_*); no module imports it.

The setup line is the one of the document of the Grok CLI, "Adding a server":
    grok mcp add filesystem -- npx -y @modelcontextprotocol/server-filesystem /path/to/dir
    (https://docs.x.ai/build/features/mcp-servers, the markdown at https://docs.x.ai/build/features/mcp-servers.md)
"""
import shlex

from breadcrumbs import ports

if ports.layer("grok", __file__):
    ports.harness("grok", "Grok", ("grok",), lambda cmd: "grok mcp add breadcrumbs -- " + shlex.join(cmd), order=50)
