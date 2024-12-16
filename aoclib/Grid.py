#! /usr/bin/env python3

from collections.abc import Sequence
from copy import deepcopy

from aocutil import puzzleinput
from Vec2 import Vec2


class Grid(Sequence):
  def __init__(self, grid):
    self.grid = grid
    self.height = len(grid)
    self.width = len(grid[0])

  def copy(self):
    return deepcopy(self)

  def get_tile(self, p):
    if p.x >= 0 and p.x < self.width and p.y >= 0 and p.y < self.height:
      return self[p.y][p.x]
    return None

  def set_tile(self, p, c):
    self.grid[p.y][p.x] = c

  def __iter__(self):
    return iter(self.grid)

  def __getitem__(self, i):
    return self.grid[i]

  def __len__(self):
    return len(self.grid)

  def find(self, c):
    for y, line in enumerate(self):
      for x, t in enumerate(line):
        if t == c:
          return Vec2(x=x, y=y)

  def wrap(self, p):
    return Vec2(x=p.x % self.width, y=p.y % self.height)

  def valid(self, p):
    return p.x >= 0 and p.x < self.width and p.y >= 0 and p.y < self.height

  def __str__(self):
    return '\n'.join(''.join(line) for line in self)

  def prettyprint(self):
    return '\n'.join((f'{y:3} ') + ''.join(line) for y, line in enumerate(self))


def get_grid(tilemapper=None, container=tuple, lineiterator=None):
  if lineiterator is None:
    lineiterator = puzzleinput()

  if tilemapper is not None:
    if tilemapper is True:
      tilemapper = lambda x: x
    grid = container(container(map(tilemapper, line)) for line in lineiterator)
  else:
    grid = container(lineiterator)

  return Grid(grid)
