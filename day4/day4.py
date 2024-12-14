#! /usr/bin/env python3

import sys
from Vec2 import Vec2, Direction


lines = tuple(map(str.strip, sys.stdin))
x_max = len(lines[0])
y_max = len(lines)
c = 0


def char_at(v):
  return lines[v.y][v.x]


def str_from(p, d):
  return char_at(p + d) + char_at(p + d * 2) + char_at(p + d * 3)


def check_pos(p, d):
  global c
  if str_from(p, d) == 'MAS':
    c += 1


for y in range(len(lines)):
  line = lines[y]
  for x in range(len(line)):
    char = line[x]

    if char == 'X':
      p = Vec2(x, y)
      if x >= 3 and y >= 3:
        check_pos(p, Direction.NORTH_WEST)
      if y >= 3:
        check_pos(p, Direction.NORTH)
      if x + 3 < x_max and y >= 3:
        check_pos(p, Direction.NORTH_EAST)
      if x + 3 < x_max:
        check_pos(p, Direction.EAST)
      if x + 3 < x_max and y + 3 < y_max:
        check_pos(p, Direction.SOUTH_EAST)
      if y + 3 < y_max:
        check_pos(p, Direction.SOUTH)
      if x >= 3 and y + 3 < y_max:
        check_pos(p, Direction.SOUTH_WEST)
      if x >= 3:
        check_pos(p, Direction.WEST)

print(c)
