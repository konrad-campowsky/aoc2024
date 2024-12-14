import sys
from functools import cache


@cache
def do_stone(stone: int, i, blinks):
  if i >= blinks:
    return 1

  if stone == 0:
    return do_stone(1, i + 1, blinks)

  stonestr = str(stone)
  if len(stonestr) % 2 == 0:
    first, second = stonestr[:len(stonestr)//2], stonestr[len(stonestr)//2:]
    return do_stone(int(first), i + 1, blinks) + do_stone(int(second), i + 1, blinks)

  return do_stone(stone * 2024, i + 1, blinks)


stones=next(sys.stdin).strip().split(" ")
print(sum([do_stone(int(stone), 0, 25) for stone in stones]))
print(sum([do_stone(int(stone), 0, 75) for stone in stones]))

