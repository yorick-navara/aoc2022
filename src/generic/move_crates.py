
from typing import List

from typing import List


def parse_instruction(instruction:str) -> List[int]:
  i = instruction.split(' ')
  return [int(i[1]), int(i[3])-1, int(i[5])-1]


def get_top_crates_after_move_single(crates, instructions):
  end_situation = move_crates_single(crates, instructions)
  top_crates = []
  for stack in end_situation:
    top_crates.append(stack[-1])
  return ''.join(top_crates)


def remove_top_crate(crates:str, num:int=1) -> str:
  top_crate = crates[-num:]
  remaining_stack = crates[:-num]
  return remaining_stack, top_crate


def put_crate_on_stack(stack:str, crate:str) -> str:
  return f"{stack}{crate}"


def move_crates_single(crates, instructions:List[str]) -> List:
  for instr_str in instructions:
    instr = parse_instruction(instr_str)
    for i in range(instr[0]): # num repeat
      crates[instr[1]], crate = remove_top_crate(crates[instr[1]])
      crates[instr[2]] = put_crate_on_stack(crates[instr[2]],crate)
  return crates


def move_crates_multiple(crates, instructions:List[str]) -> List:
  for instr_str in instructions:
    instr = parse_instruction(instr_str)
    crates[instr[1]], crate = remove_top_crate(crates[instr[1]], num=instr[0])
    crates[instr[2]] = put_crate_on_stack(crates[instr[2]],crate)
  return crates


def get_top_crates_after_move_multiple(crates, instructions):
  end_situation = move_crates_multiple(crates, instructions)
  top_crates = []
  for stack in end_situation:
    top_crates.append(stack[-1])
  return ''.join(top_crates)
