from puzzles import *
from puzzles import \
  puzzle01, \
  puzzle02, \
  puzzle03, \
  puzzle04, \
  puzzle05, \
  puzzle06, \
  puzzle08, \
  puzzle09, \
  puzzle10, \
  puzzle11


PUZZLE_SOLVERS = {
  1: {
    1: puzzle01.part1,
    2: puzzle01.part2
  },
  2: {
    1: puzzle02.part1,
    2: puzzle02.part2
  },
  3: {
    1: puzzle03.part1,
    2: puzzle03.part2
  },
  4: {
    1: puzzle04.part1,
    2: puzzle04.part2
  },
  5: {
    1: puzzle05.part1,
    2: puzzle05.part2
  },
  6: {
    1: puzzle06.part1,
    2: puzzle06.part2
  },
  8: {
    1: puzzle08.part1,
    2: puzzle08.part2
  },
  9: {
    1: puzzle09.part1,
    2: puzzle09.part2
  },
  10: {
    1: puzzle10.part1,
    2: puzzle10.part2
  },
  11: {
    1: puzzle11.part1,
    2: puzzle11.part2
  }
}


def solve(puzzle_number: int, part: int=None):
  solvers = PUZZLE_SOLVERS[puzzle_number]
  if part != 2:
    solution = solvers[1]()
    print(f"Solution of puzzle {puzzle_number}, part 1 is: {solution}")
  if part != 1:
    solution = solvers[2]()
    print(f"Solution of puzzle {puzzle_number}, part 2 is: {solution}")