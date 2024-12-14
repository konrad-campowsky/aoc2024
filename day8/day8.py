#! /usr/bin/env python3

import sys
from collections import defaultdict
from itertools import combinations
from Vec2 import Vec2


antennas = defaultdict(list)

for y, line in enumerate(sys.stdin):
  for x, c in enumerate(line.strip()):
    if c != ".":
      antennas[c].append(Vec2(x, y))

x_max = x
y_max = y

unique1 = set()


def valid_pos(v):
  return v.x >= 0 and v.x <= x_max and v.y >= 0 and v.y <= y_max


for frequency_antennas in antennas.values():
  for a1, a2 in combinations(frequency_antennas, 2):
    d1 = a1 - a2
    an1 = a1 + d1
    if valid_pos(an1):
      unique1.add(an1)
    d2 = a2 - a1
    an2 = a2 + d2
    if valid_pos(an2):
      unique1.add(an2)


print(x_max, y_max)
print(len(unique1))

unique2 = set()

for frequency_antennas in antennas.values():
  for a1, a2 in combinations(frequency_antennas, 2):
    unique2.add(a1)

    d = (a1 - a2).shrunk()
    an = a1
    while True:
      an = an + d
      if not valid_pos(an):
        break
      unique2.add(an)

    an = a1
    while True:
      an = an - d
      if not valid_pos(an):
        break
      unique2.add(an)

print(len(unique2))
