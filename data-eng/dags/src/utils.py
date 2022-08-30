import logging
import os.path
from typing import List

import pandas as pd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def save_files(
    df_list: List[pd.DataFrame],
    base_path: str
) -> None:
    """accepts dataframe list as input
    saves each dataframe in the tmp folder as csv
    the file name corresponds to the dataframe "name" attribute

    Args:
        df_list (list): list of dataframes
        base_path (str): base path for saving file
    """
    for df in df_list:
        logging.info(f"Saving file {df.name} in {base_path}")
        df.to_csv(
            base_path + df.name + ".csv" , sep=",", index=False
        )
        logging.info(f"file {df.name} saved!")


def load_files(
    names_list: List[str],
    base_path: str
) -> List[pd.DataFrame]:
    """accepts a list of names (str) as input
    load each csv file from the tmp folder with the input names
    returns a list of loaded dataframes

    Args:
        names_list (list): list of names
        base_path (str): base path for loading files

    Returns:
        list: list of loaded dataframes
    """
    df_list = []
    for name in names_list:
        if os.path.isfile(base_path + name + ".csv"):
            df_list.append(
                pd.read_csv(base_path + name + ".csv")
            )

    return df_list
