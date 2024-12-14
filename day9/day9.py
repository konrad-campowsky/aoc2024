#! /usr/bin/env python3

import sys

line = next(sys.stdin).strip()

disk = []
EMPTY = '.'

at_file = True
file_id = 0
free_count = 0
for count in line:
  count = int(count)
  if at_file:
    if count == 0:
      raise Exception("0 file")
    fill = file_id
    file_id += 1
  else:
    fill = EMPTY
    free_count += count

  disk.extend((fill,) * count)
  at_file = not at_file

print(file_id, len(disk), free_count)
#print(disk)

moved = 0
next_block = 0
while moved < free_count:
  moved += 1
  if moved % 1000 == 0:
    print(moved)
  block_to_move = disk.pop()
  if block_to_move != EMPTY:
    for i, block in enumerate(disk[next_block:]):
      if block == EMPTY:
        disk[i + next_block] = block_to_move
        next_block = i + 1
        break

print("move done", moved, len(disk))

#print(disk)

checksum = 0

for i, block in enumerate(disk):
  checksum += i * block

print(checksum)
