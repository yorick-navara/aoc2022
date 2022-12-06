from typing import List
from generic.read_inputs import read_input_list_from_nr

def get_start_marker(signal: str, MARKER_SIZE: int = 4) -> int:
  for index,c in enumerate(signal):
    marker = [signal[i] for i in range(index, index + MARKER_SIZE)]
    if len(set(marker)) == MARKER_SIZE:
      return index + MARKER_SIZE

def part1(use_example:bool=False) -> List[int]:
  input = read_input_list_from_nr(6, use_example=use_example)
  markers = []
  for x in input:
    marker = get_start_marker(x)
    markers.append(marker)
  return markers


def part2(use_example:bool=False) -> str:
  input = read_input_list_from_nr(6, use_example=use_example)
  markers = []
  for x in input:
    marker = get_start_marker(x, MARKER_SIZE=14)
    markers.append(marker)
  return markers