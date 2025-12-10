"""Shared MCP instance used by server, tools and resources.

Creating `mcp` in a separate module prevents double-import problems when
running `python server.py` (which would otherwise execute server as
`__main__` and then import `server` again from other modules).
"""
from mcp.server.fastmcp import FastMCP


mcp = FastMCP("local-file-mcp", json_reponse=True)
"""Shared MCP instance used by server, tools and resources.

Creating `mcp` in a separate module prevents double-import problems when
running `python server.py` (which would otherwise execute server as
`__main__` and then import `server` again from other modules).
"""
from mcp.server.fastmcp import FastMCP


mcp = FastMCP("local-file-mcp", json_reponse=True)
