import os
import pickle

import pytest

from src import settings
from src.book import Catalog


def get_pickle_data(pickle_path):
    with open(pickle_path, 'rb') as pickle_file:
        obj = pickle.load(pickle_file)
    return obj

@pytest.fixture
def catalog():
    return Catalog(url=settings.BOOK_URL)

@pytest.fixture
def catalog_urls():
    pickle_file = "./data/catalog_urls.pkl"
    urls_data = get_pickle_data(pickle_file)
    return urls_data

def test_catalog_urls(catalog_urls, catalog):
    urls = catalog._catalog_urls
    assert urls == catalog_urls

def test_number_of_pages(catalog_urls, catalog):
    url_test = catalog_urls[1]
    n_pages = catalog.number_of_web_pages(
        catalog_url=os.path.join(catalog.url, url_test, "index.html")
    )
    assert n_pages == "2"

def test_book_title_name(catalog_urls, catalog):
    url = catalog_urls[0]
    soup = catalog.get_soup(url=os.path.join(catalog.url, url, "index.html"))
    books = soup.find_all(attrs={"class": "product_pod"})
    book = books[0]
    assert catalog.book_title_name(book) == "It's Only the Himalayas"

def test_book_price(catalog_urls, catalog):
    url = catalog_urls[0]
    soup = catalog.get_soup(url=os.path.join(catalog.url, url, "index.html"))
    books = soup.find_all(attrs={"class": "product_pod"})
    book = books[0]
    assert catalog.book_price(book) == "45.17"

def test_book_is_book_available(catalog_urls, catalog):
    url = catalog_urls[0]
    soup = catalog.get_soup(url=os.path.join(catalog.url, url, "index.html"))
    books = soup.find_all(attrs={"class": "product_pod"})
    book = books[0]
    assert catalog.is_book_available(book) == "In stock"

def test_book_ratings(catalog_urls, catalog):
    url = catalog_urls[0]
    soup = catalog.get_soup(url=os.path.join(catalog.url, url, "index.html"))
    books = soup.find_all(attrs={"class": "product_pod"})
    book = books[0]
    assert catalog.book_ratings(book) == "Two"

def test_book_category(catalog_urls, catalog):
    url = catalog_urls[0]
    assert catalog.book_category(catalog_url=url) == "travel"