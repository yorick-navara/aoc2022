from puzzles import *
from puzzles import puzzle01, puzzle02, puzzle04


PUZZLE_SOLVERS = {
  1: {
    1: puzzle01.part1,
    2: puzzle01.part2
  },
  2: {
    1: puzzle02.part1,
    2: puzzle02.part2
  },
  4: {
    1: puzzle04.part1,
    2: puzzle04.part2
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