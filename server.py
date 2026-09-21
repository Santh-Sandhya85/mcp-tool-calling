from mcp.server.mcpserver import MCPServer

mcp = MCPServer("Document Assistant")


@mcp.tool()
def hello(name: str) -> str:
    """Return a greeting."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    mcp.run()