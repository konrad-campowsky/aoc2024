#! /usr/bin/env python3

import sys


def is_safe(t):
  st = sorted(t)
  if st == t or list(reversed(st)) == t:
    for i in range(1, len(t)):
      if abs(t[i] - t[i - 1]) not in (1, 2, 3):
        return False
    return True

  return False


def is_safe2(t):
  if is_safe(t):
    return True
  for i in range(len(t)):
    t2 = t.copy()
    t2.pop(i)
    if is_safe(t2):
      return True
  return False


safe = safe2 = 0

for line in sys.stdin:
  t = list(map(int, line.strip().split(" ")))
  if is_safe(t):
    safe += 1
  if is_safe2(t):
    safe2 += 1

print(safe, safe2)