#!/usr/bin/python3

# python3 -m doctest -v 18.py

'''
--- Day 18: Lavaduct Lagoon ---

Thanks to your efforts, the machine parts factory is one of the first factories up and running since the lavafall came back. However, to catch up with the large backlog of parts requests, the factory will also need a large supply of lava for a while; the Elves have already started creating a large lagoon nearby for this purpose.

However, they aren't sure the lagoon will be big enough; they've asked you to take a look at the dig plan (your puzzle input). For example:

R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
The digger starts in a 1 meter cube hole in the ground. They then dig the specified number of meters up (U), down (D), left (L), or right (R), clearing full 1 meter cubes as they go. The directions are given as seen from above, so if "up" were north, then "right" would be east, and so on. Each trench is also listed with the color that the edge of the trench should be painted as an RGB hexadecimal color code.

When viewed from above, the above example dig plan would result in the following loop of trench (#) having been dug out from otherwise ground-level terrain (.):

#######
#.....#
###...#
..#...#
..#...#
###.###
#...#..
##..###
.#....#
.######
At this point, the trench could contain 38 cubic meters of lava. However, this is just the edge of the lagoon; the next step is to dig out the interior so that it is one meter deep as well:

#######
#######
#######
..#####
..#####
#######
#####..
#######
.######
.######
Now, the lagoon can contain a much more respectable 62 cubic meters of lava. While the interior is dug out, the edges are also painted according to the color codes in the dig plan.

The Elves are concerned the lagoon won't be large enough; if they follow their dig plan, how many cubic meters of lava could it hold?
'''
import sys

with open('input/18.txt', 'r') as f:
# with open('input/18-small.txt', 'r') as f:
    lines = f.readlines()
lines = [l.rstrip() for l in lines]
lines = [l for l in lines if l]

cmds =[]
for l in lines:
    c = l[0]
    parts = l.split(' ')
    i = int(parts[1])
    cmds.append((c, i))

min_x = min_y = max_x = max_y = 0
x = y = 0
for (c, distance) in cmds:
    if c == 'R':
        x += distance
        if x > max_x:
            max_x = x
    elif c == 'L':
        x -= distance
        if x < min_x:
            min_x = x
    elif c == 'U':
        y -= distance
        if y < min_y:
            min_y = y
    elif c == 'D':
        y += distance
        if y > max_y:
            max_y = y
    else:
        print('Err!')
        sys.exit(22)

print(f'min_x={min_x} min_y={min_y} max_x={max_x} max_y={max_y}')
width2 = max_x - min_x + 1 + 2
height2 = max_y - min_y + 1 + 2
field = [['.' for x in range(width2)] for y in range(height2)]

def print_field():
    print(f'(w={width2} * h={height2})')
    for l in field:
        s = ''.join(l)
        print(s)

start_x = 0 - min_x + 1
start_y = 0 - min_y + 1
print(f'start=({start_x}, {start_y})')

x, y = start_x, start_y
for (c, distance) in cmds:
    if c == 'R':
        for cx in range(x, x + distance):
            field[y][cx] = '#'
        x += distance
    elif c == 'L':
        for cx in range(x, x - distance, -1):
            field[y][cx] = '#'
        x -= distance
    elif c == 'U':
        for cy in range(y, y - distance, -1):
            field[cy][x] = '#'
        y -= distance
    elif c == 'D':
        for cy in range(y, y + distance):
            field[cy][x] = '#'
        y += distance
    else:
        print('Err!')
        sys.exit(22)

q = []
for x in range(len(field[0])):
    field[0][x] = 'O'
    q.append((x, 0))
    field[height2 - 1][x] = 'O'
    q.append((x, height2 - 1))

for y in range(len(field)):
    field[y][0] = 'O'
    q.append((0, y))
    field[y][width2 - 1] = 'O'
    q.append((width2 - 1, y))

def enq(x, y):
    if field[y][x] == '.':
        field[y][x] = 'O'
        q.append((x, y))

while len(q) > 0:
    (x, y) = q.pop(0)
    if x + 1 < width2:
        enq(x + 1, y)
    if x - 1 > -1:
        enq(x - 1, y)
    if y + 1 < height2:
        enq(x, y + 1)
    if y - 1 > -1:
        enq(x, y - 1)

filled = 0
for y in range(len(field)):
    for x in range(len(field[0])):
        if field[y][x] != 'O':
            field[y][x] = '#'
            filled += 1

print_field()
print(f'filled={filled}')

