from puzzles.puzzle10 import part1, part2, get_signal_strengths
from generic.read_inputs import read_input_list_from_nr


def test_get_signal_strengths_example():
  input = read_input_list_from_nr(10, use_example=True)
  signal_indices = [20, 60, 100, 140, 180, 220]
  signal_strengths = get_signal_strengths(input, signal_indices, start_value=1)
  assert signal_strengths == [420, 1140, 1800, 2940, 2880, 3960]


def test_part1_example():
  assert part1(use_example=True) == 13140


def test_part1():
  assert part1() == 12740


def test_part2_example():
  assert part2(use_example=True) == [
    '##..##..##..##..##..##..##..##..##..##..',
    '###...###...###...###...###...###...###.', 
    '####....####....####....####....####....', 
    '#####.....#####.....#####.....#####.....', 
    '######......######......######......####', 
    '#######.......#######.......#######.....']


def test_part2():
  assert part2() == [
    '###..###..###...##..###...##...##..####.',
    '#..#.#..#.#..#.#..#.#..#.#..#.#..#.#....',
    '#..#.###..#..#.#..#.#..#.#..#.#....###..',
    '###..#..#.###..####.###..####.#.##.#....',
    '#.#..#..#.#....#..#.#.#..#..#.#..#.#....',
    '#..#.###..#....#..#.#..#.#..#..###.#....']