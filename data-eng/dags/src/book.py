import re
from typing import Any, List

import bs4  # type: ignore
import requests
from bs4 import BeautifulSoup


class Book:

    def __init__(self, url: str):
        """This class collects all information about the books that are being scraped

        Args:
            url (str): self explained
        """
        self.url = url

    def book_title_name(self, book: bs4.element.ResultSet) -> Any:
        return book.h3.a.get("title")

    def book_price(self, book: bs4.element.ResultSet) -> Any:
        return book.find("p", class_="price_color").text[2:]

    def book_ratings(self, book: bs4.element.ResultSet) -> Any:
        return book.find("p", class_="star-rating")["class"][-1]

    def book_category(self, catalog_url: str) -> Any:
        category = re.findall(r"\w+_", catalog_url)[0].replace("_", "")
        return category

    def is_book_available(self, book: bs4.element.ResultSet) -> Any:
        return book.find("p", class_="instock availability").text.strip()


class Catalog(Book):

    def __init__(self, url: str):
        """This class get informations about the web page where the books are in.

        Args:
            url (str): self explained
        """
        self._url = url
        super().__init__(url)

    @property  # type: ignore
    def url(self) -> Any:  # type: ignore
        return self._url

    @url.setter
    def url(self, url: Any) -> Any:
        if isinstance(url, str):
            self._url = url
        else:
            raise Exception("url attribute is not a string")

    @staticmethod
    def get_soup(url: str) -> bs4.BeautifulSoup:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        return soup

    @property
    def _catalog_urls(self) -> List[str]:
        urls = []
        soup = self.get_soup(self.url)
        for a in soup.find_all("a", href=True):
            urls.append(a["href"])
        catalog_urls = [
            url.replace(
                "/index.html", ""
            ) for url in urls if "catalogue/category/books/" in url
        ]
        return catalog_urls

    def number_of_web_pages(self, catalog_url: str) -> Any:
        soup = self.get_soup(catalog_url)
        html_cont = soup.find_all(attrs={"class": "current"})
        n_of_web_pages = html_cont[0].next_element.split()[-1] if html_cont else None
        return n_of_web_pages
