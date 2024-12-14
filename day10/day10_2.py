#! /usr/bin/env python3

import sys
from Vec2 import Vec2, Direction


rows = []
heads = []
for y, line in enumerate(sys.stdin):
  row = []
  for x, c in enumerate(line.strip()):
    row.append(int(c) if c != '.' else -1)
    if c == '0':
      heads.append(Vec2(x, y))

  rows.append(row)


num_cols = len(rows[0])
num_rows = len(rows)


def test_path(p, height):
  if height == 9:
    return 1

  s = 0
  for d in Direction.MAIN:
    p2 = p + d

    if p2.x < 0 or p2.x >= num_rows or p2.y < 0 or p2.y >= num_cols:
      continue

    h2 = rows[p2.y][p2.x]
    if h2 == height + 1:
      s += test_path(p2, height + 1, visited)

  return s


s = 0
for head in heads:
  s += test_path(head, 0)

print(s)
