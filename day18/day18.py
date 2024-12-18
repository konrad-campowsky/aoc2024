#! /usr/bin/env python3

import sys

from aocutil import puzzleinput
from Grid import get_grid
from Vec2 import Vec2, Direction, parse_vec2


WIDTH = HEIGHT = 71 #7
LIMIT = 1024 #12
end = Vec2(WIDTH-1, HEIGHT-1)
positions = list(map(parse_vec2, puzzleinput()))


def get_d18_grid(limit):
  def get_tile(x, y):
    return '#' if Vec2(x, y) in positions[:limit] else '.'

  return get_grid(lineiterator=([get_tile(x, y) for x in range(WIDTH)] for y in range(HEIGHT)))


def shortest_path():
  cost = {}
  grid = get_d18_grid(LIMIT)
  def walk(p, c):
    if c >= cost.get(p, sys.maxsize):
      return
    cost[p] = c

    if p != end:
      for d in Direction.MAIN:
        if grid.get_tile(p + d) == '.':
          walk(p + d, c + 1)

  walk(Vec2(0, 0), 0)
  return cost[end]


def path_exists(grid):
  visited=set()
  def walk(p):
    if p == end:
      return True
    visited.add(p)
    return any(walk(p + d) for d in Direction.MAIN if grid.get_tile(p + d) == '.' and (p + d) not in visited)
  return walk(Vec2(0, 0))


def first_block():
  maxfree = LIMIT
  maxblock = len(positions)

  while maxfree < maxblock - 1:
    t = maxfree + (maxblock - maxfree) // 2
    grid = get_d18_grid(t)
    if path_exists(grid):
      maxfree = t
    else:
      maxblock = t

  return positions[maxfree]


sys.setrecursionlimit(100000)
print(shortest_path())
print(first_block().shortstr())
