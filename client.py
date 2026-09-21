import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


server_params = StdioServerParameters(
    command=".venv\\Scripts\\python.exe",
    args=["server.py"],
)


async def main():

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:

            await session.initialize()

            tools = await session.list_tools()

            print("Available tools:")

            for tool in tools.tools:
                print("-", tool.name)

            result = await session.call_tool(
                "search_documents",
                {"query": "remote"}
            )

            print("\nSearch Result:")
            print(result.structured_content["result"])

            result = await session.call_tool(
                "list_files",
                {}
            )

            print("\nFiles:")
            print(result.structured_content["result"])

            result = await session.call_tool(
                "calculate",
                {"expression": "25 * 4"}
            )

            print("\nCalculation:")
            print(result.structured_content["result"])


if __name__ == "__main__":
    asyncio.run(main())