#!/usr/bin/python3

# python3 -m doctest -v 18b.py

'''
--- Part Two ---

The Elves were right to be concerned; the planned lagoon would be much too small.

After a few minutes, someone realizes what happened; someone swapped the color and instruction parameters when producing the dig plan. They don't have time to fix the bug; one of them asks if you can extract the correct instructions from the hexadecimal codes.

Each hexadecimal code is six hexadecimal digits long. The first five hexadecimal digits encode the distance in meters as a five-digit hexadecimal number. The last hexadecimal digit encodes the direction to dig: 0 means R, 1 means D, 2 means L, and 3 means U.

So, in the above example, the hexadecimal codes can be converted into the true instructions:

#70c710 = R 461937
#0dc571 = D 56407
#5713f0 = R 356671
#d2c081 = D 863240
#59c680 = R 367720
#411b91 = D 266681
#8ceee2 = L 577262
#caa173 = U 829975
#1b58a2 = L 112010
#caa171 = D 829975
#7807d2 = L 491645
#a77fa3 = U 686074
#015232 = L 5411
#7a21e3 = U 500254
Digging out this loop and its interior produces a lagoon that can hold an impressive 952408144115 cubic meters of lava.

Convert the hexadecimal color codes into the correct instructions; if the Elves follow this new dig plan, how many cubic meters of lava could the lagoon hold?
'''
import sys

# with open('input/18.txt', 'r') as f:
with open('input/18-small.txt', 'r') as f:
    lines = f.readlines()
lines = [l.rstrip() for l in lines]
lines = [l for l in lines if l]

cmds =[]
# for l in lines:
#     digits = l.split('#')[1].rstrip(')')
#     i = int(digits[:-1], 16)
#     c = int(digits[-1:])
#     cmds.append((c, i))

cm = {'R': 0, 'D': 1, 'L': 2, 'U': 3}

# 18a
for l in lines:
    c = cm[l[0]]
    parts = l.split(' ')
    i = int(parts[1])
    cmds.append((c, i))

vertices = []
min_x = min_y = max_x = max_y = 0
x = y = 0
vertices.append((x, y))
pp = -1 # exclude starting point since this is a loop
for (c, distance) in cmds:
    pp += distance
    if c == 0:
        x += distance
        if x > max_x:
            max_x = x
    elif c == 2:
        x -= distance
        if x < min_x:
            min_x = x
    elif c == 3:
        y -= distance
        if y < min_y:
            min_y = y
    elif c == 1:
        y += distance
        if y > max_y:
            max_y = y
    else:
        print('Err!')
        sys.exit(22)
    vertices.append((x, y))

print(f'min_x={min_x} min_y={min_y} max_x={max_x} max_y={max_y}')

width = max_x - min_x + 1
height = max_y - min_y + 1
print(f'(w={width} * h={height})')

width2 = max_x - min_x + 1 + 2
height2 = max_y - min_y + 1 + 2
print(f'(w2={width2} * h2={height2})')

start_x = 0 - min_x + 1
start_y = 0 - min_y + 1
print(f'start=({start_x}, {start_y})')

v2 = []
for (x, y) in vertices:
    v2.append((x - min_x + 1, y - min_y + 1))

# shoe
s = 0
for k in range(len(v2) - 1):
    x, y = v2[k]
    x2, y2 = v2[k + 1]
    s += x * y2 - y * x2

print(f's={s}')



print(f's-height={s - height}')
p = width + height - 1 + width - 1 + height - 2
print(f'p={p}')
print(f'pp={pp} 62-pp={61-pp}')
print(f's-p={s - p}')


# field = [['.' for x in range(width2)] for y in range(height2)]
#
# def print_field():
#     print(f'(w={width2} * h={height2})')
#     for l in field:
#         s = ''.join(l)
#         print(s)
#

#
# x, y = start_x, start_y
# for (c, distance) in cmds:
#     if c == 'R':
#         for cx in range(x, x + distance):
#             field[y][cx] = '#'
#         x += distance
#     elif c == 'L':
#         for cx in range(x, x - distance, -1):
#             field[y][cx] = '#'
#         x -= distance
#     elif c == 'U':
#         for cy in range(y, y - distance, -1):
#             field[cy][x] = '#'
#         y -= distance
#     elif c == 'D':
#         for cy in range(y, y + distance):
#             field[cy][x] = '#'
#         y += distance
#     else:
#         print('Err!')
#         sys.exit(22)
#
# q = []
# for x in range(len(field[0])):
#     field[0][x] = 'O'
#     q.append((x, 0))
#     field[height2 - 1][x] = 'O'
#     q.append((x, height2 - 1))
#
# for y in range(len(field)):
#     field[y][0] = 'O'
#     q.append((0, y))
#     field[y][width2 - 1] = 'O'
#     q.append((width2 - 1, y))
#
# def enq(x, y):
#     if field[y][x] == '.':
#         field[y][x] = 'O'
#         q.append((x, y))
#
# while len(q) > 0:
#     (x, y) = q.pop(0)
#     if x + 1 < width2:
#         enq(x + 1, y)
#     if x - 1 > -1:
#         enq(x - 1, y)
#     if y + 1 < height2:
#         enq(x, y + 1)
#     if y - 1 > -1:
#         enq(x, y - 1)
#
# filled = 0
# for y in range(len(field)):
#     for x in range(len(field[0])):
#         if field[y][x] != 'O':
#             field[y][x] = '#'
#             filled += 1
#
# print_field()
# print(f'filled={filled}')

