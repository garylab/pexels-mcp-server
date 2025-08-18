import asyncio
import argparse
from . import server


def main():
    asyncio.run(server.main())


__all__ = ["main"]
