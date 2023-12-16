#!/usr/bin/python3

# python3 -m doctest -v 16b.py

'''
'''


with open('input/16.txt', 'r') as f:
# with open('input/16-small.txt', 'r') as f:
    lines = f.readlines()
lines = [l.rstrip() for l in lines]
lines = [l for l in lines if l]

# up, left, down, right
#  0    1    2    3

# visit tile x,y with direction dir in tile x,y
def visit(x, y, beam_dir, visited): # from top, left, down, right
    candidates = []
    if not visited[y][x][beam_dir]:
        visited[y][x][beam_dir] = True
        if lines[y][x] == '-':
            if beam_dir == 0 or beam_dir == 2: # in x,y tile heading up/down
                if x - 1 > -1:
                    candidates.append((x - 1, y, 1)) # left
                if x + 1 < len(lines[0]):
                    candidates.append((x + 1, y, 3)) # right
            elif beam_dir == 1: # traverse - left
                if x - 1 > -1:
                    candidates.append((x - 1, y, 1)) # left
            else: # 3
                if x + 1 < len(lines[0]):
                    candidates.append((x + 1, y, 3)) # right
        elif lines[y][x] == '|':
            if beam_dir == 1 or beam_dir == 3: # in x,y tile heading left/right
                if y - 1 > -1:
                    candidates.append((x, y - 1, 0)) # up
                if y + 1 < len(lines):
                    candidates.append((x, y + 1, 2)) # down
            elif beam_dir == 0: # traverse | up
                if y - 1 > -1:
                    candidates.append((x, y - 1, 0)) # up
            else: # 2
                if y + 1 < len(lines):
                    candidates.append((x, y + 1, 2)) # down
        elif lines[y][x] == '\\':
            if beam_dir == 0: # in x,y tile heading up
                if x - 1 > -1:
                    candidates.append((x - 1, y, 1)) # left
            elif beam_dir == 1: # left
                if y - 1 > -1:
                    candidates.append((x, y - 1, 0)) # up
            elif beam_dir == 2: # down
                if x + 1 < len(lines[0]):
                    candidates.append((x + 1, y, 3)) # right
            else: # 3 right
                if y + 1 < len(lines):
                    candidates.append((x, y + 1, 2)) # down
        elif lines[y][x] == '/':
            if beam_dir == 0: # in x,y tile heading up
                if x + 1 < len(lines[0]):
                    candidates.append((x + 1, y, 3)) # right
            elif beam_dir == 1: # left
                if y + 1 < len(lines):
                    candidates.append((x, y + 1, 2)) # down
            elif beam_dir == 2: # down
                if x - 1 > -1:
                    candidates.append((x - 1, y, 1)) # left
            else: # 3 right
                if y - 1 > -1:
                    candidates.append((x, y - 1, 0)) # up
        else: # . traverse
            if beam_dir == 0: # in x,y tile heading up
                if y - 1 > -1:
                    candidates.append((x, y - 1, 0)) # up
            elif beam_dir == 1: # left
                if x - 1 > -1:
                    candidates.append((x - 1, y, 1)) # left
            elif beam_dir == 2: # down
                if y + 1 < len(lines):
                    candidates.append((x, y + 1, 2)) # down
            else: # 3 right
                if x + 1 < len(lines[0]):
                    candidates.append((x + 1, y, 3)) # right

    next = []
    for n in candidates:
        x, y, dir = n
        if not visited[y][x][dir]:
            next.append(n)
    return next

def process(x, y, dir):
    visited = [[[False, False, False, False] for i in l] for l in lines]
    beams = []
    beams.append((x, y, dir))
    while len(beams) > 0:
        next_beams = []
        for b in beams:
            bb = visit(b[0], b[1], b[2], visited)
            next_beams.extend(bb)
        beams = next_beams

    total = 0
    for l in visited:
        for tile in l:
            t = 0
            for dir in tile:
                if dir > 0:
                    t = 1
            total += t
    return total

max_total = 0
max_tile = (0, 0)
max_dir = 3

dir = 3 # heading right
x = 0
for y in range(len(lines)):
    c = process(x, y, dir)
    if c > max_total:
        max_total = c
        max_tile = (x, y)
        max_dir = dir

dir = 1 # heading left
x = len(lines[0]) - 1
for y in range(len(lines)):
    c = process(x, y, dir)
    if c > max_total:
        max_total = c
        max_tile = (x, y)
        max_dir = dir

dir = 2 # heading down
y = 0
for x in range(len(lines[0])):
    c = process(x, y, dir)
    if c > max_total:
        max_total = c
        max_tile = (x, y)
        max_dir = dir

dir = 0 # heading top
y = len(lines) - 1
for x in range(len(lines[0])):
    c = process(x, y, dir)
    if c > max_total:
        max_total = c
        max_tile = (x, y)
        max_dir = dir

print(f'max_total={max_total} tile=({max_tile[0]}, {max_tile[1]}) dir={max_dir}')
