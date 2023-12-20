#!/usr/bin/python3

# python3 -m doctest -v 10.py

'''
--- Day 10: Pipe Maze ---

You use the hang glider to ride the hot air from Desert Island all the way up to the floating metal island. This island is surprisingly cold and there definitely aren't any thermals to glide on, so you leave your hang glider behind.

You wander around for a while, but you don't find any people or animals. However, you do occasionally find signposts labeled "Hot Springs" pointing in a seemingly consistent direction; maybe you can find someone at the hot springs and ask them where the desert-machine parts are made.

The landscape here is alien; even the flowers and trees are made of metal. As you stop to admire some metal grass, you notice something metallic scurry away in your peripheral vision and jump into a big pipe! It didn't look like any animal you've ever seen; if you want a better look, you'll need to get ahead of it.

Scanning the area, you discover that the entire field you're standing on is densely packed with pipes; it was hard to tell at first because they're the same metallic silver color as the "ground". You make a quick sketch of all of the surface pipes you can see (your puzzle input).

The pipes are arranged in a two-dimensional grid of tiles:

| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
Based on the acoustics of the animal's scurrying, you're confident the pipe that contains the animal is one large, continuous loop.

For example, here is a square loop of pipe:

.....
.F-7.
.|.|.
.L-J.
.....
If the animal had entered this loop in the northwest corner, the sketch would instead look like this:

.....
.S-7.
.|.|.
.L-J.
.....
In the above diagram, the S tile is still a 90-degree F bend: you can tell because of how the adjacent pipes connect to it.

Unfortunately, there are also many pipes that aren't connected to the loop! This sketch shows the same loop as above:

-L|F7
7S-7|
L|7||
-L-J|
L|-JF
In the above diagram, you can still figure out which pipes form the main loop: they're the ones connected to S, pipes those pipes connect to, pipes those pipes connect to, and so on. Every pipe in the main loop connects to its two neighbors (including S, which will have exactly two pipes connecting to it, and which is assumed to connect back to those two pipes).

Here is a sketch that contains a slightly more complex main loop:

..F7.
.FJ|.
SJ.L7
|F--J
LJ...
Here's the same example sketch with the extra, non-main-loop pipe tiles also shown:

7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
If you want to get out ahead of the animal, you should find the tile in the loop that is farthest from the starting position. Because the animal is in the pipe, it doesn't make sense to measure this by direct distance. Instead, you need to find the tile that would take the longest number of steps along the loop to reach from the starting point - regardless of which way around the loop the animal went.

In the first example with the square loop:

.....
.S-7.
.|.|.
.L-J.
.....
You can count the distance each tile in the loop is from the starting point like this:

.....
.012.
.1.3.
.234.
.....
In this example, the farthest point from the start is 4 steps away.

Here's the more complex loop again:

..F7.
.FJ|.
SJ.L7
|F--J
LJ...
Here are the distances for each tile on that loop:

..45.
.236.
01.78
14567
23...
Find the single giant loop starting at S. How many steps along the loop does it take to get from the starting position to the point farthest from the starting position?
'''

with open('input/10.txt', 'r') as f:
# with open('input/10-small.txt', 'r') as f:
# with open('input/10-small-2.txt', 'r') as f:
# with open('input/10-small-3.txt', 'r') as f:
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
visited[start[1]][start[0]] = True

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
                visited[top[1]][top[0]] = True
                q.append((top, 1))

    if bottom[1] < len(lines):
        if not visited[bottom[1]][bottom[0]]:
            ch = lines[bottom[1]][bottom[0]]
            if ch == '|' or ch == 'J' or ch == 'L':
                visited[bottom[1]][bottom[0]] = True
                q.append((bottom, 1))

    if left[0] > -1:
        if not visited[left[1]][left[0]]:
            ch = lines[left[1]][left[0]]
            if ch == '-' or ch == 'F' or ch == 'L':
                visited[left[1]][left[0]] = True
                q.append((left, 1))

    if right[0] < len(lines[0]):
        if not visited[right[1]][right[0]]:
            ch = lines[right[1]][right[0]]
            if ch == '-' or ch == 'J' or ch == '7':
                visited[right[1]][right[0]] = True
                q.append((right, 1))

enq_start()

def enq(curr, cnt):
    c = lines[curr[1]][curr[0]]

    top = (curr[0], curr[1] - 1)
    bottom = (curr[0], curr[1] + 1)
    left = (curr[0] - 1, curr[1])
    right = (curr[0] + 1, curr[1])

    if c == 'J' or c == '|' or c == 'L':
        if top[1] > -1:
            if not visited[top[1]][top[0]]:
                visited[top[1]][top[0]] = True
                q.append((top, cnt + 1))

    if c == '|' or c == '7' or c == 'F':
        if bottom[1] < len(lines):
            if not visited[bottom[1]][bottom[0]]:
                visited[bottom[1]][bottom[0]] = True
                q.append((bottom, cnt + 1))

    if c == '-' or c == '7' or c == 'J':
        if left[0] > -1:
            if not visited[left[1]][left[0]]:
                visited[left[1]][left[0]] = True
                q.append((left, cnt + 1))

    if c == '-' or c == 'F' or c == 'L':
        if right[0] < len(lines[0]):
            if not visited[right[1]][right[0]]:
                visited[right[1]][right[0]] = True
                q.append((right, cnt + 1))

while len(q) > 0:
    curr = q.pop(0)
    print(curr)
    enq(curr[0], curr[1])
