from argparse import ArgumentParser

from asyncio import create_task, gather, new_event_loop, set_event_loop, Task

from src.fetch import fetch

parser = ArgumentParser(
    prog = "himePicParser",
    description = "Fetch all url in the matsurihi.me html elements"
)

parser.add_argument("-U", "--url", nargs="+", type=str, default=["https://mltd.matsurihi.me/cards/1945"])
parser.add_argument("-D", "--dir", nargs=1, type=str, default="./")
args = parser.parse_args()

async def main(urls: list[str], directory: str) -> None:
    for url in urls:
        queue: list[str] = fetch(url)

        if not len(queue):
            return None

        from aiohttp import ClientSession
        from src.download import download
        tasks: list[Task] = []

        async with ClientSession() as session:
            for asset in queue:
                path = f"{directory}/{asset[0]}"
                tasks.append(create_task(download(session, path, asset[1], asset[2])))
            await gather(*tasks)

    return None

if __name__ == "__main__":
    loop = new_event_loop()
    set_event_loop(loop)
    loop.run_until_complete(main(args.url, args.dir))