from puzzles.puzzle08 import part1, part2


def test_part1_example():
  assert part1(use_example=True) == 21


def test_part1():
  assert part1() == 1827


def test_part2_example():
  assert part2(use_example=True) == 8


def test_part2():
  assert part2() == -1