import subprocess
import os
from pathlib import Path
from mcp.server import FastMCP
from src.resources import save_roast

def register_tools(mcp: FastMCP):
    
    @mcp.tool()
    def roast_file(file_path:str) -> str:
        """Read a source file and return its content for roasting."""
        path = Path(file_path)
        
        if not path.exists():
            return f"File not found: {file_path}"
        if not path.is_file():
            return f"That's a directory, not a file. Nice try."
        return path.read_text(encoding="utf-8")
        
    @mcp.tool()
    def record_roast(file_path: str, roast_level: str) -> str:
        """Save a completed roast to history. Call this after delivering a roast. roast_level should be 'savage' or 'brutal'."""
        save_roast(file_path, roast_level)
        return f"Roast recorded for {file_path} ({roast_level})."

    @mcp.tool()
    def roast_git_diff()-> str:
        """Fetches the currently staged git diff. Use this when the user wants to roast code they're about to commit. Returns the raw diff text showing added and removed lines."""
        try:
            result = subprocess.run(
                ["git", "diff", "--cached"],
                capture_output=True,
                text=True,
                timeout=10,
                stdin=subprocess.DEVNULL,
                env={**os.environ, "GIT_TERMINAL_PROMPT": "0"}
            )
        except subprocess.TimeoutExpired:
            return "git timed out. Is this a git repository?"
        except FileNotFoundError:
            return "git not found. Is git installed and on PATH?"
        if not result.stdout.strip():
            return "No staged changes found. Stage something first with git add."
        diff = result.stdout
        if len(diff) > 500:
            diff = diff[:500] + "\n\n[diff truncated at 500 chars]"
        return diff