#!/usr/bin/python3

# python3 -m doctest -v 14b.py

'''
--- Part Two ---

The parabolic reflector dish deforms, but not in a way that focuses the beam. To do that, you'll need to move the rocks to the edges of the platform. Fortunately, a button on the side of the control panel labeled "spin cycle" attempts to do just that!

Each cycle tilts the platform four times so that the rounded rocks roll north, then west, then south, then east. After each tilt, the rounded rocks roll as far as they can before the platform tilts in the next direction. After one cycle, the platform will have finished rolling the rounded rocks in those four directions in that order.

Here's what happens in the example above after each of the first few cycles:

After 1 cycle:
.....#....
....#...O#
...OO##...
.OO#......
.....OOO#.
.O#...O#.#
....O#....
......OOOO
#...O###..
#..OO#....

After 2 cycles:
.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#..OO###..
#.OOO#...O

After 3 cycles:
.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#...O###.O
#.OOO#...O
This process should work if you leave it running long enough, but you're still worried about the north support beams. To make sure they'll survive for a while, you need to calculate the total load on the north support beams after 1000000000 cycles.

In the above example, after 1000000000 cycles, the total load on the north support beams is 64.

Run the spin cycle for 1000000000 cycles. Afterward, what is the total load on the north support beams?
'''

import datetime, sys

with open('input/14.txt', 'r') as f:
# with open('input/14-small.txt', 'r') as f:
    lines = f.readlines()
lines = [l.rstrip() for l in lines]
lines = [l for l in lines if l]

def to_digit(ch):
    if ch == '#': return 2
    elif ch == 'O': return 1
    return 0

def to_ch(digit):
    if digit == 2: return '#'
    elif digit == 1: return 'O'
    return '.'

digital = [[to_digit(ch) for ch in l] for l in lines]

width = len(lines[0])
height = len(lines)

def tilt(dir):
    start = end = -1
    round = 0

    if dir == 3: # east
        for y in range(0, len(digital)):
            start = end = -1
            round = 0
            for x in range(0, len(digital[y])):
                if digital[y][x] == 2: # a rock:
                    if round > 0: # finalize interval if any
                        # shift round
                        for j in range(start, x):
                            digital[y][j] = 0
                        for j in range(round):
                            digital[y][end - j] = 1
                        round = 0
                    start = end = -1
                elif digital[y][x] == 1:
                    round += 1
                    if start < 0:
                        start = x
                    end = x
                else:
                    if start < 0:
                        start = x
                    end = x

            if round > 0: # finalize interval if any
                # shift round
                for j in range(start, end + 1):
                    digital[y][j] = 0
                for j in range(round):
                    digital[y][end - j] = 1
    elif dir == 1: # west
        for y in range(0, len(digital)):
            start = end = -1
            round = 0
            for x in range(len(digital[y]) - 1, -1, -1):
                if digital[y][x] == 2: # a rock:
                    if round > 0: # finalize interval if any
                        # shift round
                        for j in range(start, x, -1):
                            digital[y][j] = 0
                        for j in range(round):
                            digital[y][end + j] = 1
                        round = 0
                    start = end = -1
                elif digital[y][x] == 1:
                    round += 1
                    if start < 0:
                        start = x
                    end = x
                else:
                    if start < 0:
                        start = x
                    end = x

            if round > 0: # finalize interval if any
                # shift round
                for j in range(start, end - 1, -1):
                    digital[y][j] = 0
                for j in range(round):
                    digital[y][end + j] = 1
    elif dir == 2: # south
        for x in range(0, len(digital[0])):
            start = end = -1
            round = 0
            for y in range(0, len(digital)):
                if digital[y][x] == 2: # a rock:
                    if round > 0: # finalize interval if any
                        # shift round
                        for j in range(start, y):
                            digital[j][x] = 0
                        for j in range(round):
                            digital[end - j][x] = 1
                        round = 0
                    start = end = -1
                elif digital[y][x] == 1:
                    round += 1
                    if start < 0:
                        start = y
                    end = y
                else:
                    if start < 0:
                        start = y
                    end = y

            if round > 0: # finalize interval if any
                # shift round
                for j in range(start, end + 1):
                    digital[j][x] = 0
                for j in range(round):
                    digital[end - j][x] = 1
    elif dir == 0: # north
        for x in range(0, len(digital[0])):
            start = end = -1
            round = 0
            for y in range(len(digital) - 1, -1, -1):
                if digital[y][x] == 2: # a rock:
                    if round > 0: # finalize interval if any
                        # shift round
                        for j in range(start, y, -1):
                            digital[j][x] = 0
                        for j in range(round):
                            digital[end + j][x] = 1
                        round = 0
                    start = end = -1
                elif digital[y][x] == 1:
                    round += 1
                    if start < 0:
                        start = y
                    end = y
                else:
                    if start < 0:
                        start = y
                    end = y

            if round > 0: # finalize interval if any
                # shift round
                for j in range(start, end - 1, -1):
                    digital[j][x] = 0
                for j in range(round):
                    digital[end + j][x] = 1
    else:
        print('ERR!')
        sys.exit(22)


# cycle: north, then west, then south, then east
def cycle():
    tilt(0)
    tilt(1)
    tilt(2)
    tilt(3)

def calc_north():
    total = 0
    for x in range(0, len(digital[0])):
        for w in range(1, height + 1):
            y = height - w
            if digital[y][x] == 1: # a round
                total += w
    # print(total)
    return total

inform = 1_000_000
# num_cycles = 1_000_000_000
# num_cycles = 10_000_000
num_cycles = 1

north = []
north.append(calc_north())

i = 0
started = datetime.datetime.now()
while i < num_cycles:
    print(f'{i} {calc_north()}')
    cycle()

    # n = calc_north()
    # north.append(n)
    # if (i + 1) % 10000 == 0:
    #     print(f'result after {i + 1} cycles: total={n}')

    # if i % inform == 0:
    #     n = datetime.datetime.now()
    #     print(f'{n} i={int(i / inform)}M elapsed {n - started}')
    i += 1
print(f'{i} {calc_north()}')

small_cycle = [69, 65, 64, 65, 63, 68, 69]
small_cycle_start = 4 # 4, 5, 6, 7, 8, 9, 10
def small_north(n):
    ix = (n - small_cycle_start) % len(small_cycle)
    return small_cycle[ix]

big_cycle = [83473, 83484, 83491, 83507, 83516, 83516, 83502, 83489, 83488, 83482, 83477,]
big_cycle_start = 148
def big_north(n):
    ix = (n - big_cycle_start) % len(big_cycle)
    return big_cycle[ix]

print('========')
for i in range(148, 172):
    print(f'{i} {big_north(i)}')
print('========')
print(f'north(1000000000)={big_north(1000000000)}')
print('========')



# print('========')
# for i in range(4, 41):
#     print(f'{i} {small_north(i)}')
# print('========')
# print(f'north(1000000000)={small_north(1000000000)}')
# print('========')

def print_m(digital):
    text = [[to_ch(digit) for digit in l] for l in digital]
    for l in text:
        print(''.join(l))
# print_m(digital)

print(f'north={north}')

total = calc_north()
print(f'result after {i} cycles: total={total}')
finished = datetime.datetime.now()
print(f'elapsed {finished - started}')

