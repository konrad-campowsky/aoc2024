import sys
from collections import defaultdict
from dataclasses import dataclass
from parse import parse
from Vec2 import Vec2


@dataclass
class Robot:
  p: Vec2
  v: Vec2


def parse_line(line):
  r = parse("p={:d},{:d} v={:d},{:d}", line.strip())
  return Robot(p=Vec2(r[0], r[1]), v=Vec2(r[2], r[3]))


#width = 11
#height = 7
width=101
height=103
seconds = 100

robots = tuple(map(parse_line, sys.stdin))


def wrap(p):
  return Vec2(x=p.x % width, y=p.y % height)


top_left = top_right = bottom_left = bottom_right = 0

for robot in robots:
  p2 = wrap(robot.p + robot.v * 100)

  if p2.x < width // 2 and p2.y < height // 2:
    top_left += 1
  elif p2.x > width // 2 and p2.y < height // 2:
    top_right += 1
  elif p2.x < width // 2 and p2.y > height // 2:
    bottom_left += 1
  elif p2.x > width // 2 and p2.y > height // 2:
    bottom_right += 1


print(top_left * top_right * bottom_left * bottom_right)
print()

def test_board(second):
  board = [ [0 for _ in range(width)] for _ in range(height) ]
  for robot in robots:
    board[robot.p.y][robot.p.x] += 1
  for line in board:
    l = ''.join(map(str, line))
    if '1111111' in l:
      print_board(second, board)
      return


def print_board(second, board):
  print(second)

  for line in board:
    print(''.join(map(str, line)).replace('0', '.'))
  print("*" * width)
  print()
  return True


for second in range(100000):
  c = defaultdict(int)
  line_c = defaultdict(int)
  for robot in robots:
    robot.p = wrap(robot.p + robot.v)
    c[robot.p] += 1
    line_c[robot.p.y] += 1
  test_board(second)

