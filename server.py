from fastmcp import FastMCP
import re

# Initialize MCP server
mcp = FastMCP("safe-greeter")

# Define a secure tool
@mcp.tool
def greet(name: str) -> dict:
    # SECURITY: whitelist input (letters and spaces only)
    if not re.fullmatch(r"[A-Za-z ]{1,30}", name):
        return {"error": "Invalid name — only letters and spaces allowed."}
    return {"message": f"Hello, {name}!"}

if __name__ == "__main__":
    mcp.run()  # default STDIO transport inferred automatically
