import pandas as pd


CHOOSE_ROCK = 1
CHOOSE_PAPER = 2
CHOOSE_SCISSORS = 3

WIN = 'Z'
LOSE = 'X'
DRAW = 'Y'

OPP_ROCK = 'A'
OPP_PAPER = 'B'
OPP_SCISSORS = 'C'


def get_score(row) -> int:
  score = 0
  if row['you'] == 'X':
    score += 1
    if row['opp'] == 'A':
      score += 3
    elif row['opp'] == 'C':
      score += 6
  elif row['you'] == 'Y':
    score += 2
    if row['opp'] == 'B':
      score += 3
    elif row['opp'] == 'A':
      score += 6
  elif row['you'] == 'Z':
    score += 3
    if row['opp'] == 'C':
      score += 3
    elif row['opp'] == 'B':
      score += 6
  return score


def get_total_score_pt1(strat: pd.DataFrame) -> int:
  strat['score'] = strat.apply(get_score, axis = 1)
  return sum(strat['score'])


def get_score2(row) -> int:
  score = 0
  outcome = row['you']

  if row['opp'] == OPP_ROCK:
    if outcome == LOSE:
      score += CHOOSE_SCISSORS
    elif outcome == DRAW:
      score += CHOOSE_ROCK
    elif outcome == WIN:
      score += CHOOSE_PAPER
  elif row['opp'] == OPP_PAPER:
    if outcome == LOSE:
      score += CHOOSE_ROCK
    elif outcome == DRAW:
      score += CHOOSE_PAPER
    elif outcome == WIN:
      score += CHOOSE_SCISSORS
  elif row['opp'] == OPP_SCISSORS:
    if outcome == WIN:
      score += CHOOSE_ROCK
    elif outcome == DRAW:
      score += CHOOSE_SCISSORS
    elif outcome == LOSE:
      score += CHOOSE_PAPER 

  outcome = row['you']
  if outcome == 'X':
    score += 0
  elif outcome == 'Y':
    score += 3
  elif outcome == 'Z':
    score += 6
  
  return score


def get_total_score_pt2(strat: pd.DataFrame):
  strat['score'] = strat.apply(get_score2, axis = 1)
  return sum(strat['score'])