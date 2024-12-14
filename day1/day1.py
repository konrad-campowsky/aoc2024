#! /usr/bin/env python3

import sys
from collections import Counter

left = []
right = []

for line in sys.stdin:
  s = line.strip().split(" ")
  left.append(int(s[0]))
  right.append(int(s[-1]))

left.sort()
right.sort()

d = 0
sim = 0
counted = Counter(right)

for i in range(len(left)):
  l = left[i]
  d += abs(l - right[i])
  sim += l * counted[l]

print(d)
print(sim)