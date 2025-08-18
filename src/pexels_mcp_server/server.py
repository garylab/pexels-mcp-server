from typing import Any, List, Sequence
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent, ImageContent, EmbeddedResource
from dotenv import load_dotenv
import json

from .core import (
    PEXELS_API_KEY,
    pexels_get,
    build_photos_url,
    build_videos_url,
)
from .enums import PexelsTools
from .schemas import (
    PhotosSearchRequest,
    PhotosCuratedRequest,
    PhotoGetRequest,
    VideosSearchRequest,
    VideosPopularRequest,
    VideoGetRequest,
    CollectionsFeaturedRequest,
    CollectionsMediaRequest,
)

load_dotenv()

server = Server("Pexels")

pexels_request_map = {
    PexelsTools.PHOTOS_SEARCH: PhotosSearchRequest,
    PexelsTools.PHOTOS_CURATED: PhotosCuratedRequest,
    PexelsTools.PHOTO_GET: PhotoGetRequest,
    PexelsTools.VIDEOS_SEARCH: VideosSearchRequest,
    PexelsTools.VIDEOS_POPULAR: VideosPopularRequest,
    PexelsTools.VIDEO_GET: VideoGetRequest,
    PexelsTools.COLLECTIONS_FEATURED: CollectionsFeaturedRequest,
    PexelsTools.COLLECTIONS_MEDIA: CollectionsMediaRequest,
}


@server.list_tools()
async def list_tools() -> List[Tool]:
    tools = []

    for k, v in pexels_request_map.items():
        description = ""
        if k == PexelsTools.PHOTOS_SEARCH:
            description = "Search photos on Pexels"
        elif k == PexelsTools.PHOTOS_CURATED:
            description = "List curated photos"
        elif k == PexelsTools.PHOTO_GET:
            description = "Get a photo by id"
        elif k == PexelsTools.VIDEOS_SEARCH:
            description = "Search videos on Pexels"
        elif k == PexelsTools.VIDEOS_POPULAR:
            description = "List popular videos"
        elif k == PexelsTools.VIDEO_GET:
            description = "Get a video by id"
        elif k == PexelsTools.COLLECTIONS_FEATURED:
            description = "List featured collections"
        elif k == PexelsTools.COLLECTIONS_MEDIA:
            description = "List collection media"

        tools.append(
            Tool(
                name=k.value,
                description=description or "Pexels operation",
                inputSchema=v.model_json_schema(),
            )
        )

    return tools


@server.call_tool()
async def call_tool(
    name: str, arguments: dict[str, Any]
) -> Sequence[TextContent | ImageContent | EmbeddedResource]:
    if not PEXELS_API_KEY:
        return [TextContent(text=f"PEXELS_API_KEY is empty!", type="text")]

    try:
        if not PexelsTools.has_value(name):
            raise ValueError(f"Tool {name} not found")

        tool = PexelsTools(name)
        request_model = pexels_request_map[tool]
        request = request_model(**arguments)

        # Route to the correct Pexels endpoint
        if tool == PexelsTools.PHOTOS_SEARCH:
            url = build_photos_url("search")
            result = await pexels_get(url, request)
        elif tool == PexelsTools.PHOTOS_CURATED:
            url = build_photos_url("curated")
            result = await pexels_get(url, request)
        elif tool == PexelsTools.PHOTO_GET:
            url = build_photos_url(f"photos/{request.id}")
            result = await pexels_get(url, None)
        elif tool == PexelsTools.VIDEOS_SEARCH:
            url = build_videos_url("search")
            result = await pexels_get(url, request)
        elif tool == PexelsTools.VIDEOS_POPULAR:
            url = build_videos_url("popular")
            result = await pexels_get(url, request)
        elif tool == PexelsTools.VIDEO_GET:
            url = build_videos_url(f"videos/{request.id}")
            result = await pexels_get(url, None)
        elif tool == PexelsTools.COLLECTIONS_FEATURED:
            url = "https://api.pexels.com/v1/collections/featured"
            result = await pexels_get(url, request)
        elif tool == PexelsTools.COLLECTIONS_MEDIA:
            url = f"https://api.pexels.com/v1/collections/{request.id}"
            result = await pexels_get(url, request)
        else:
            raise ValueError("Unsupported tool")

        return [TextContent(text=json.dumps(result, indent=2), type="text")]
    except Exception as e:
        return [TextContent(text=f"Error: {str(e)}", type="text")]


async def main():
    options = server.create_initialization_options()
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, options)
