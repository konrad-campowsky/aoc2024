#! /usr/bin/env python3

import sys
from functools import cache
from Grid import get_grid
from Vec2 import Direction


def walk(p, d, c):
  if c > cost.get(p, sys.maxsize):
    return
  cost[p] = c

  if p != end:
    for d2, c2 in ((d, 1), (rot_right[d], 1001), (rot_left[d], 1001)):
      if maze.get_tile(p + d2) != '#':
        walk(p + d2, d2, c + c2)


@cache
def walk2(p, d, c):
  if p == end:
    return [p]

  tiles = []
  if c <= cost[end]:
    for d2, c2 in ((d, 1), (rot_right[d], 1001), (rot_left[d], 1001)):
      if maze.get_tile(p + d2) != '#':
        tiles += walk2(p + d2, d2, c + c2)

    if tiles:
      tiles = [p] + tiles

  return tiles

maze = get_grid()
start = maze.find('S')
end = maze.find('E')
cost = {start: 0}
rot_left = Direction.ROTATIONS_MAIN_LEFT
rot_right = Direction.ROTATIONS_MAIN_RIGHT

sys.setrecursionlimit(10000)
walk(start, Direction.EAST, 0)
seats = len(set(walk2(start, Direction.EAST, 0)))

print(cost[end])
print(seats)

