#! /usr/bin/env python3

import sys
from functools import cmp_to_key


rules = []

for line in sys.stdin:
  if "|" not in line:
    break

  rules.append(line.strip().split("|"))

orders = [ line.strip().split(",") for line in sys.stdin ]


def must_come_before(x, y):
  return [x, y] in rules


def is_legal_order(order):
  if len(order) == 1:
    return True

  item, rest = order[0], order[1:]
  for later_item in rest:
    if must_come_before(later_item, item):
      return False

  return is_legal_order(rest)


def cmp(x, y):
  if must_come_before(x, y):
    return -1
  if must_come_before(y, x):
    return 1
  return 0


s = s2 = 0

for order in orders:
  if is_legal_order(order):
    s += int(order[len(order) // 2])
  else:
    legal = sorted(order, key=cmp_to_key(cmp))
    s2 += int(legal[len(order) // 2])

print(s)
print(s2)


