from typing import List

import pandas as pd


def get_prio(item: str) -> int:
  scores = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  return scores.index(item)


def get_duplicate_priorities(row) -> int:
  items = row['c1']
  num = len(items)
  first = items[:int(num/2)]
  second = items[int(num/2):]
  dupes = list(set([c for c in first if c in second]))
  prio = get_prio(dupes[0])
  return prio


def get_badge_prio(backpacks: List[str]) -> int:
  common = list(set([x for x in backpacks[0] if x in backpacks[1] and x in backpacks[2]]))
  prio = get_prio(common[0])
  return prio


def get_sum_priorities_unique_items(df: pd.DataFrame) -> int:
  df['prio'] = df.apply(get_duplicate_priorities, axis = 1)
  return sum(df['prio'])


def get_sum_priorities_group(df: pd.DataFrame) -> int:
  badge_prios = []
  for i in range(0, df.shape[0], 3):
    prio = get_badge_prio(list(df['c1'][i:i+3]))
    badge_prios.append(prio)

  return sum(badge_prios)