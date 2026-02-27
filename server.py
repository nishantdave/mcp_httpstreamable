#server.py
from mcp.server.fastmcp import FastMCP

#Create an MCP server
mcp = FastMCP("Demo")

#Add an additional tool
@mcp.tool()
def greeting(name: str) -> str:
    "Send a greeting to the user"
    return f"Hello, {name}! Welcome to the MCP server demo."

if __name__ == "__main__":
    #Start the server
    mcp.run(transport="streamable-http")
