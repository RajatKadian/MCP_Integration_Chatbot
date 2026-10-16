import asyncio

from dotenv import load_dotenv
from langchain.mcp import MCPAdapter
from langchain.agents import create_agent
from langchain_groq import ChatGroq

load_dotenv()


async def main():

    # -----------------------------
    # 1. Connect to MCP servers
    # -----------------------------
    adapter = MCPAdapter(
        {
            "math": {
                "command": "python",
                "args": ["mathserver.py"],
                "transport": "stdio",
            },

            "weather": {
                "url": "http://localhost:8000/mcp",
                "transport": "http",
            },
        }
    )

    # -----------------------------
    # 2. Get tools from MCP servers
    # -----------------------------
    tools = await adapter.list_tools()

    print("\nAvailable tools:")
    for tool in tools:
        print("-", tool.name)

    # -----------------------------
    # 3. Create Groq model
    # -----------------------------
    model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

    # -----------------------------
    # 4. Create agent
    # -----------------------------
    agent = create_agent(
        model=model,
        tools=tools
    )

    # -----------------------------
    # 5. Ask math question
    # -----------------------------
    response = await agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                     "content": """
                What is the weather in Chandigarh?
                Also calculate 25 * 4 and then add 10 to the result.
                """
                }
            ]
        }
    )

    print("\nMath Response:")
    print(response["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())