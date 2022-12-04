from generic.read_inputs import read_input_df_from_nr
from generic.assignments import count_assignments_contain_each_other, count_assignments_overlap


def part1(use_example:bool=False) -> int:
  df = read_input_df_from_nr(4, use_example=use_example)
  a1_list = df['c1'].values.tolist()
  a2_list = df['c2'].values.tolist()

  solution = count_assignments_contain_each_other(a1_list, a2_list)
  return solution


def part2(use_example:bool=False) -> int:
  df = read_input_df_from_nr(4, use_example=use_example)
  a1_list = df['c1'].values.tolist()
  a2_list = df['c2'].values.tolist()

  solution2 = count_assignments_overlap(a1_list, a2_list)
  return solution2
  # expected: 852