import wget
import sys
from bs4 import BeautifulSoup
import requests
from typing import List


# e.g Example
BASE_URL = ""


def scrape_hyperef(str_html: str, pred_suff: List = None) -> List:
    if pred_suff is None:
        pred_suff = ["pdf", "md", "ppt", "pptx", "csv", "txt", "xslx"]
    soup = BeautifulSoup(markup=str_html, features="html5lib")
    links = [
        link.get("href")
        for link in soup.find_all("a")
        if len(link.get("href").split(".")) > 1
    ]
    links_filtered = [link for link in links if link.split(".")[1] in pred_suff]
    print(f"Total number of hyperlinks: {len(links_filtered)}!")
    return links_filtered


def download(list_url: List) -> None:
    base_url = BASE_URL
    [wget.download(base_url + i) for i in list_url]


def main() -> None:
    """
    A link  <a href="something.pdf"> scraper-downloader!
    Usage:
            python download.py <github.com> <"md txt pdf">
            <optional>
    """

    if len(sys.argv) > 1:
        global BASE_URL
        BASE_URL = sys.argv[1]
    if len(sys.argv) > 2:
        pred_suff = sys.argv[2]
    res = requests.get(BASE_URL)
    list_href = scrape_hyperef(res.text)
    download(list_href)


if __name__ == "__main__":
    main()
