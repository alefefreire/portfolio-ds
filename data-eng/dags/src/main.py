import os

import pandas as pd
from src import settings
from src.book import Catalog
from src.utils import save_files


def run() -> None:
    """This function runs the main logic to do the scraping

    Args:
        book_url (str): the url of web page which will be scraped.
    """
    catalog = Catalog(settings.BOOK_URL)
    book_info = []
    for url in catalog._catalog_urls:
        number_of_web_pages = catalog.number_of_web_pages(
            catalog_url=os.path.join(catalog.url, url, "index.html")
        )
        if number_of_web_pages:
            n_pages = int(number_of_web_pages)
            for n in range(1, n_pages + 1):
                soup = catalog.get_soup(
                    url=os.path.join(catalog.url, url, f"page-{n}.html")
                )
                books = soup.find_all(attrs={"class": "product_pod"})
                for book in books:
                    aux = []
                    aux.append(
                        catalog.book_category(catalog_url=url)
                    )
                    aux.append(
                        catalog.book_title_name(book)
                    )
                    aux.append(
                        catalog.book_price(book)
                    )
                    aux.append(
                        catalog.is_book_available(book)
                    )
                    aux.append(
                        catalog.book_ratings(book)
                    )

                    book_info.append(aux)
        else:
            soup = catalog.get_soup(
                    url=os.path.join(catalog.url, url, "index.html")
                )
            books = soup.find_all(attrs={"class": "product_pod"})
            for book in books:
                aux = []
                aux.append(
                    catalog.book_category(catalog_url=url)
                )
                aux.append(
                    catalog.book_title_name(book)
                )
                aux.append(
                    catalog.book_price(book)
                )
                aux.append(
                    catalog.is_book_available(book)
                )
                aux.append(
                    catalog.book_ratings(book)
                )

                book_info.append(aux)

    df = pd.DataFrame(
        book_info,
        columns=["category", "title", "price", "stock", "rating"]
    )

    df.name = "book"

    save_files(
        df_list=[df],
        base_path="/opt/airflow/data/"
    )
