from typing import List
from generic.read_inputs import read_csv_list_from_nr


def get_signal_strengths(
  input: List[str],
  signal_indices: List[str],
  start_value: int
) -> List[int]:
  values = get_signals(input, start_value=1)
  return [values[index-1]*index for index in signal_indices]


def get_signals(
  input: List[str],
  start_value: int
) -> List[int]:
  current_value = start_value
  # start with value, one-off, because setting value lags behind by a cycle 
  values = [start_value]
  for signal in input:
    if signal == 'noop':
      values.append(current_value)
    elif signal.startswith('addx '):
      addition = int(signal.split(' ')[1])
      # first cycle:
      values.append(current_value)
      # second cycle:
      current_value += addition
      values.append(current_value)
    else:
      ValueError(f"Command {signal} in input not recognized")
  return values


def draw_crt(input: List[str], width=40, height=6):
  signals = get_signals(input, start_value=1)
  crt = []
  
  for cycle, signal in enumerate(signals):
    drawing_position = cycle % width
    if drawing_position >= signal-1 and drawing_position <= signal+1:
      crt.append('#')
    else:
      crt.append('.')
  return [''.join(crt[start*width:start*width+width]) for start in range(6)]


def part1(use_example:bool=False) -> int:
  input = read_csv_list_from_nr(10, use_example=use_example)
  signal_indices = [20, 60, 100, 140, 180, 220]
  signal_strengths = get_signal_strengths(input, signal_indices, start_value=1)
  return sum(signal_strengths)


def part2(use_example:bool=False) -> int:
  input = read_csv_list_from_nr(10, use_example=use_example)
  result = draw_crt(input)
  return result