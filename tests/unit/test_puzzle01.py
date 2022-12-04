from puzzles.puzzle01 import part1, part2


def test_part1_example():
  assert part1(use_example=True) == 24000


def test_part1():
  assert part1() == 72478


def test_part2_example():
  assert part2(use_example=True) == 45000


def test_part2():
  assert part2() == 210367
