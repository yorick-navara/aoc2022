from puzzles.puzzle05 import part1, part2


def test_part1_example():
  assert part1(use_example=True) == 'CMZ'


def test_part1():
  assert part1() == 'WCZTHTMPS'


def test_part2_example():
  assert part2(use_example=True) == 'MCD'


def test_part2():
  assert part2() == ''