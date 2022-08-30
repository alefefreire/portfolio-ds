import logging

import src.settings as settings
from sqlalchemy import create_engine  # type: ignore
from src.utils import load_files

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

db_engine = settings.DB_ENGINE
db_schema = settings.DB_SCHEMA
db_table = settings.DB_TABLE


def save_data() -> None:
    logger.info("Saving data in DB")
    df = load_files(["book"], base_path="/opt/airflow/data/")[0]
    engine = create_engine(db_engine)
    df.to_sql(db_table, engine, schema=db_schema, if_exists="replace", index=False)
    logger.info("Data info saved in DB")
