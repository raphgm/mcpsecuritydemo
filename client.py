import asyncio
from fastmcp import Client

async def main():
    # Pass the server script path; Client infers STDIO transport
    async with Client("./server.py") as client:
        # Valid input
        resp = await client.call_tool("greet", {"name": "Raphael"})
        print("Valid input:", resp)

        # Invalid input
        resp_bad = await client.call_tool("greet", {"name": "<script>alert(1)</script>"})
        print("Bad input:", resp_bad)

if __name__ == "__main__":
    asyncio.run(main())
