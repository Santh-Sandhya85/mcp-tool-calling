from pathlib import Path
from mcp.server.mcpserver import MCPServer

mcp = MCPServer("Document Assistant")

DOCUMENT_DIR = Path("documents")


@mcp.tool()
def hello(name: str) -> str:
    """Return a greeting."""
    return f"Hello, {name}!"


@mcp.tool()
def search_documents(query: str) -> list[str]:
    """Search local text documents for a keyword or phrase."""
    results = []

    for file_path in DOCUMENT_DIR.glob("*.txt"):
        content = file_path.read_text(encoding="utf-8")

        if query.lower() in content.lower():
            results.append(file_path.name)

    return results


@mcp.tool()
def list_files() -> list[str]:
    """List available text documents."""
    return [file.name for file in DOCUMENT_DIR.glob("*.txt")]


@mcp.tool()
def calculate(expression: str) -> str:
    """Calculate a simple mathematical expression."""
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception:
        return "Invalid calculation."


if __name__ == "__main__":
    mcp.run()