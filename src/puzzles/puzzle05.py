from generic.read_inputs import read_input_list_from_nr
from generic.move_crates import get_top_crates_after_move_single, \
  get_top_crates_after_move_multiple


def get_data_stacks(use_example:bool): #-> int, List:
  if use_example:
    start = 4
    cratestacks = ['ZN', 'MCD', 'P']
  else:
    start = 8
    cratestacks = [
      'GDVZJSB',
      'ZSMGVP',
      'CLBSWTQF',
      'HJGWMRVQ',
      'CLSNFMD',
      'RGCD',
      'HGTRJDSQ',
      'PFV',
      'DRSTJ'
    ]
  return start, cratestacks


def part1(use_example:bool=False) -> str:
  start, cratestacks = get_data_stacks(use_example)

  input = read_input_list_from_nr(5, use_example=use_example)
  instructions = input[start:]

  return get_top_crates_after_move_single(cratestacks, instructions)


def part2(use_example:bool=False) -> str:
  start, cratestacks = get_data_stacks(use_example)

  input = read_input_list_from_nr(5, use_example=use_example)
  instructions = input[start:]

  return get_top_crates_after_move_multiple(cratestacks, instructions)
