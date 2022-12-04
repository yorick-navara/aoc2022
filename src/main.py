import sys
from puzzle_solver import solve


def main():
  args = sys.argv[1:]

  if len(args) == 2 and args[0] == '--puzzle' or args[0] == '-p':
    puzzle_nr = int(args[1])
    print(f"Generating solution for puzzle {str(puzzle_nr)}")
    solve(puzzle_nr)
  else:
    print("Call program with flag --puzzle or -p and the number of the puzzle to solve")

if __name__ == '__main__':
  main()