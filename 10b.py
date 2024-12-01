#!/usr/bin/python3

# python3 -m doctest -v 10.py

'''
--- Part Two ---

You quickly reach the farthest point of the loop, but the animal never emerges. Maybe its nest is within the a enclosed by the loop?

To determine whether it's even worth taking the time to search for such a nest, you should calculate how many tiles are contained within the loop. For example:

...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
The above loop encloses merely four tiles - the two pairs of . in the southwest and southeast (marked I below). The middle . tiles (marked O below) are not in the loop. Here is the same loop again with those regions marked:

...........
.S-------7.
.|F-----7|.
.||OOOOO||.
.||OOOOO||.
.|L-7OF-J|.
.|II|O|II|.
.L--JOL--J.
.....O.....
In fact, there doesn't even need to be a full tile path to the outside for tiles to count as outside the loop - squeezing between pipes is also allowed! Here, I is still within the loop and O is still outside the loop:

..........
.S------7.
.|F----7|.
.||OOOO||.
.||OOOO||.
.|L-7F-J|.
.|II||II|.
.L--JL--J.
..........
In both of the above examples, 4 tiles are enclosed by the loop.

Here's a larger example:

.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
The above sketch has many random bits of ground, some of which are in the loop (I) and some of which are outside it (O):

OF----7F7F7F7F-7OOOO
O|F--7||||||||FJOOOO
O||OFJ||||||||L7OOOO
FJL7L7LJLJ||LJIL-7OO
L--JOL7IIILJS7F-7L7O
OOOOF-JIIF7FJ|L7L7L7
OOOOL7IF7||L7|IL7L7|
OOOOO|FJLJ|FJ|F7|OLJ
OOOOFJL-7O||O||||OOO
OOOOL---JOLJOLJLJOOO
In this larger example, 8 tiles are enclosed by the loop.

Any tile that isn't part of the main loop can count as being enclosed by the loop. Here's another example with many bits of junk pipe lying around that aren't connected to the main loop at all:

FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
Here are just the tiles that are enclosed by the loop marked with I:

FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJIF7FJ-
L---JF-JLJIIIIFJLJJ7
|F|F-JF---7IIIL7L|7|
|FFJF7L7F-JF7IIL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
In this last example, 10 tiles are enclosed by the loop.

Figure out whether you have time to search for the nest by calculating the a within the loop. How many tiles are enclosed by the loop?
'''

# with open('input/10.txt', 'r') as f:
# with open('input/10-small.txt', 'r') as f:
# with open('input/10-small-2.txt', 'r') as f:
# with open('input/10-small-3.txt', 'r') as f:
# with open('input/10-small-4.txt', 'r') as f:
with open('input/10-small-5.txt', 'r') as f:
    lines = f.readlines()
lines = [l.rstrip() for l in lines]
lines = [l for l in lines if l]

def find_start(lines):
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == 'S':
                return (x, y)

start = find_start(lines)
print(f'start={start}')

visited = [[False for k in range(len(lines[0]))] for j in range(len(lines))]
visited[start[1]][start[0]] = True # a must so no traverse through S immediately

# calc: from 0 till every point of the path,
# up: positive
# down: negative
ar = [0, False] # area, goes up/down
# on first goes up/down need to add/substract start[0]
ops = []

def change_start(curr, prev):
    d = 0
    if curr[1] > prev[1]: # down: -
        d = -prev[0]
    elif curr[1] < prev[1]: # up: +
        d = prev[0] + 1
    if d != 0:
        ops.append(d)
        ar[0] += d

def change(prev, curr, next):
    d = 0
    if next[1] > curr[1]: # down: -
        d = -curr[0]
    elif next[1] < curr[1]: # up: +
        d = curr[0] + 1
    else: # left or right
        if curr[1] != prev[1]: # if curr is a corner
            if curr[0] < next[0]: # go right after the corner
                d = -curr[0]
            elif next[0] < curr[0]:
                d = curr[0] + 1

    if d != 0:
        ops.append(d)
        ar[0] += d

q = []
# q = [(start, 0)]

def enq_start():
    top = (start[0], start[1] - 1)
    bottom = (start[0], start[1] + 1)
    left = (start[0] - 1, start[1])
    right = (start[0] + 1, start[1])

    if top[1] > -1:
        if not visited[top[1]][top[0]]:
            ch = lines[top[1]][top[0]]
            if ch == '|' or ch == 'F' or ch == '7':
                # going up: start is up too, will go bottom at the end
                # +1: outside
                # change(start[0] + 1)
                # change(top[0] + 1)
                # ar[1] = True # starting tile: consider up

                change_start(top, start)

                q.append((top, 1))
                visited[top[1]][top[0]] = True
                print('first is top')
                return # only one

    if bottom[1] < len(lines):
        if not visited[bottom[1]][bottom[0]]:
            ch = lines[bottom[1]][bottom[0]]
            if ch == '|' or ch == 'J' or ch == 'L':
                # ar[1] = True # starting tile: consider down
                # change(-start[0])
                # change(-bottom[0]) # down: -

                change_start(bottom, start)

                q.append((bottom, 1))
                visited[bottom[1]][bottom[0]] = True
                print('first is bottom')
                return # only one

    if left[0] > -1:
        if not visited[left[1]][left[0]]:
            ch = lines[left[1]][left[0]]
            if ch == '-' or ch == 'F' or ch == 'L':
                # change(left[0]) # left: +

                change_start(left, start)

                visited[left[1]][left[0]] = True
                q.append((left, 1))
                print('first is left')
                return # only one

    if right[0] < len(lines[0]):
        if not visited[right[1]][right[0]]:
            ch = lines[right[1]][right[0]]
            if ch == '-' or ch == 'J' or ch == '7':
                # change(-right[0]) # right: -

                change_start(right, start)

                visited[right[1]][right[0]] = True
                q.append((right, 1))
                print('first is right')
                return # only one

enq_start()

def enq(curr, cnt, prev):
    c = lines[curr[1]][curr[0]]

    top = (curr[0], curr[1] - 1)
    bottom = (curr[0], curr[1] + 1)
    left = (curr[0] - 1, curr[1])
    right = (curr[0] + 1, curr[1])

    if c == 'J' or c == '|' or c == 'L':
        if top[1] > -1:
            if not visited[top[1]][top[0]]:
                # if not ar[1]:
                #     ar[1] = True # first up
                #     change(start[0] + 1) # going up: start is up too, will go bottom at the end
                # change(curr[0] + 1) # up: +; +1: outside
                change(prev, curr, top)

                visited[top[1]][top[0]] = True
                q.append((top, cnt + 1))

    if c == '|' or c == '7' or c == 'F':
        if bottom[1] < len(lines):
            if not visited[bottom[1]][bottom[0]]:
                # if not ar[1]:
                #     ar[1] = True # first down/up
                #     change(-start[0])
                # change(-curr[0]) # down -
                change(prev, curr, bottom)

                visited[bottom[1]][bottom[0]] = True
                q.append((bottom, cnt + 1))

    if c == '-' or c == '7' or c == 'J':
        if left[0] > -1:
            if not visited[left[1]][left[0]]:
                # change(curr[0] + 1) # left: +
                change(prev, curr, left)

                visited[left[1]][left[0]] = True
                q.append((left, cnt + 1))

    if c == '-' or c == 'F' or c == 'L':
        if right[0] < len(lines[0]):
            if not visited[right[1]][right[0]]:
                # ? depends on direction in path
                # change(-curr[0]) # right: -
                change(prev, curr, right)

                visited[right[1]][right[0]] = True
                q.append((right, cnt + 1))
p = 0
first = q[0][0]
last = start
prev = start
while len(q) > 0:
    curr, cnt = q.pop(0)
    last = curr
    p = cnt
    print(f'curr={curr}')
    print(f'ar={ar}')
    enq(curr, cnt, prev)
    prev = curr
else:
    # finally process transition to S
    # last -> start
    visited[start[1]][start[0]] = False
    enq(last, 0, prev)

    # # finally process transition to S
    # # last -> start
    # visited[first[1]][first[0]] = False
    # enq(start, 0, last)

p += 1 # starting from 0; need num of tiles
area = ar[0] - p

print(f'ar={ar}')
print(f'ops={ops}')
print(f'P={p}')
print(f'area={area}')

