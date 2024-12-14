#! /usr/bin/env python3

import sys
from Vec2 import Vec2, Direction

HEAD = 0
DIRECTIONS = (Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST)

rows = []
heads = []
for y, line in enumerate(sys.stdin):
#  line = tuple(map(int, line.strip()))
  row = []
  for c in line.strip():
    if c == '.':
      row.append(-1)
    else:
      row.append(int(c))

  rows.append(row)
  for x, c in enumerate(row):
    if c == HEAD:
      heads.append(Vec2(x, y))

num_cols = len(rows[0])
num_rows = len(rows)



#print(rows)


def test_path(p, height, visited):
  if height == 9:
    return 1

#  print("Visiting", p, "at height", height)

  s = 0
  for d in DIRECTIONS:
    p2 = p + d

#    if height == 3:
#      print("HUHU at", p, d, (p2.x < 0 or p2.x >= num_rows or p2.y < 0 or p2.y >= num_cols))



    if p2.x < 0 or p2.x >= num_rows or p2.y < 0 or p2.y >= num_cols:
      continue

    h2 = rows[p2.y][p2.x]

#    print ("Testing", p2, "with heights", height, " -> ", h2)

    if h2 == height + 1:
      s += test_path(p2, height + 1, visited)

  return s

s = 0
for head in heads:
  s += test_path(head, 0, set())

print(s)
