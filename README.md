# roast-my-code

An MCP server that roasts your code with savage wit. Point it at a file or your staged git diff and get a technically-valid, brutally funny code review.

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

## Setup

Requires Python 3.12+ and [uv](https://github.com/astral-sh/uv).

```bash
uv sync
```

### Claude Desktop config

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "roast-my-code": {
      "command": "uv",
      "args": ["run", "python", "main.py"],
      "cwd": "/path/to/mcptool"
    }
  }
}
```
