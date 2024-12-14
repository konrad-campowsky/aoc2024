import sys
from dataclasses import dataclass
from operator import attrgetter
from Grid import Grid, get_grid
from Vec2 import Vec2, Direction


@dataclass
class Region:
  plant: str
  plots: list


garden = get_grid()
regions = []
handled = set()


def scan_region(region):
  p = region.plots[-1]

  for d in Direction.MAIN:
    p2 = p + d
    if p2 not in handled and garden.get_tile(p2) == region.plant:
      handled.add(p2)
      region.plots.append(p2)
      scan_region(region)


for y, row in enumerate(garden):
  for x, plant in enumerate(row):
    p = Vec2(x, y)
    if p not in handled:
      handled.add(p)
      regions.append(Region(plant=plant, plots=[p]))
      scan_region(regions[-1])


def get_price1(region):
  perimeter = 0
  for p in region.plots:
    for d in Direction.MAIN:
      if garden.get_tile(p + d) != region.plant:
        perimeter += 1

  return perimeter * len(region.plots)


def get_price2(region):
  north_sides = 0
  for y in range(garden.num_rows):
    plots = [ p for p in region.plots if (p.y == y and garden.get_tile(p + Direction.NORTH) != region.plant) ]
    if plots:
      plots.sort(key=attrgetter("x"))
      north_sides += 1
      for i in range(1, len(plots)):
        if plots[i].x != plots[i-1].x + 1:
          north_sides += 1

  south_sides = 0
  for y in range(garden.num_rows):
    plots = [ p for p in region.plots if (p.y == y and garden.get_tile(p + Direction.SOUTH) != region.plant) ]
    if plots:
      plots.sort(key=attrgetter("x"))
      south_sides += 1
      for i in range(1, len(plots)):
        if plots[i].x != plots[i-1].x + 1:
          south_sides += 1

  east_sides = 0
  for x in range(garden.num_cols):
    plots = [ p for p in region.plots if (p.x == x and garden.get_tile(p + Direction.EAST) != region.plant) ]
    if plots:
      plots.sort(key=attrgetter("y"))
      east_sides += 1
      for i in range(1, len(plots)):
        if plots[i].y != plots[i-1].y + 1:
          east_sides += 1

  west_sides = 0
  for x in range(garden.num_cols):
    plots = [ p for p in region.plots if (p.x == x and garden.get_tile(p + Direction.WEST) != region.plant) ]
    if plots:
      plots.sort(key=attrgetter("y"))
      west_sides += 1
      for i in range(1, len(plots)):
        if plots[i].y != plots[i-1].y + 1:
          west_sides += 1

  return (north_sides + south_sides + west_sides + east_sides) * len(region.plots)


print (sum(map(get_price1, regions)))
print (sum(map(get_price2, regions)))


