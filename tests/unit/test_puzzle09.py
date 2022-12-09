from puzzles.puzzle09 import part1, part1_generalized, part2


def test_part1_example():
  assert part1(use_example=True) == 13


def test_part1_example_generalized():
  assert part1_generalized(use_example=True) == 13


def test_part1():
  assert part1() == 5907


def test_part1_generalized():
  assert part1_generalized() == 5907


def test_part2_example():
  assert part2(use_example=True) == 36


def test_part2():
  assert part2() == 2303