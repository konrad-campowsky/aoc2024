#! /usr/bin/env python3

import sys
from collections import defaultdict
from copy import deepcopy
from Vec2 import Vec2, Direction


orgfield = [ list(line.strip().replace("^", "X")) for line in sys.stdin ]


for y, line in enumerate(orgfield):
  try:
    x = line.index("X")
  except ValueError:
    pass
  else:
    orgguard_pos = Vec2(x, y)
    break
else:
  raise Exception("Guard not found")


def run_iteration(field):
  guard_dir = Direction.NORTH
  guard_pos = orgguard_pos
  c = 1
  visited = defaultdict(set)

  def get_field(p):
    if p.x < 0 or p.y < 0:
      return None
    try:
      return field[p.y][p.x]
    except IndexError:
      return None


  def visit(p, d):
    field[p.y][p.x] = 'X'
    s = visited[p]
    if d in s:
      return True
    s.add(d)
    return False

  i = 0

  while True:
    next_pos = guard_pos + guard_dir
    current_field = get_field(guard_pos)
    next_field = get_field(next_pos)

    if next_field is None:
      break

    if next_field == "#":
      guard_dir = guard_dir.rotated(90)
    else:
      guard_pos = next_pos
      if next_field != 'X':
        c += 1

      if visit(guard_pos, guard_dir):
        return -1

  return c

print(run_iteration(deepcopy(orgfield)))

c2 = 0

for y in range(len(orgfield)):
  for x in range(len(orgfield[y])):
    if orgfield[y][x] != '.':
      continue

    field = deepcopy(orgfield)
    field[y][x] = '#'
    if run_iteration(field) == -1:
      c2 += 1

print(c2)
