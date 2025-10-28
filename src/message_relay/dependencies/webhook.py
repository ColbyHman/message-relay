import httpx
import logging
logger = logging.getLogger("discord")

async def send_webhook(url: str, payload: dict):
    """Send a payload to the specified webhook URL."""
    try:
        async with httpx.AsyncClient(verify=False) as client:
            response = await client.post(url, json=payload)
            response.raise_for_status()
    except httpx.HTTPError as e:
        logger.error(f"Failed to send webhook: {e}")