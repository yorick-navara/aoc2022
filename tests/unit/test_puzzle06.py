from puzzles.puzzle06 import part1, part2


def test_part1_example():
  assert part1(use_example=True) == [7,5,6,10,11]


def test_part1():
  assert part1() == 1655


def test_part2_example():
  assert part2(use_example=True) == 0


def test_part2():
  assert part2() == 2665