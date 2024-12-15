#! /usr/bin/env python3

from itertools import takewhile

from aocutil import puzzleinput
from Grid import get_grid
from Vec2 import Vec2, Direction


moves = {
 '^': Direction.NORTH,
 '>': Direction.EAST,
 'v': Direction.SOUTH,
 '<': Direction.WEST
}


def part1(warehouse):
  for y, line in enumerate(warehouse):
    for x, c in enumerate(line):
      if c == '@':
        robot = Vec2(x, y)
        break

  def move(p, d):
    c = warehouse.get_tile(p)
    if c == '#':
      return False
    if c == '.':
      return True
    if move(p + d, d):
      warehouse.set_tile(p + d, c)
      return True
    return False


  for order in orders:
    d = moves[order]
    if move(robot, d):
      warehouse.set_tile(robot, '.')
      robot = robot+d


  s = 0
  for y, line in enumerate(warehouse):
    for x, c in enumerate(line):
      if c == 'O':
        s += 100 * y + x
  print(s)


def part2(warehouse):
  for y, line in enumerate(warehouse):
    for x, c in enumerate(line):
      if c == '@':
        robot = Vec2(x, y)
        break

  def move_h(p, d):
    c = warehouse.get_tile(p)
    if c == '#':
      return False
    if c == '.':
      return True
    if move(p + d, d):
      warehouse.set_tile(p + d, c)
      return True
    return False

  def test_box(p, d):
    if warehouse.get_tile(p) == '[':
      box = (p, p + Direction.EAST)
    else:
      box = (p + Direction.WEST, p)

    box2 = (box[0] + d, box[1] + d)
    next_tiles = warehouse.get_tile(box[0] + d) + warehouse.get_tile(box[1] + d)

    if next_tiles == '..':
      return True, [box]
    if "#" in next_tiles:
      return False, []
    if next_tiles == '[]' or next_tiles == '].':
      can_move, boxes = test_box(box2[0], d)
      return can_move, boxes + [box]
    if next_tiles == '.[':
      can_move, boxes = test_box(box2[1], d)
      return can_move, boxes + [box]

    cm1, boxes1 = test_box(box2[0], d)
    cm2, boxes2 = test_box(box2[1], d)
    return cm1 and cm2, boxes1 + boxes2 + [box]

  def move_boxes(p, d):
    can_move, boxes = test_box(p, d)
    if can_move:
      for box in dict.fromkeys(boxes):
        for p in box:
          warehouse.set_tile(p + d, warehouse.get_tile(p))
          warehouse.set_tile(p, '.')
      return True
    return False

  def move_v(p, d):
    c = warehouse.get_tile(p)
    if c == '#':
      return False
    if c == '.':
      return True
    if c in '[]':
      return move_boxes(p, d)
    if move(p + d, d):
      warehouse.set_tile(p + d, c)
      return True

#  print(warehouse.prettyprint())

  for order in orders:
    d = moves[order]
#    print (order)
    if order in '<>':
      move = move_h
    else:
      move = move_v

    if move(robot, d):
      warehouse.set_tile(robot, '.')
      robot = robot+d

#    print(warehouse.prettyprint())

  s = 0
  for y, line in enumerate(warehouse):
    for x, c in enumerate(line):
      if c == '[':
        s += 100 * y + x
  print(s)


def expand(line):
  for c in line:
    if c =='O':
      yield '['
      yield ']'
    else:
      yield c
      if c == '@':
        yield '.'
      else:
        yield c


warehouse = get_grid(lambda x: x, container=list, lineiterator=takewhile(bool, puzzleinput()))
orders = ''.join(puzzleinput())
warehouse2 = get_grid(lambda x: x, container=list, lineiterator=(expand(line) for line in warehouse))

part1(warehouse)
part2(warehouse2)


