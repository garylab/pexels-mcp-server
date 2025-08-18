import os
import ssl
from typing import Dict, Any
import certifi
import aiohttp
from pydantic import BaseModel

PEXELS_API_KEY = str.strip(os.getenv("PEXELS_API_KEY", ""))
AIOHTTP_TIMEOUT = int(os.getenv("AIOHTTP_TIMEOUT", "15"))


async def pexels_get(url: str, request: BaseModel | None) -> Dict[str, Any]:
    params = request.model_dump(exclude_none=True) if request is not None else None
    headers = {
        "Authorization": PEXELS_API_KEY,
    }

    ssl_context = ssl.create_default_context(cafile=certifi.where())
    connector = aiohttp.TCPConnector(ssl=ssl_context)

    timeout = aiohttp.ClientTimeout(total=AIOHTTP_TIMEOUT)
    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        async with session.get(url, headers=headers, params=params) as response:
            response.raise_for_status()
            return await response.json()


def build_photos_url(path: str) -> str:
    return f"https://api.pexels.com/v1/{path}"


def build_videos_url(path: str) -> str:
    return f"https://api.pexels.com/videos/{path}"
