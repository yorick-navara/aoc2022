from typing import List, Union, Sequence, Literal

import pandas as pd


def read_input_df(filepath: str) -> pd.DataFrame:
  df = pd.read_csv(filepath)
  return df


def read_input_list(
  filepath: str,
  header:Union[int, Sequence[int], str, Literal["infer"]]='infer'
) -> List:
  df = pd.read_csv(filepath, header)
  return df.iloc[:, 0].values.tolist()


def get_puzzle_filename(
  puzzle_number: int,
  use_example = False,
  variant = 1
) -> str:
  if variant != 1:
    filename_variant = f'_{str(variant)}'
  else:
    filename_variant = ''
  if use_example:
    return f"data/{str(puzzle_number).zfill(2)}_input{filename_variant}_example.csv"
  else:
    return f"data/{str(puzzle_number).zfill(2)}_input{filename_variant}.csv"


def read_input_list_from_nr(
  puzzle_number: int,
  use_example = False,
  variant = 1
) -> List[any]:
  filename = get_puzzle_filename(puzzle_number, use_example=use_example, variant = variant)
  return read_input_list(filename)


def read_input_df_from_nr(
  puzzle_number: int,
  use_example = False
) -> pd.DataFrame:
  filename = get_puzzle_filename(puzzle_number, use_example=use_example)
  return read_input_df(filename)
