"""The adapter of breadcrumbs_grok: it gives the entry 'grok' of the harness table of core.py (identify and setup).
Run with breadcrumbs-common and this folder on PYTHONPATH."""
import unittest

from breadcrumbs import harness_case


class Adapter(harness_case.HarnessCase):
    KEY, LABEL, LAYER = "grok", "Grok", "grok"
    NAMES = ['grok', 'Grok CLI']
    SETUP = "grok mcp add breadcrumbs -- env PYTHONPATH=/x python -m breadcrumbs core mcp"


if __name__ == "__main__":
    unittest.main()
