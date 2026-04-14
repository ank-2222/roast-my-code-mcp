import sys
import os
from pathlib import Path

# Fix module resolution when launched via absolute path by MCP
sys.path.insert(0, str(Path(__file__).parent))

from mcp.server import FastMCP
from src.tools import register_tools
from src.resources import register_resources
from src.prompts import register_prompts

transport = os.environ.get("TRANSPORT", "stdio")

if transport == "streamable-http":
    mcp = FastMCP("roast-my-code", host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
else:
    mcp = FastMCP("roast-my-code")

register_tools(mcp)
register_resources(mcp)
register_prompts(mcp)

if __name__ == "__main__":
    mcp.run(transport=transport)
