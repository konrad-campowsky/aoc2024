#! /usr/bin/env python3

from aocutil import puzzleinput
from functools import cache


colors = next(puzzleinput()).split(", ")
designs = tuple(puzzleinput())


def find_path(design):
  if not design:
    return True

  return any(find_path(design[len(c):]) for c in colors if design.startswith(c))


@cache
def find_all_paths(design):
  if not design:
    return 1

  return sum(find_all_paths(design[len(c):]) for c in colors if design.startswith(c))


print(sum(1 for d in designs if find_path(d)))
print(sum(find_all_paths(d) for d in designs))