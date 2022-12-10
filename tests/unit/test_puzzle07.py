from puzzles.puzzle07 import part1, part2, determine_file_structure
from generic.read_inputs import read_input_list_from_nr


def test_part1_example():
  assert part1(use_example=True) == 95437


def test_determine_file_structure_example():
  input = read_input_list_from_nr(7, use_example=True)
  expected_dir_structure = {
    '/': {
      'a': {
        'e': {
          'i': 584
        },
        'f': 29116,
        'g': 2557,
        'h.lst': 62596
      },
      'b.txt': 14848514,
      'c.dat': 8504156,
      'd': {
        'j': 4060174,
        'd.log': 8033020,
        'd.ext': 5626152,
        'k': 7214296
      }
    }
  }

  dir_structure = determine_file_structure(input)

  assert dir_structure == expected_dir_structure

def test_part1():
  result = part1()
  assert result == 1325919
  assert result == 0


# def test_part2_example():
#   assert part2(use_example=True) == 0


# def test_part2():
#   assert part2() == 0