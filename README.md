# Pexels MCP Server

A Model Context Protocol server that provides access to the **Pexels API** for searching and retrieving photos, videos, and collections.

## Available Tools

- `photos_search` – Search photos
- `photos_curated` – List curated photos
- `photo_get` – Get a photo by id
- `videos_search` – Search videos
- `videos_popular` – List popular videos
- `video_get` – Get a video by id
- `collections_featured` – List featured collections
- `collections_media` – List media in a collection


## Usage


### Using `uv` (recommended)

1. Install [`uv`](https://docs.astral.sh/uv/).

2. In your MCP client code configuration or **Claude** settings (file `claude_desktop_config.json`) add `pexels` mcp server:
    ```json
    {
        "mcpServers": {
            "pexels": {
                "command": "uvx",
                "args": ["pexels-mcp-server"],
                "env": {
                    "PEXELS_API_KEY": "<Your Pexels API key>"
                }
            }
        }
    }
    ```
    `uv` will download the MCP server automatically using `uvx` from [pypi.org](https://pypi.org/project/pexels-mcp-server/) and apply to your MCP client.

### Using `pip` for a project
1. Add `pexels-mcp-server` to your MCP client code `requirements.txt` file.
    ```txt
    pexels-mcp-server
    ```

2. Install the dependencies.
    ```shell
    pip install -r requirements.txt
    ```

3. Add the configuration for your client:
    ```json
    {
        "mcpServers": {
            "pexels": {
                "command": "python3",
                "args": ["-m", "pexels_mcp_server"],
                "env": {
                    "PEXELS_API_KEY": "<Your Pexels API key>"
                }
            }
        }
    }
    ```


### Using `pip` globally

1. Ensure `pip` or `pip3` is available on your system.
    ```bash
    pip install pexels-mcp-server
    # or
    pip3 install pexels-mcp-server
    ```

2. MCP client code configuration or **Claude** settings, add `pexels` mcp server:
    ```json
    {
        "mcpServers": {
            "pexels": {
                "command": "python3",
                "args": ["pexels-mcp-server"],
                "env": {
                    "PEXELS_API_KEY": "<Your Pexels API key>"
                }
            }
        }
    }
    ```


## Debugging

You can use the MCP inspector to debug the server. For `uvx` installations:

```bash
npx @modelcontextprotocol/inspector uvx pexels-mcp-server
```

Or if you've installed the package in a specific directory or are developing on it:

```bash
git clone https://github.com/garylab/pexels-mcp-server.git
cd pexels-mcp-server
npx @modelcontextprotocol/inspector uv run pexels-mcp-server -e PEXELS_API_KEY=<the key>
```


## License

pexels-mcp-server is licensed under the MIT License. This means you are free to use, modify, and distribute the software, subject to the terms and conditions of the MIT License. For more details, please see the LICENSE file in the project repository.
