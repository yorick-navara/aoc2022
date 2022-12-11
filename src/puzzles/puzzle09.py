from argparse import ArgumentError
from typing import List, Tuple
from generic.read_inputs import read_csv_list_from_nr

def sign(x:int) -> int:
  if x >= 0:
    return 1
  elif x < 0:
    return -1
  else:
    raise ValueError(f'Sign of {x} could not be determined')



def move_one_step(dir:str, head_pos: Tuple[int, int]) -> Tuple[int, int]:
  if dir == 'U':
    return (head_pos[0], head_pos[1]+1)
  elif dir == 'D':
    return (head_pos[0], head_pos[1]-1)
  elif dir == 'L':
    return (head_pos[0]-1, head_pos[1])
  elif dir == 'R':
    return (head_pos[0]+1, head_pos[1])
  else:
    raise ArgumentError(f"Direction {dir} not valid")


def catch_up_tail(head_pos: Tuple[int, int], tail_pos: Tuple[int, int]) -> Tuple[int, int]:
  diff_x = head_pos[0] - tail_pos[0]
  diff_y = head_pos[1] - tail_pos[1]
  # if close enough: don't move
  if abs(diff_x) <= 1 and abs(diff_y) <= 1:
    return tail_pos
  elif abs(diff_x) >= 2:
    new_tail_x = tail_pos[0] + int(sign(diff_x)*(abs(diff_x)-1))
    if abs(diff_y) >= 2:
      new_tail_y = tail_pos[1] + int(sign(diff_y)*(abs(diff_y)-1))
    else:
      new_tail_y = tail_pos[1] + diff_y
    return (new_tail_x, new_tail_y)
  elif abs(diff_y) >= 2:
    if abs(diff_x) >= 2:
      new_tail_x = tail_pos[0] + int(sign(diff_x)*(abs(diff_x)-1))
    else:
      new_tail_x = tail_pos[0] + diff_x
    new_tail_y = tail_pos[1] + int(sign(diff_y)*(abs(diff_y)-1))
    return (new_tail_x, new_tail_y)
  else:
    raise NotImplementedError(f"Unable to deal with combination of diff_x={diff_x} and diff_y={diff_y}")



def get_pos_tail_visited(input: List[str]) -> int:
  head_pos = (0,0)
  tail_pos = (0,0)
  tail_pos_visited =[(0,0)]

  for step in input:
    step_spl = step.split(' ')
    dir = step_spl[0]
    dist = int(step_spl[1])

    for x in range(dist):
      head_pos = move_one_step(dir, head_pos)
      new_tail_pos = catch_up_tail(head_pos, tail_pos)
      tail_pos_visited.append(new_tail_pos)
      tail_pos = new_tail_pos

  return len(set(tail_pos_visited))


def get_pos_tail_visited_long_rope(input: List[str], rope_length) -> int:
  tail_pos_visited =[(0,0)]
  knot_pos = [(0,0) for x in range(rope_length)]
  tail_pos_visited =[(0,0)]

  for step in input:
    step_spl = step.split(' ')
    dir = step_spl[0]
    dist = int(step_spl[1])
    for x in range(dist):
      for knot_index, head_pos in enumerate(knot_pos):
        if knot_index == 0:
          knot_pos[0] = move_one_step(dir, knot_pos[0])
        elif knot_index <= len(knot_pos) - 1:
          knot_pos[knot_index] = catch_up_tail(knot_pos[knot_index-1], knot_pos[knot_index])
          if knot_index == len(knot_pos) - 1:
            tail_pos_visited.append(knot_pos[knot_index])

  return len(set(tail_pos_visited))
    


def part1(use_example:bool=False) -> int:
  input = read_csv_list_from_nr(9, use_example=use_example)
  steps = get_pos_tail_visited_long_rope(input,rope_length=2)
  return steps


def part1_generalized(use_example:bool=False) -> int:
  input = read_csv_list_from_nr(9, use_example=use_example)
  steps = get_pos_tail_visited_long_rope(input,rope_length=2)
  return steps


def part2(use_example:bool=False) -> int:
  if use_example:
    variant = 2
  else:
    variant = 1
  input = read_csv_list_from_nr(9, use_example=use_example, variant=variant)
  steps = get_pos_tail_visited_long_rope(input,rope_length=10)
  return steps