import os

BOOK_URL = os.environ.get("BOOK_URL", "http://books.toscrape.com/")
DB_ENGINE = os.environ.get(
    "DB_ENGINE",
    "postgresql+psycopg2://airflow:airflow@postgres/airflow"
)
DB_SCHEMA = os.environ.get("DB_SCHEMA", "public")
DB_TABLE = os.environ.get("DB_TABLE", "book")
