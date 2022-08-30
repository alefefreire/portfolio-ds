import os

import pandas as pd
import pytest
from src import utils


def test_save_files(tmp_path):
    output_path = os.path.join(tmp_path, 'test')
    d = {'col1': [1, 2], 'col2': [3, 4]}
    mock_df = pd.DataFrame(data=d)
    mock_df.name = 'test'
    utils.save_files(
        df_list=[mock_df],
        base_path=output_path
    )
    assert True

def test_load_files(tmp_path):
    output_path = os.path.join(tmp_path, 'test')
    d = {'col1': [1, 2], 'col2': [3, 4]}
    mock_df = pd.DataFrame(data=d)
    mock_df.name = 'test'
    utils.save_files(
        df_list=[mock_df],
        base_path=output_path
    )

    loaded_df = utils.load_files(
        names_list=['test'],
        base_path=output_path
    )[0]

    assert list(loaded_df.columns) == list(mock_df.columns)
    assert loaded_df.values.tolist() == mock_df.values.tolist()
