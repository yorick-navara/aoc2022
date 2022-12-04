from puzzles.puzzle04 import part1, part2


def test_part1_example():
  assert part1(use_example=True) == 2


def test_part1():
  assert part1() == 433


def test_part2_example():
  assert part2(use_example=True) == 4


def test_part2():
  assert part2() == 852