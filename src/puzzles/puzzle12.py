
from typing import List, Tuple
from generic.read_inputs import read_txt_list_from_nr

from collections import namedtuple


Point = namedtuple("Point", "x y")


def parse_height_map(
  input: List[str]
) -> Tuple[List[List[int]], Point, Point]:
  map = []
  start = None
  end = None
  for row, chars in enumerate(input):
    chars = chars.replace('\n','')
    elev = []
    for col, c in enumerate(chars):
      if c == 'S':
        c = 'a'
        start = Point(row, col)
      elif c == 'E':
        c = 'z'
        end = Point(row, col)
      elev.append('abcdefghijklmnopqrstuvwxyz'.index(c))
    map.append(elev)
  return map, start, end


def allowed_next_steps(
  point: Point,
  map: List[List[int]],
  dist_map: List[List[int]]
) -> List[Point]:

  neighbour_points = []
  if point.x-1 >= 0 and dist_map[point.x-1][point.y] == -1:
    neighbour_points.append(Point(point.x-1, point.y))
  if point.y-1 >= 0 and dist_map[point.x][point.y-1] == -1:
    neighbour_points.append(Point(point.x, point.y-1))
  if point.x+1 <= len(map)-1 and dist_map[point.x+1][point.y] == -1:
    neighbour_points.append(Point(point.x+1, point.y))
  if point.y+1 <= len(map[0])-1 and dist_map[point.x][point.y+1] == -1:
    neighbour_points.append(Point(point.x, point.y+1))
  
  allowed_next_steps = []
  for neighbour in neighbour_points:
    if map[point.x][point.y] >= map[neighbour.x][neighbour.y] - 1:
      allowed_next_steps.append(neighbour)
  return allowed_next_steps


def find_distances_start_to_end(
  map: List[List[int]],
  start: Point,
  end: Point
) -> int:
  distance_map = get_distance_map(map, start, end)
  if distance_map is None:
    return None

  return distance_map[end.x][end.y]


def find_distances_nearest_low_point_to_end(
  map: List[List[int]],
  start: Point,
  end: Point
) -> int:
  low_points = []
  for x in range(len(map)):
    for y in range(len(map[0])):
      if map[x][y] == 0:
        low_points.append(Point(x,y))
  
  low_point_distances = []
  for low_point in low_points:
    low_point_distance = find_distances_start_to_end(map, low_point, end)
    if low_point_distance is not None:
      low_point_distances.append(low_point_distance)
  print(low_point_distances)
  return min(low_point_distances)


def get_distance_map(
  map: List[List[int]],
  start: Point,
  end: Point
) -> int:
  width = len(map)
  height = len(map[0])
  distance_map = []
  for x in range(width):
    distance_map.append([-1] * height)
  
  last_forwardpoints = [start]

  distance_map[start.x][start.y] = 0

  distance = 0
  while distance_map[end.x][end.y] == -1:
    distance += 1
    new_forwardpoints = []
    for forwardpoint in last_forwardpoints:
      next_steps = allowed_next_steps(forwardpoint, map, distance_map)
      for next in next_steps:
        distance_map[next.x][next.y] = distance
      new_forwardpoints = new_forwardpoints + next_steps
    if len(new_forwardpoints) == 0:
      return None
    last_forwardpoints = new_forwardpoints
  return distance_map


def part1(use_example:bool=False) -> int:
  input = read_txt_list_from_nr(12, use_example=use_example)
  map, start, end = parse_height_map(input)
  
  distance = find_distances_start_to_end(map, start, end)
  
  return distance


def part2(use_example:bool=False) -> int:
  input = read_txt_list_from_nr(12, use_example=use_example)
  map, start, end = parse_height_map(input)
  
  distance = find_distances_nearest_low_point_to_end(map, start, end)
  
  return distance
