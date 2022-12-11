from typing import List
from generic.read_inputs import read_csv_list_from_nr


def part1(use_example:bool=False) -> int:
  input = read_csv_list_from_nr(8, use_example=use_example)
  
  num_trees_visible = 0
  
  forest_grid = [
    [int(tree) for tree in str(row)] for row in input]
  
  for col_index, row in enumerate(forest_grid):
    for row_index, selected_tree in enumerate(row):
      if col_index == 0 or col_index == len(input) - 1: # is it a tree on the right or left edge?
        num_trees_visible+=1
        continue
      if row_index == 0 or row_index == len(row) - 1: # is it a tree on the top or bottom edge?
        num_trees_visible+=1
        continue
      if all(tree < selected_tree for tree in row[row_index+1:]) or \
        all(tree < selected_tree for tree in row[0:row_index]):
        num_trees_visible += 1
        continue
      trees_in_col = [forest_grid[c][row_index] for c in range(len(forest_grid))]
      if all(tree < selected_tree for tree in trees_in_col[col_index+1:]) or \
        all(tree < selected_tree for tree in trees_in_col[0:col_index]):
        num_trees_visible += 1
        continue 
  return num_trees_visible


def get_scenic_score(view:List[int], selected_tree: int) -> int:
    if len(view) == 0:
      return 0
    trees_block_view = [tree >= selected_tree for tree in view]
    if not any(trees_block_view):
      return len(view)
    
    return trees_block_view.index(True) + 1


def part2(use_example:bool=False) -> int:
  input = read_csv_list_from_nr(8, use_example=use_example)
  
  max_scenic_score = 0
  
  forest_grid = [
    [int(tree) for tree in str(row)] for row in input]
  
  for col_index, row in enumerate(forest_grid):
    for row_index, selected_tree in enumerate(row):
      if col_index == 0 or col_index == len(input) - 1: # is it a tree on the right or left edge?
        continue
      if row_index == 0 or row_index == len(row) - 1: # is it a tree on the top or bottom edge?
        continue
      
      view_right = row[row_index+1:]
      scenic_score_right = get_scenic_score(view_right, selected_tree)
      
      view_left = list(reversed(row[0:row_index]))
      scenic_score_left = get_scenic_score(view_left, selected_tree)
      
      trees_in_col = [forest_grid[c][row_index] for c in range(len(forest_grid))]
      
      view_up = list(reversed(trees_in_col[0:col_index]))
      scenic_score_up = get_scenic_score(view_up, selected_tree)
      
      view_down =  trees_in_col[col_index+1:]
      scenic_score_down = get_scenic_score(view_down, selected_tree)
      
      total_scenic_score = scenic_score_right * scenic_score_left * scenic_score_up * scenic_score_down

      if total_scenic_score > max_scenic_score:
        max_scenic_score = total_scenic_score
  return max_scenic_score