from puzzles.puzzle02 import part1, part2


def test_part1_example():
  assert part1(use_example=True) == 15


def test_part1():
  assert part1() == 13268


def test_part2_example():
  assert part2(use_example=True) == 12


def test_part2():
  assert part2() == 15508
