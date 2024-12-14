#! /usr/bin/env python3

import sys
from dataclasses import dataclass

line = next(sys.stdin).strip()

disk = []
EMPTY = -1

@dataclass
class Area:
  length: int
  file_id: int

  @property
  def is_empty(self):
    return self.file_id == EMPTY

at_file = True
file_id = 0
for count in line:
  count = int(count)
  if at_file:
    fill = file_id
    file_id += 1
  else:
    fill = EMPTY
    if count == 0:
      at_file = not at_file
      continue

  disk.append(Area(length=count, file_id=fill))
  at_file = not at_file

print(file_id, len(disk))


i = len(disk) - 1
while i >= 0:
  source_area = disk[i]
  i -= 1
  if source_area.file_id == EMPTY:
    continue
  for j, target_area in enumerate(disk):
    if target_area is source_area:
      break

    if target_area.is_empty:
      if target_area.length >= source_area.length:
        if target_area.length > source_area.length:
          disk.insert(j + 1, Area(length = target_area.length - source_area.length, file_id = EMPTY))
          target_area.length = source_area.length
          i += 1

        target_area.file_id = source_area.file_id
        source_area.file_id = EMPTY
        break

print("move done", len(disk))

checksum = 0
i = 0
for area in disk:
  if area.file_id == EMPTY:
    i += area.length
  else:
    target = i + area.length
    while i < target:
      checksum += area.file_id * i
      i += 1

print(checksum)

