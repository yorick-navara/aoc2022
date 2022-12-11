from puzzles.puzzle11 import part1, part2


def test_part1_example():
  assert part1(use_example=True) == 10605


def test_part1():
  assert part1() == 58322


def test_part2_example():
  # divisor = 1834963
  assert part2(use_example=True) == 2713310158

def test_part2():
  assert part2() < 14808513720