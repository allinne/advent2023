#!/usr/bin/python3

# python3 -m doctest -v 16.py

'''
'''


# with open('input/16.txt', 'r') as f:
with open('input/16-small.txt', 'r') as f:
    lines = f.readlines()
lines = [l.rstrip() for l in lines]
lines = [l for l in lines if l]

# up, left, down, right
#  0    1    2    3
visited = [[[False, False, False, False] for x in y] for y in lines]
beams = []

# visit tile x,y with direction dir in tile x,y
def visit(x, y, beam_dir): # from top, left, down, right
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

beams.append((0, 0, 3))
while len(beams) > 0:
    next_beams = []
    for b in beams:
        bb = visit(b[0], b[1], b[2])
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
print(total)
