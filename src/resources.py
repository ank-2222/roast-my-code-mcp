# resources.py
import json
from pathlib import Path
from mcp.server import FastMCP

HISTORY_FILE = Path(__file__).parent.parent / "data" / "history.json"

def load_history() -> list:
    """Load existing roast history from disk."""
    if not HISTORY_FILE.exists():
        return []
    text = HISTORY_FILE.read_text().strip()
    if not text:
        return []
    return json.loads(text)

def save_roast(file_path: str, roast_level: str):
    """Append a new roast entry to history — called after each roast."""
    HISTORY_FILE.parent.mkdir(parents=True, exist_ok=True)
    history = load_history()
    history.append({"file": file_path, "level": roast_level})
    HISTORY_FILE.write_text(json.dumps(history, indent=2))
    
def register_resources(mcp: FastMCP):

    @mcp.resource("roast://history")
    def get_roast_history() -> str:
        """Returns full roast history so AI can say 'still writing bad code!'"""
        history = load_history()
        if not history:
            return "No roasts yet. Your code is safe... for now."
        # Format it nicely for the AI to read
        lines = [f"- {r['file']} ({r['level']} roast)" for r in history]
        return "Past Roasts:\n" + "\n".join(lines)

    @mcp.resource("roast://leaderboard")
    def get_leaderboard() -> str:
        """Returns which files have been roasted most — the hall of shame."""
        history = load_history()
        counts = {}
        for entry in history:
            counts[entry["file"]] = counts.get(entry["file"], 0) + 1
        # Sort by roast count descending
        sorted_files = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        if not sorted_files:
            return "Leaderboard is empty. Write some bad code first."
        lines = [f"{i+1}. {f} — roasted {c} times" for i, (f, c) in enumerate(sorted_files)]
        return "🏆 Hall of Shame:\n" + "\n".join(lines)