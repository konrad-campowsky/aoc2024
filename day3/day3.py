#! /usr/bin/env python3

from re import findall, M

s = s2 = 0

with open("input") as f:
  input = f.read()

muls = findall(r'mul\((\d{1,3}),(\d{1,3})\)', input, M)
for a, b in muls:
  s += int(a) * int(b)

rs = ''
i = 0
do = True

while True:
  if do:
    try:
      j = input.index("don't", i)
    except ValueError:
      j = len(input)
    rs += input[i:j]
    i = j + 5
    do = False
  else:
    try:
      i = input.index("do", i) + 2
    except ValueError:
      break
    if not input[i:].startswith("n't"):
      do = True
    else:
      i += 3

muls = findall(r'mul\((\d{1,3}),(\d{1,3})\)', rs, M)
for a, b in muls:
  s2 += int(a) * int(b)

print(s, s2)