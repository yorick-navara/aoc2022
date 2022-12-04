from puzzles.puzzle03 import part1, part2


def test_part1_example():
  assert part1(use_example=True) == 157


def test_part1():
  assert part1() == 8394


def test_part2_example():
  assert part2(use_example=True) == 70


def test_part2():
  assert part2() == 2413
