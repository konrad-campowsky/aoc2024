#! /usr/bin/env python3

from Vec2 import Vec2


class Grid:
  def __init__(self, grid):
    self.grid = grid
    self.height = len(grid)
    self.width = len(grid[0])

  def get_tile(self, p):
    if p.x >= 0 and p.x < self.num_cols and p.y >= 0 and p.y < self.num_rows:
      return self.grid[p.y][p.x]
    return None

  def __iter__(self):
    return iter(self.grid)

  def wrap(p):
    return Vec2(x=p.x % self.width, y=p.y % self.height)


def get_grid(tilemapper=None, container=tuple, lineiterator=None):
  if lineiterator is None:
    import sys
    lineiterator = sys.stdin

  if tilemapper is not None:
    grid = container(container(map(tilemapper, line.strip())) for line in lineiterator)
  else:
    grid = container(line.strip() for line in lineiterator)

  return Grid(grid)
