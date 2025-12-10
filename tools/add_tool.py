from mcp_app import mcp


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b
