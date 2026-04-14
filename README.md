# roast-my-code

An MCP server that roasts your code with savage wit. Point it at a file or your staged git diff and get a technically-valid, brutally funny code review.

## Run Modes

| Feature | Local (stdio) | Render (SSE) |
|---------|:---:|:---:|
| `roast_file` | yes | yes |
| `roast_git_diff` | yes | no (no local git repo) |
| Roast history | yes, persists | yes, resets after redeploy |
| History after 15 min idle | yes | lost (free tier sleeps) |

---

## Running Locally

Requires Python 3.12+ and [uv](https://github.com/astral-sh/uv).

**1. Install dependencies**

```bash
uv sync
```

**2. Connect to Claude Desktop**

Find your config file:
- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

Add this entry (replace the path with your actual path):

```json
{
  "mcpServers": {
    "roast-my-code": {
      "command": "uv",
      "args": ["run", "python", "main.py"],
      "cwd": "C:/path/to/mcptool"
    }
  }
}
```

Restart Claude Desktop. The server runs as a local `stdio` process — git and history both work fully.

---


## Connect to Claude Desktop

Once deployed, add this to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "roast-my-code": {
      "url": "https://roast-my-code.onrender.com/mcp"
    }
  }
}
```

> **Note:** The free Render tier sleeps after 15 minutes of inactivity. The first request after idle will take ~30 seconds to cold-start. Roast history is lost on each redeploy or sleep cycle.

---

## Tools

| Tool | Description |
|------|-------------|
| `roast_file` | Read a source file and return its content for roasting |
| `roast_git_diff` | Fetch the currently staged git diff for roasting |
| `record_roast` | Save a completed roast to history |

## Resources

| Resource | Description |
|----------|-------------|
| `roast://history` | Full roast history — so the AI can call out repeat offenders |
| `roast://leaderboard` | Hall of shame: files roasted most often |

## Prompts

| Prompt | Description |
|--------|-------------|
| `savage_roast_prompt` | Sharp but fair — real issues, wit included |
| `brutal_roast_prompt` | Full devastation mode, no mercy |

