#!/usr/bin/env python3
"""
mcp.py - Run configuration-driven MCP servers.

This is an adapter module that delegates to the original implementation
in khive.cli.khive_mcp.
"""

from __future__ import annotations

# Import the original implementation
from khive.cli.khive_mcp import main as original_main


def cli_entry() -> None:
    """
    Entry point for the mcp command.

    This function delegates to the original implementation.
    """
    original_main()


if __name__ == "__main__":
    cli_entry()
