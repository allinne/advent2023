#!/usr/bin/python3

# python3 -m doctest -v 21.py

'''
--- Day 21: Step Counter ---

You manage to catch the airship right as it's dropping someone else off on their all-expenses-paid trip to Desert Island! It even helpfully drops you off near the gardener and his massive farm.

"You got the sand flowing again! Great work! Now we just need to wait until we have enough sand to filter the water for Snow Island and we'll have snow again in no time."

While you wait, one of the Elves that works with the gardener heard how good you are at solving problems and would like your help. He needs to get his steps in for the day, and so he'd like to know which garden plots he can reach with exactly his remaining 64 steps.

He gives you an up-to-date map (your puzzle input) of his starting position (S), garden plots (.), and rocks (#). For example:

...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
The Elf starts at the starting position (S) which also counts as a garden plot. Then, he can take one step north, south, east, or west, but only onto tiles that are garden plots. This would allow him to reach any of the tiles marked O:

...........
.....###.#.
.###.##..#.
..#.#...#..
....#O#....
.##.OS####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
Then, he takes a second step. Since at this point he could be at either tile marked O, his second step would allow him to reach any garden plot that is one step north, south, east, or west of any tile that he could have reached after the first step:

...........
.....###.#.
.###.##..#.
..#.#O..#..
....#.#....
.##O.O####.
.##.O#...#.
.......##..
.##.#.####.
.##..##.##.
...........
After two steps, he could be at any of the tiles marked O above, including the starting position (either by going north-then-south or by going west-then-east).

A single third step leads to even more possibilities:

...........
.....###.#.
.###.##..#.
..#.#.O.#..
...O#O#....
.##.OS####.
.##O.#...#.
....O..##..
.##.#.####.
.##..##.##.
...........
He will continue like this until his steps for the day have been exhausted. After a total of 6 steps, he could reach any of the garden plots marked O:

...........
.....###.#.
.###.##.O#.
.O#O#O.O#..
O.O.#.#.O..
.##O.O####.
.##.O#O..#.
.O.O.O.##..
.##.#.####.
.##O.##.##.
...........
In this example, if the Elf's goal was to get exactly 6 more steps today, he could use them to reach any of 16 garden plots.

However, the Elf actually needs to get 64 steps today, and the map he's handed you is much larger than the example map.

Starting from the garden plot marked S on your map, how many garden plots could the Elf reach in exactly 64 steps?
'''

with open('input/21.txt', 'r') as f:
# with open('input/21-small.txt', 'r') as f:
    lines = f.readlines()
lines = [l.rstrip() for l in lines]
lines = [[ch for ch in l] for l in lines if l]


start_x, start_y = 0, 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == 'S':
            start_x, start_y = x, y
            break
lines[start_y][start_x] = '.'

def step(q):
    new_q = set()
    for (x, y) in q:
        if x - 1 > -1:
            if lines[y][x - 1] != '#':
                new_q.add((x - 1, y))
        if x + 1 < len(lines[0]):
            if lines[y][x + 1] != '#':
                new_q.add((x + 1, y))
        if y - 1 > -1:
            if lines[y - 1][x] != '#':
                new_q.add((x, y - 1))
        if y + 1 < len(lines):
            if lines[y + 1][x] != '#':
                new_q.add((x, y + 1))
    return list(new_q)

q = [(start_x, start_y)]
for i in range(64):
    q = step(q)

for (x, y) in q:
    lines[y][x] = 'O'
for l in lines:
    print(''.join(l))
print(f'num={len(q)}')


