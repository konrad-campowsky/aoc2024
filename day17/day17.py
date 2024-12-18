#! /usr/bin/env python3

import sys


A = int(next(sys.stdin).split(":")[1].strip())
B = int(next(sys.stdin).split(":")[1].strip())
C = int(next(sys.stdin).split(":")[1].strip())
next(sys.stdin)
program = list(map(int, next(sys.stdin).split(":")[1].strip().split(",")))


def execute(A, B, C, program):
  ip=0
  output = []

  def combo(operand):
    if 0 <= operand <= 3:
      return operand
    if operand == 4:
      return A
    if operand == 5:
      return B
    if operand == 6:
      return C
    raise ValueError("Illegal combo oeprand " + str(operand))

  while True:
    try:
      opcode, operand = program[ip], program[ip+1]
    except IndexError:
      return output

    if opcode == 0:
      A //= (2 ** combo(operand))
    elif opcode == 1:
      B ^= operand
    elif opcode == 2:
      B = combo(operand) % 8
    elif opcode == 3:
      if A:
        ip = operand
        continue
    elif opcode == 4:
      B ^= C
    elif opcode == 5:
      output.append(combo(operand) % 8)
    elif opcode == 6:
      B = A // (2 ** combo(operand))
    elif opcode == 7:
      C = A // (2 ** combo(operand))

    ip += 2


def search(a, target):
  for a in range(a * 8, a * 8 + 8):
    output = execute(a, 0, 0, program)
    if output[0] == target[0]:
      if len(target) == 1:
        return a
      r = search(a, target[1:])
      if r >= 0:
        return r

  return -1


print(','.join(map(str, execute(A, B, C, program))))
print(search(0, program[::-1]))
