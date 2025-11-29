

# 🛡️ MCP Secure Greeter — Demo Project

A simple, security-focused demo showing how to build and run a **Model Context Protocol (MCP)** server and interact with it using the built-in MCP client.
This demo is designed for workshops, training sessions, and developer onboarding.

---

## 📌 **What This Demo Teaches**

This project demonstrates **secure tool invocation** using MCP:

### ✔️ What participants learn

* How MCP servers work
* How to validate user input safely
* How to run a server with STDIO transport
* How to use the built-in MCP client to call tools
* How “secure-by-default” validation prevents abuse

### ✔️ Why MCP Security Matters

MCP lets developers expose tools to LLMs safely.
But **AI models can be tricked into sending malicious inputs**, so tools must:

* Validate every input
* Reject suspicious patterns
* Only return safe content

This demo shows the **difference between safe and unsafe input**.

---

# ⚙️ Project Structure

```
mcpdemo/
│
├── server.py       # MCP server with input validation
├── client.py       # Python MCP client calling the server
├── requirements.txt
└── README.md
```

---

# 🚀 Step-by-Step Setup Guide

## 1️⃣ Create the project folder

```bash
mkdir mcpdemo
cd mcpdemo
```

---

## 2️⃣ Create a Python virtual environment (Mac)

Why?
A venv keeps dependencies isolated so the global system is not affected.

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Create `requirements.txt`

Why?
So the environment can install the exact packages the server and client need.

```bash
touch requirements.txt
```

Add this inside:

```
fastmcp==2.13.1
```

Install everything:

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Create the MCP Secure Greeter Server (`server.py`)

Why?
This file exposes an MCP tool called **greet**, validates names, and demonstrates safe error handling.

```python
from fastmcp import FastMCP, tool

app = FastMCP("safe-greeter")

def is_valid_name(name: str) -> bool:
    return name.replace(" ", "").isalpha()

@tool
def greet(name: str):
    if not is_valid_name(name):
        return {"error": "Invalid name — only letters and spaces allowed."}
    return {"message": f"Hello, {name}!"}

if __name__ == "__main__":
    app.run()
```

### 🔐 Why this matters

The `is_valid_name()` filter prevents:

* code injection
* prompt injection
* script tags
* SQL-like payloads
* shell commands

This demonstrates MCP’s **input-level security**.

---

## 5️⃣ Create the MCP Client (`client.py`)

Why?
To simulate how an AI model or external program would call your MCP server.

```python
import asyncio
from fastmcp.client import Client

async def main():
    async with Client(
        transport="python3 server.py"
    ) as client:
        resp = await client.call_tool("greet", {"name": "Raphael"})
        print("Valid input:", resp)

        resp = await client.call_tool("greet", {"name": "Raphael123!!"})
        print("Bad input:", resp)

asyncio.run(main())
```

---

#  6️⃣ Run the demo

## Start the client (which auto-starts the server)

```bash
python3 client.py
```

### Expected Output

```
Valid input: {"message": "Hello, Raphael!"}

Bad input: {"error": "Invalid name — only letters and spaces allowed."}
```

You will also see FastMCP start up:

```
FastMCP 2.13.1
Server: safe-greeter
Transport: STDIO
```

---

# 🧠 What Makes This a Good MCP Security Demo?

### 🔒 1. Input validation is clear

The demo visually shows:

* Good input → Accepted
* Bad input → Rejected

Perfect for live explanation.

### 🧪 2. Easy to modify

Participants can try breaking it with:

* `"Robert'); DROP TABLE Students;--"`
* `"<script>alert(1)</script>"`
* `"$(rm -rf ~)"`

All will be safely rejected.

### 🚀 3. Demonstrates real-world MCP usage

This is exactly how MCP tools are integrated into:

* AI agents
* ChatGPT custom tools
* Automated systems
* Secure pipelines

---

# 📚 Additional Learning Ideas

You can extend this demo with:

* Logging middleware
* Rate limiting
* Role-based access
* Token-based authorization
* More validated tools (e.g., email validator, file-safe analyzer)

---

# 🙌 Credits

Created for MCP Security Workshops by **Raphael Gab-Momoh**.

---

