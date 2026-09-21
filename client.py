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

            while True:

                query = input("\nEnter a query (or type 'exit'): ")

                if query.lower() == "exit":
                    break

                if query.lower().startswith("search "):

                    search_query = query[7:]

                    result = await session.call_tool(
                        "search_documents",
                        {"query": search_query}
                    )

                elif query.lower() == "list files":

                    result = await session.call_tool(
                        "list_files",
                        {}
                    )

                elif query.lower().startswith("calculate "):

                    expression = query[10:]

                    result = await session.call_tool(
                        "calculate",
                        {"expression": expression}
                    )

                else:

                    print("Unknown command.")
                    continue

                print("\nResult:")
                print(result.structured_content["result"])


if __name__ == "__main__":
    asyncio.run(main())