#! /usr/bin/env python3

import sys
from itertools import takewhile
from Grid import get_grid
from Vec2 import Vec2, Direction


warehouse = get_grid(lambda x: x, container=list, lineiterator=takewhile(bool, map(str.strip, sys.stdin)))
orders = ''.join(map(str.strip, sys.stdin))

moves = {
 '^': Direction.NORTH,
 '>': Direction.EAST,
 'v': Direction.SOUTH,
 '<': Direction.WEST
}


def part2(warehouse):
  for y, line in enumerate(warehouse):
    for x, c in enumerate(line):
      if c == '@':
        robot = Vec2(x, y)
        break

  def move_h(p, d):
#    print('move_h', p, d)
#    print(warehouse)
    c = warehouse.get_tile(p)
#    print(c)
    if c == '#':
      return False
    if c == '.':
      return True
    if move(p + d, d):
      warehouse.set_tile(p + d, c)
      return True
    return False

  def test_box(p, d):
    print("test_box", p, d)
    if warehouse.get_tile(p) == '[':
      box = (p, p + Direction.EAST)
    else:
      if not warehouse.get_tile(p) == ']':
        raise Exception("Not a box at " + str(p))
      box = (p + Direction.WEST, p)

    box2 = (box[0] + d, box[1] + d)
    next_tiles = warehouse.get_tile(box[0] + d) + warehouse.get_tile(box[1] + d)

    print(next_tiles)

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
      print("Moving boxes", boxes)
      handled = set()
      for box in boxes:
        if warehouse.get_tile(box[0]) + warehouse.get_tile(box[1]) != '[]':
          raise Exception("Received not a box at " + str(box) + ": " + warehouse.get_tile(box[0]) + warehouse.get_tile(box[1]))

      for box in dict.fromkeys(boxes):
        print("Moving box", box)
        if warehouse.get_tile(box[0]) + warehouse.get_tile(box[1]) != '[]':
          raise Exception("Not a box at " + str(box) + ": " + warehouse.get_tile(box[0]) + warehouse.get_tile(box[1]))
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

  print(warehouse.prettyprint())

  for order in orders:
    d = moves[order]
    print (order)
    if order in '<>':
      move = move_h
    else:
      move = move_v

    if move(robot, d):
      warehouse.set_tile(robot, '.')
      robot = robot+d

    print(warehouse.prettyprint())
#    break


  s = 0
  for y, line in enumerate(warehouse):
    for x, c in enumerate(line):
      if c == '[':
        s += 100 * y + x
  print(s)



part2(warehouse)


