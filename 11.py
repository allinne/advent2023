#!/usr/bin/python3

# python3 -m doctest -v 11.py

'''
--- Day 11: Cosmic Expansion ---

You continue following signs for "Hot Springs" and eventually come across an observatory. The Elf within turns out to be a researcher studying cosmic expansion using the giant telescope here.

He doesn't know anything about the missing machine parts; he's only visiting for this research project. However, he confirms that the hot springs are the next-closest area likely to have people; he'll even take you straight there once he's done with today's observation analysis.

Maybe you can help him with the analysis to speed things up?

The researcher has collected a bunch of data and compiled the data into a single giant image (your puzzle input). The image includes empty space (.) and galaxies (#). For example:

...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
The researcher is trying to figure out the sum of the lengths of the shortest path between every pair of galaxies. However, there's a catch: the universe expanded in the time it took the light from those galaxies to reach the observatory.

Due to something involving gravitational effects, only some space expands. In fact, the result is that any rows or columns that contain no galaxies should all actually be twice as big.

In the above example, three columns and two rows contain no galaxies:

   v  v  v
 ...#......
 .......#..
 #.........
>..........<
 ......#...
 .#........
 .........#
>..........<
 .......#..
 #...#.....
   ^  ^  ^
These rows and columns need to be twice as big; the result of cosmic expansion therefore looks like this:

....#........
.........#...
#............
.............
.............
........#....
.#...........
............#
.............
.............
.........#...
#....#.......
Equipped with this expanded universe, the shortest path between every pair of galaxies can be found. It can help to assign every galaxy a unique number:

....1........
.........2...
3............
.............
.............
........4....
.5...........
............6
.............
.............
.........7...
8....9.......
In these 9 galaxies, there are 36 pairs. Only count each pair once; order within the pair doesn't matter. For each pair, find any shortest path between the two galaxies using only steps that move up, down, left, or right exactly one . or # at a time. (The shortest path between two galaxies is allowed to pass through another galaxy.)

For example, here is one of the shortest paths between galaxies 5 and 9:

....1........
.........2...
3............
.............
.............
........4....
.5...........
.##.........6
..##.........
...##........
....##...7...
8....9.......
This path has length 9 because it takes a minimum of nine steps to get from galaxy 5 to galaxy 9 (the eight locations marked # plus the step onto galaxy 9 itself). Here are some other example shortest path lengths:

Between galaxy 1 and galaxy 7: 15
Between galaxy 3 and galaxy 6: 17
Between galaxy 8 and galaxy 9: 5
In this example, after expanding the universe, the sum of the shortest path between all 36 pairs of galaxies is 374.

Expand the universe, then find the length of the shortest path between every pair of galaxies. What is the sum of these lengths?
'''


with open('input/11.txt', 'r') as f:
# with open('input/11-small.txt', 'r') as f:
    lines = f.readlines()
lines = [l.rstrip() for l in lines]
lines = [l for l in lines if l]

def expand_rows(ar):
    e = []
    for l in ar:
        e.append(l)
        if l.find('#') < 0:
            e.append(l)
    return e

def transpose(ar_strs):
    '''
    >>> transpose(['aa', '..'])
    ['a.', 'a.']
    '''
    res = []
    for x in range(len(ar_strs[0])):
        col_lst = [ar_strs[y][x] for y in range(len(ar_strs))]
        col = ''.join(col_lst)
        res.append(col)
    return res

expanded = expand_rows(lines)

# expand columns
tr = transpose(expanded)
tr_expanded = expand_rows(tr)

expanded2 = transpose(tr_expanded)

print(f'size of lines=({len(lines[0])}x{len(lines)})')
print(f'size of expanded2=({len(expanded2[0])}x{len(expanded2)})')

galaxies = []
for y in range(len(expanded2)):
    for x in range(len(expanded2[0])):
        if expanded2[y][x] != '.':
            galaxies.append((x, y))

# print(galaxies)
print(f'size of galaxies={len(galaxies)}')

# d = []
total = 0
for k in range(len(galaxies) - 1):
    first = galaxies[k]
    for j in range(k + 1, len(galaxies)):
        second = galaxies[j]
        dx = abs(first[0] - second[0])
        dy = abs(first[1] - second[1])
        path = dx + dy
        # d.append(path)
        total += path
# print(d)
print(f'total={total}')

