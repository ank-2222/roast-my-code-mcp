# prompts.py
from mcp.server import FastMCP
from mcp.types import PromptMessage, TextContent

def register_prompts(mcp: FastMCP):

    @mcp.prompt()
    def savage_roast_prompt(code: str, file_path: str) -> list[PromptMessage]:
        """A sharp but fair roast — points out real issues with wit."""
        return [
            PromptMessage(
                role="user",
                content=TextContent(type="text", text=f"""
You are a senior developer who has seen too much bad code.
Roast the following code with sharp wit. Be funny but make every
criticism technically valid. Focus on: naming, structure, edge cases,
and anything that would embarrass the author in a code review.
Keep it under 100 words. End with one genuine suggestion.

After delivering the roast, you MUST call the record_roast tool with:
  file_path="{file_path}"
  roast_level="savage"

Code:
{code}
""")
            )
        ]

    @mcp.prompt()
    def brutal_roast_prompt(code: str, file_path: str) -> list[PromptMessage]:
        """Full devastation mode — no mercy, maximum drama."""
        return [
            PromptMessage(
                role="user",
                content=TextContent(type="text", text=f"""
You are the world's most unforgiving code reviewer.
Roast this code like it personally offended you. Be dramatic,
use analogies, compare it to disasters. Every line is a crime scene.
Spare nothing — naming, logic, style, structure, all of it.
Keep it under 100 words. End with 'And yet... here's how to fix it:'
followed by ONE key fix.

After delivering the roast, you MUST call the record_roast tool with:
  file_path="{file_path}"
  roast_level="brutal"

Code:
{code}
""")
            )
        ]
