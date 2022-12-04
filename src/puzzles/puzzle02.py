from generic.read_inputs import read_input_df_from_nr
from generic.rps import get_total_score_pt1, get_total_score_pt2


def part1(use_example:bool=False) -> int:
  df = read_input_df_from_nr(2, use_example=use_example)
  return get_total_score_pt1(df)


def part2(use_example:bool=False) -> int:
  df = read_input_df_from_nr(2, use_example=use_example)
  return get_total_score_pt2(df)