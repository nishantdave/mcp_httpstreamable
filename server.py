#server.py
from mcp.server.fastmcp import FastMCP

#Create an MCP server
mcp = FastMCP("Demo", host="0.0.0.0", port=8000)

#Add an additional tool
@mcp.tool()
def greeting(name: str) -> str:
    "Send a greeting to the user"
    return f"Hello, {name}! Welcome to the MCP server demo."

if __name__ == "__main__":
    #Start the server with custom host and port. Specify 0.0.0.0 to allow external access.
    mcp.run(transport="streamable-http")
    