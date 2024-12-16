from dataclasses import dataclass
from math import gcd


@dataclass(frozen=True)
class Vec2:
  x: int
  y: int

  def __add__(self, v):
    return Vec2(self.x + v.x, self.y + v.y)

  def __sub__(self, v):
    return Vec2(self.x - v.x, self.y - v.y)

  def __mul__(self, i):
    return Vec2(self.x * i, self.y * i)

  def __floordiv__(self, i):
    return Vec2(self.x // i, self.y // i)

  def __neg__(self):
    return Vec2(-self.x, -self.y)

  def shrunk(self):
    return self // gcd(self.x, self.y)

  def rotated(self, degrees: int):
    if degrees % 45 != 0:
      raise ValueError(f"Cannot rotate by {degrees} degrees.")

    if self not in Direction.ALL:
      raise ValueError(f"Cannot rotate {self}.")

    times = degrees // 45
    if times > 0:
      rotations = Direction.ROTATIONS_RIGHT
      d = 1
    else:
      rotations = Direction.ROTATIONS_LEFT
      d = -1

    result = self
    while times:
      result = rotations[result]
      times -= d

    return result


class Direction:
  NORTH = Vec2(0, -1)
  NORTH_EAST = Vec2(1, -1)
  EAST = Vec2(1, 0)
  SOUTH_EAST = Vec2(1, 1)
  SOUTH = Vec2(0, 1)
  SOUTH_WEST = Vec2(-1, 1)
  WEST = Vec2(-1, 0)
  NORTH_WEST = Vec2(-1, -1)

  ALL = (NORTH, NORTH_EAST, EAST, SOUTH_EAST, SOUTH, SOUTH_WEST, WEST, NORTH_WEST)
  MAIN = (NORTH, EAST, SOUTH, WEST)

  ROTATIONS_RIGHT = {
    NORTH: NORTH_EAST,
    NORTH_EAST: EAST,
    EAST: SOUTH_EAST,
    SOUTH_EAST: SOUTH,
    SOUTH: SOUTH_WEST,
    SOUTH_WEST: WEST,
    WEST: NORTH_WEST,
    NORTH_WEST: NORTH
  }

  ROTATIONS_LEFT = {
    NORTH: NORTH_WEST,
    NORTH_EAST: NORTH,
    EAST: NORTH_EAST,
    SOUTH_EAST: EAST,
    SOUTH: SOUTH_EAST,
    SOUTH_WEST: SOUTH,
    WEST: SOUTH_WEST,
    NORTH_WEST: WEST
  }

  ROTATIONS_MAIN_LEFT = {
    NORTH: WEST,
    EAST: NORTH,
    SOUTH: EAST,
    WEST: SOUTH
  }

  ROTATIONS_MAIN_RIGHT = {
    NORTH: EAST,
    EAST: SOUTH,
    SOUTH: WEST,
    WEST: NORTH
  }
