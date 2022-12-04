from typing import List


def assignment_contains_other(a1: str, a2: str) -> True:
  a1_min, a1_max = [int(x) for x in a1.split('-')]
  a2_min, a2_max = [int(x) for x in a2.split('-')]

  if (a1_min <= a2_min and a1_max >= a2_max) \
    or (a1_min >= a2_min and a1_max <= a2_max):
    return True
  else:
    return False


def assignment_overlaps_other(a1: str, a2: str) -> True:
  a1_min, a1_max = [int(x) for x in a1.split('-')]
  a2_min, a2_max = [int(x) for x in a2.split('-')]

  if (a1_min <= a2_min and a1_max >= a2_max) \
    or (a1_min >= a2_min and a1_max <= a2_max) \
    or (a1_min >= a2_min and a1_min <= a2_max) \
    or (a1_max >= a2_min and a1_max <= a2_max):
    return True
  else:
    return False


def count_assignments_contain_each_other(
  a1_list: List[str],
  a2_list: List[str]
)-> int:
  are_contained = [assignment_contains_other(a1_list[i], a2_list[i]) for i, _ in enumerate(a1_list) ]
  return sum(are_contained)


def count_assignments_overlap(
  a1_list: List[str],
  a2_list: List[str]
)-> int:
  are_contained = [assignment_overlaps_other(a1_list[i], a2_list[i]) for i, _ in enumerate(a1_list) ]
  return sum(are_contained)