from re import search

from argparse import ArgumentParser

import requests

from bs4 import BeautifulSoup as bs

parser = ArgumentParser(
    prog = "himePicParser",
    description = "Easy to fetch all pictures in the matsurihi.me"
)

parser.add_argument("-U", "--url", nargs="+", type=str, default="https://mltd.matsurihi.me/cards/1945")

args = parser.parse_args()

def main(urls):
    for url in urls:
        request = requests.get(url)
        page = bs(request.content, "html.parser")
        
        for element in page.find_all("div", {"class": "card-img-b"}):
            element = str(element)
            begin = search("https", element).start()
            end = search(".png", element).end()
            print(element[begin:end])

main(args.url)