from mcp.server import MCPServer

mcp = MCPServer(name="math")

@mcp.tool()
def add(a:int, b:int) -> int:
    """Add two numbers together yeahhhhhh"""
    return a + b

@mcp.tool()
def subtract(a:int, b:int) -> int:
    """Subtract two numbers........................"""
    return a - b

@mcp.tool()
def multiply(a:int, b:int) -> int:
    """Multiply two numbers oh yeahhhhhh"""
    return a * b

if __name__ == "__main__":
    mcp.run(transport="stdio")
    print("Math server is running on port 8000")



