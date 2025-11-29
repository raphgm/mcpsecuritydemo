# 🔐 MCP Security Demo

A hands-on demonstration of building secure Model Context Protocol (MCP) tools using FastMCP, showcasing input validation, least privilege principles, and safe inter-process communication.

## 🎯 Goal

Build a secure MCP tool that:
- ✅ Validates user input
- ✅ Exposes only necessary functionality (least privilege)
- ✅ Uses safe inter-process communication
- ✅ Demonstrates structured output

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## 🚀 Setup Instructions

### Step 1 — Set up your project and virtual environment

A virtual environment isolates dependencies for this demo, preventing conflicts with other Python packages.

```bash
mkdir mcpdemo
cd mcpdemo
python3 -m venv venv        # create isolated Python environment
source venv/bin/activate    # activate it
```

You should now see `(venv)` in your terminal prompt.

### Step 2 — Install FastMCP

FastMCP is the framework we'll use to create MCP servers and clients. It handles tool registration, secure execution, and communication.

```bash
python3 -m pip install --upgrade pip
python3 -m pip install fastmcp
```

Verify installation:

```bash
python3 -m pip show fastmcp
```

## 📁 Project Structure

```
mcpdemo/
├── server.py      # MCP server with secure tool implementation
├── client.py      # MCP client demonstrating tool calls
├── venv/          # Virtual environment (not tracked in git)
└── README.md      # This file
```

## 🔧 Implementation

### Server (`server.py`)

The server hosts your MCP tools. This is where security enforcement happens: validating input, limiting exposed functionality, and controlling output.

**Security Highlights:**
- ✅ Input is validated using regex whitelisting
- ✅ Only the `greet` tool is exposed (least privilege)
- ✅ Minimal dependencies (fastmcp only)
- ✅ STDIO transport ensures the server runs safely as a subprocess

```python
from fastmcp import FastMCP
import re

mcp = FastMCP("safe-greeter")

@mcp.tool
def greet(name: str) -> dict:
    """
    A simple greeting tool.
    Input is validated to allow only letters and spaces.
    """
    # SECURITY: Input validation prevents malicious input
    if not re.fullmatch(r"[A-Za-z ]{1,30}", name):
        return {"error": "Invalid name — only letters and spaces allowed."}
    return {"message": f"Hello, {name}!"}

if __name__ == "__main__":
    mcp.run()
```

### Client (`client.py`)

The client demonstrates how to interact with MCP servers securely, calling tools and handling structured results.

**How this enforces security:**
- ✅ The client cannot bypass input validation
- ✅ The server responds with structured content (CallToolResult) for predictable handling
- ✅ Only tools defined on the server are callable

## ▶️ Running the Demo

Activate your virtual environment and run the client:

```bash
source venv/bin/activate    # activate venv if not already
python3 client.py           # runs client, which auto-starts server via STDIO
```

### Expected Output

```
Valid input: CallToolResult(... {'message': 'Hello, Raphael!'} ...)
Bad input: CallToolResult(... {'error': 'Invalid name — only letters and spaces allowed.'} ...)
```

**Explanation:**
- ✅ **Valid input** → server accepted the input and returned a greeting
- ❌ **Bad input** → server rejected malicious input, demonstrating security in action

## 🔒 Security Concepts Demonstrated

| Concept | How Demonstrated |
|---------|------------------|
| **Input validation** | Regex whitelisting in `greet` tool |
| **Least privilege** | Only `greet` tool exposed |
| **Safe communication** | STDIO transport, subprocess isolation |
| **Predictable outputs** | Structured `CallToolResult` objects |
| **Minimal dependencies** | Only `fastmcp` required |

## 🎓 Key Takeaways

1. **Always validate input** — Never trust user input; use whitelisting when possible
2. **Expose minimal functionality** — Only provide the tools necessary for the task
3. **Use structured outputs** — Predictable response formats make error handling easier
4. **Leverage framework security** — FastMCP handles secure communication automatically
5. **Isolate execution** — STDIO transport runs the server as a separate, controlled subprocess

## 📚 Learn More

- [FastMCP Documentation](https://github.com/jlowin/fastmcp)
- [Model Context Protocol Specification](https://modelcontextprotocol.io)

## 📝 License

This is a demo project for educational purposes.

---

**Built with ❤️ using FastMCP**
