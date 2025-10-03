"""Simple MCP server example.

This server exposes two example tools for demonstration.
"""
from __future__ import annotations

from datetime import datetime

from fastmcp import FastMCP


app = FastMCP(name="docker-mcp-server", description="Sample MCP server running in Docker")


@app.tool()
def hello(name: str) -> str:
    """Return a friendly greeting for the provided name."""
    return f"Merhaba, {name}! MCP sunucusuna hoş geldiniz."


@app.tool()
def server_time() -> str:
    """Return the current UTC time."""
    return datetime.utcnow().isoformat() + "Z"


if __name__ == "__main__":
    app.run()
