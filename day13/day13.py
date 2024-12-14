import sys, numpy as np
from parse import parse

systems = []

while True:
  r = (
    parse("Button A: X+{:d}, Y+{:d}", next(sys.stdin).strip()),
    parse("Button B: X+{:d}, Y+{:d}", next(sys.stdin).strip()),
    parse("Prize: X={:d}, Y={:d}", next(sys.stdin).strip()),
  )

  systems.append(( ((r[0][0], r[1][0]), (r[0][1], r[1][1])), tuple(r[2]) ))

  try:
    next(sys.stdin)
  except StopIteration:
    break

s = s2 = 0
for a, b in systems:
  x1, x2 = np.linalg.solve(a, b)
  if round(x1, 5).is_integer() and round(x2, 5).is_integer():
    s += 3 * int(round(x1, 5)) + int(round(x2, 5))

  b2 = (b[0] + 10000000000000, b[1] + 10000000000000)
  x1, x2 = np.linalg.solve(a, b2)
  if round(x1, 4).is_integer() and round(x2, 4).is_integer():
    s2 += 3 * int(round(x1, 4)) + int(round(x2, 4))

print(s)
print(s2)
