from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings
import httpx
import os
import uvicorn

mcp = FastMCP(
    "PhishBee",
    transport_security=TransportSecuritySettings(
        enable_dns_rebinding_protection=False,
    ),
)

PHISHBEE_URL = "https://phishbee-io.up.railway.app"

@mcp.tool()
async def check_url(url: str) -> str:
    """Check if a URL is phishing or safe using PhishBee."""
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.post(
                f"{PHISHBEE_URL}/api/check-url/",
                json={"url": url}
            )
            data = response.json()
            return f"URL: {data['url']}\nVerdict: {data['verdict']}\nScore: {data['score']}\nReasons: {', '.join(data['reasons'])}"
    except Exception as e:
        return f"Error: {str(e)}"

if name == "main":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(
        mcp.streamable_http_app(),
        host="0.0.0.0",
        port=port,
        forwarded_allow_ips="*",
        proxy_headers=True
    )
