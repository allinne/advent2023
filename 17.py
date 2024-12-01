#!/usr/bin/python3

# python3 -m doctest -v 17.py

'''
--- Day 17: Clumsy Crucible ---

The lava starts flowing rapidly once the Lava Production Facility is operational. As you leave, the reindeer offers you a parachute, allowing you to quickly reach Gear Island.

As you descend, your bird's-eye view of Gear Island reveals why you had trouble finding anyone on your way up: half of Gear Island is empty, but the half below you is a giant factory city!

You land near the gradually-filling pool of lava at the base of your new lavafall. Lavaducts will eventually carry the lava throughout the city, but to make use of it immediately, Elves are loading it into large crucibles on wheels.

The crucibles are top-heavy and pushed by hand. Unfortunately, the crucibles become very difficult to steer at high speeds, and so it can be hard to go in a straight line for very long.

To get Desert Island the machine parts it needs as soon as possible, you'll need to find the best way to get the crucible from the lava pool to the machine parts factory. To do this, you need to minimize heat loss while choosing a route that doesn't require the crucible to go in a straight line for too long.

Fortunately, the Elves here have a map (your puzzle input) that uses traffic patterns, ambient temperature, and hundreds of other parameters to calculate exactly how much heat loss can be expected for a crucible entering any particular city block.

For example:

2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
Each city block is marked by a single digit that represents the amount of heat loss if the crucible enters that block. The starting point, the lava pool, is the top-left city block; the destination, the machine parts factory, is the bottom-right city block. (Because you already start in the top-left block, you don't incur that block's heat loss unless you leave that block and then return to it.)

Because it is difficult to keep the top-heavy crucible going in a straight line for very long, it can move at most three blocks in a single direction before it must turn 90 degrees left or right. The crucible also can't reverse direction; after entering each city block, it may only turn left, continue straight, or turn right.

One way to minimize heat loss is this path:

2>>34^>>>1323
32v>>>35v5623
32552456v>>54
3446585845v52
4546657867v>6
14385987984v4
44578769877v6
36378779796v>
465496798688v
456467998645v
12246868655<v
25465488877v5
43226746555v>
This path never moves more than three consecutive blocks in the same direction and incurs a heat loss of only 102.

Directing the crucible from the lava pool to the machine parts factory, but not moving more than three consecutive blocks in the same direction, what is the least heat loss it can incur?
'''
import datetime
import queue

with open('input/17.txt', 'r') as f:
# with open('input/17-small.txt', 'r') as f:
    lines = f.readlines()
lines = [l.rstrip() for l in lines]
lines = [l for l in lines if l]

field = [[int(c) for c in l] for l in lines]
visited = [[set() for c in l] for l in lines]

# q = []
q = queue.PriorityQueue()

def is_visited(x, y, dir, prev, prev_path):
    '''
    :param x: this cell to test
    :param y:
    :param dir: in the cell x,y
    :param prev: before the cell x,y
    :return:
    '''
    # k = [dir]
    # k.extend(prev)
    # s = str_from_dirs(k)
    # if s in visited[y][x]:
    #     return True
    # else:
    #     return False

    res = False
    for i in prev_path:
        px, py, pdir, pcost = i
        if px == x and py == y:
            if pdir == dir or px == -1:
                res = True
                break
    return res

def str_from_dirs(dirs):
    s = ''
    for d in dirs:
        s += str(d)
    return s

def dirs_from_str(s):
    dirs = []
    for c in s:
        i = int(c)
        dirs.append(i)
    return dirs

def set_visited(x, y, dir, prev):
    k = [dir]
    k.extend(prev)
    s = str_from_dirs(k)
    visited[y][x].add(s)

def is_fourth(dir, prev):
    res = True
    if len(prev) < 1:
        res = False
    else:
        same_dir_count = 0
        for p in prev:
            if p != dir:
                res = False
            else:
                same_dir_count += 1
        if same_dir_count < 3:
            res = False
    return res

min_result = [1111111111111, [], []]

def print_result():
    print_lines = [[c for c in l] for l in lines]
    for n in min_result[2]:
        x, y, dir, cost = n
        ch = '^<v>'
        c = ch[dir]
        if dir < 0:
            c = 'S'
        print_lines[y][x] = c
    for l in print_lines:
        print(''.join(l))

def enq(x, y, dir, prev, prev_cost, prev_path):
    if not is_visited(x, y, dir, prev, prev_path):
        cost = prev_cost + field[y][x]
        path = [(x, y, dir, cost)]
        path.extend(prev_path)
        if x == len(field[0]) - 1 and y == len(field) - 1:
            if cost < min_result[0]:
                min_result[0] = cost
                d = [dir]
                d.extend(prev)
                min_result[1] = d
                min_result[2] = path
                s = ''.join([str(i) for i in d])
                dt = datetime.datetime.now()
                qsize = q.qsize()
                print(f'{dt} New min result: min={min_result[0]} dir={s} qsize={qsize} path={path}')
                print_result()
        elif not is_fourth(dir, prev):
            # set_visited(x, y, dir, prev)
            # q.append( (x, y, dir, prev, prev_cost, path) )
            if cost < min_result[0]:
                proximity = len(field[0]) - x + len(field) - y # A*
                # a = proximity + prev_cost
                a = proximity
                q.put(item=(a, prev_cost, x, y, dir, prev, path))

# up, left, down, right
#  0    1    2    3
def new_tiles(dir, x, y):
    tt = []
    if dir == 3:
        if x + 1 < len(field[0]):
            tt.append((x + 1, y, 3))
        if y - 1 > -1:
            tt.append((x, y - 1, 0))
        if y + 1 < len(field):
            tt.append((x, y + 1, 2))
    elif dir == 2:
        if y + 1 < len(field):
            tt.append((x, y + 1, 2))
        if x - 1 > -1:
            tt.append((x - 1, y, 1))
        if x + 1 < len(field[0]):
            tt.append((x + 1, y, 3))
    elif dir == 1:
        if x - 1 > -1:
            tt.append((x - 1, y, 1))
        if y - 1 > -1:
            tt.append((x, y - 1, 0))
        if y + 1 < len(field):
            tt.append((x, y + 1, 2))
    else: # 0
        if y - 1 > -1:
            tt.append((x, y - 1, 0))
        if x - 1 > -1:
            tt.append((x - 1, y, 1))
        if x + 1 < len(field[0]):
            tt.append((x + 1, y, 3))
    return tt

# starting from top left, enqueue neighbours
set_visited(0, 0, 3, [])
enq(1, 0, 3, [3], field[0][0], [(0, 0, -1, field[0][0])])

set_visited(0, 0, 2, [])
enq(0, 1, 2, [2], field[0][0], [(0, 0, -1, field[0][0])])

# while len(q) > 0:
while not q.empty():
    # curr = q.pop(0)
    curr = q.get()
    # proximity
    a, prev_cost, x, y, dir, prev, prev_path = curr # A*
    cost = prev_cost + field[y][x]
    # print(f'curr={curr} cost={cost}')
    tiles = new_tiles(dir, x, y)
    new_prev = [dir]
    new_prev.extend(prev[:2])
    for t in tiles:
        new_x, new_y, new_dir = t
        enq(new_x, new_y, new_dir, new_prev, cost, prev_path)

s = ''.join([str(i) for i in min_result[1]])
print(f'Final min result: min={min_result[0]} dir={s}  path={min_result[2]}')
print_result()
