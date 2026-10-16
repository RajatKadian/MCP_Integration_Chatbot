from mcp.server import MCPServer


mcp = MCPServer(name="weather")

@mcp.tool()
def weather(city:str) -> str:
    """Get the weather of a city"""
    return f"The weather of {city} is sunny"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")


