from os import path
from os import mkdir

from aiohttp import ClientSession

async def download(session: ClientSession, directory: str, filename: str, url: str) -> None:
    async with session.get(url) as file:
        file = await file.read()

        if not path.isdir(directory):
            mkdir(directory)

        with open(f"{directory}/{filename}.png", mode="w+b") as image:
            image.write(file)

    return None