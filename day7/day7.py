#! /usr/bin/env python3

import sys
from itertools import product


lines = []
max_operands = 0

for line in sys.stdin:
  result, rest = line.split(":")
  operands = tuple(map(int, rest.strip().split(" ")))
  lines.append((int(result), operands))
  max_operands = max(max_operands, len(operands))

all_permutations = {n + 1: tuple(product((int.__add__, int.__mul__), repeat=n)) for n in range(1, max_operands)}

s = 0

for result, operands in lines:
  permutations = all_permutations[len(operands)]
  for permutation in permutations:
    first, rest = operands[0], operands[1:]
    for operator, operand in zip(permutation, rest):
      first = operator(first, operand)
    if first == result:
      s += result
      break

print(s)
