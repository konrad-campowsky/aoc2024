#! /usr/bin/env python3

import sys
from Vec2 import Vec2


lines = tuple(map(str.strip, sys.stdin))
x_max = len(lines[0])
y_max = len(lines)
c = 0


def char_at(v):
  return lines[v.y][v.x]


def str_from(p, d):
  return char_at(p) + char_at(p + d) + char_at(p + d * 2)


def check_pos(p, d):
  return str_from(p, d) == 'MAS'


for y in range(1, y_max - 1):
  line = lines[y]
  for x in range(1, x_max - 1):
    if line[x] == 'A':
      p = Vec2(x, y)
      if ((check_pos(p - Vec2(1, 1), Vec2(1, 1)) or check_pos(p + Vec2(1, 1), Vec2(-1, -1)))
        and (check_pos(p + Vec2(-1, 1), Vec2(1, -1)) or check_pos(p + Vec2(1, -1), Vec2(-1, 1)))):
          c += 1

print(c)
