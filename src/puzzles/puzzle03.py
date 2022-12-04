from generic.read_inputs import read_input_df_from_nr
from generic.backpacks import get_sum_priorities_unique_items, get_sum_priorities_group


def part1(use_example:bool=False) -> int:
  df = read_input_df_from_nr(3, use_example=use_example)
  return get_sum_priorities_unique_items(df)


def part2(use_example:bool=False) -> int:
  df = read_input_df_from_nr(3, use_example=use_example)
  return get_sum_priorities_group(df)