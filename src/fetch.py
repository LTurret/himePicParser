from re import search
from re import findall

from requests import get
from bs4 import BeautifulSoup as bs

# creating psudo class -> tuple(folder, filename, url)
def fetch(url) -> list[tuple]:
    if not findall("mltd.matsurihi.me", url):
        raise ValueError('Url must start with "https://mltd.matsurihi.me"')

    request = get(url)
    page = bs(request.content, "html.parser")
    queue: list[tuple] = []

    for element in page.find_all("div", {"class": "card-img-b"}):
        element: str = str(element)

        begin: int = search("cards/", url).end()
        folder = f"{url[begin:]}"

        begin = search("card/", element).end()
        end: int = search(".png", element).end()
        filename: str = element[begin:end-4]

        begin = search("https", element).start()
        end = search(".png", element).end()
        queue.append((folder, filename, element[begin:end]))

    return queue