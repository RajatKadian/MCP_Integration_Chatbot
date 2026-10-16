import asyncio

from mcp import Client
from mathserver import mcp as math_mcp
from weather import mcp as weather_mcp


async def main():

    # Math MCP server
    async with Client(math_mcp) as math_client:
        math_tools = await math_client.list_tools()

        print("Math Tools:")
        for tool in math_tools.tools:
            print(tool.name, repr(tool.description))

    # Weather MCP server
    async with Client(weather_mcp) as weather_client:
        weather_tools = await weather_client.list_tools()

        print("\nWeather Tools:")
        for tool in weather_tools.tools:
            print(tool.name, repr(tool.description))


asyncio.run(main())