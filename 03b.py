#!/usr/bin/python3

# python3 -m doctest -v 03b.py

'''
--- Part Two ---

The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?
'''

import sys

with open('input/03.txt', 'r') as f:
# with open('input/03-small.txt', 'r') as f:
    lines = f.readlines()
lines = [l.rstrip() for l in lines]

digits ='1234567890'
def parse_nums(s):
    '''
    >>> parse_nums('467..114..')
    [('467', 0), ('114', 5)]

    >>> parse_nums('...*......')
    []

    >>> parse_nums('..35..633.')
    [('35', 2), ('633', 6)]

    >>> parse_nums('......755.')
    [('755', 6)]

    >>> parse_nums('.......755')
    [('755', 7)]

    '''
    num_pos = []
    num = ''
    pos = -1
    for k in range(len(s)):
        ch = s[k]
        if ch in digits:
            num += ch
            if pos < 0: pos = k
        else:
            if pos > -1: num_pos.append( (num, pos) )
            num = ''
            pos = -1

    if pos > -1: num_pos.append( (num, pos) )

    return num_pos


def is_attached(num_str, row, col, lines):
    width, height = len(lines[0]), len(lines)

    start_col, end_col = col - 1, col + len(num_str)
    if start_col < 0: start_col = 0
    if end_col > width - 1: end_col = width - 1

    start_row, end_row = row - 1, row + 1
    if start_row < 0: start_row = 0
    if end_row > height - 1: end_row = height - 1
    # print(f'{num_str}, x:[{start_col}, {end_col}], y:[{start_row}, {end_row}]')
    for x in range(start_col, end_col + 1):
        for y in range(start_row, end_row + 1):
            ch = lines[y][x]
            # print(f'{x}, {y}')
            if ch != '.' and digits.find(ch) < 0:
                return True

    return False

# print(is_attached('598', 9, 5, lines))
# sys.exit(11)

small = [\
        '467..114..',\
        '...*......',\
        '..35..633.',\
        '......#...',\
        '617*......',\
        '.....+.58.',\
        '..592.....',\
        '......755.',\
        '...$.*....',\
        '.664.598..'\
    ]
sum = 0
def star_coords(lines):
    '''
    >>> star_coords(small)
    [(3, 1), (3, 4), (5, 8)]
    '''

    width, height = len(lines[0]), len(lines)
    stars = []

    for row in range(height):
        line = lines[row]
        for col in range(width):
            if line[col] == '*':
                stars.append((col, row))
    return stars

def left_number(x, y, lines):
    '''
    >>> left_number(3, 4, small)
    617

    >>> left_number(4, 1, lines)
    0
    '''
    n = 0
    x1 = x - 1
    s = ''
    while x1 > -1 and digits.find(lines[y][x1]) > -1:
        s += lines[y][x1]
        x1 -= 1
    if s:
        n = int(s[::-1])
    return n

def right_number(x, y, lines):
    '''
    >>> right_number(3, 4, small)
    0

    >>> right_number(4, 1, lines)
    609
    '''
    n = 0
    x1 = x + 1
    s = ''
    while x1 < len(lines[0]) and digits.find(lines[y][x1]) > -1:
        s += lines[y][x1]
        x1 += 1
    if s:
        n = int(s)
    return n

def chonit(x, y, lines):
    '''
    >>> chonit(2, 0, small)
    467

    >>> chonit(1, 0, small)
    467

    >>> chonit(0, 0, small)
    467


    >>> chonit(2, 6, small)
    592

    >>> chonit(3, 6, small)
    592

    >>> chonit(4, 6, small)
    592


    >>> chonit(1, 9, small)
    664

    >>> chonit(2, 9, small)
    664

    >>> chonit(3, 9, small)
    664


    >>> chonit(7, 5, small)
    58

    >>> chonit(8, 5, small)
    58


    >>> chonit(140, 65, lines)
    296

    >>> chonit(139, 65, lines)
    296

    >>> chonit(138, 65, lines)
    296
    '''

    x1 = x - 1
    s = ''
    while x1 > -1 and digits.find(lines[y][x1]) > -1:
        s += lines[y][x1]
        x1 -= 1
    both = s[::-1]

    x1 = x
    s = ''
    while x1 < len(lines[0]) and digits.find(lines[y][x1]) > -1:
        s += lines[y][x1]
        x1 += 1
    both += s

    return int(both)

def power(star, lines):
    '''
    >>> power((3, 1), small)
    16345

    >>> power((3, 4), small)
    0

    >>> power((5, 8), small)
    451490
    '''
    res = 0
    nums = []
    x, y = star
    width, height = len(lines[0]), len(lines)

    # prev row
    if y > 0:
        y2 = y - 1
        if digits.find(lines[y2][x]) > -1:
            above = chonit(x, y2, lines)
            if above != 0: nums.append(above)
        else:
            above_left = left_number(x, y2, lines)
            above_right = right_number(x, y2, lines)
            if above_left != 0: nums.append(above_left)
            if above_right != 0: nums.append(above_right)

    # left, right
    if x > 0:
        left = left_number(x, y, lines)
        if left != 0: nums.append(left)

    if x < width - 1:
        right = right_number(x, y, lines)
        if right != 0: nums.append(right)

    # next row
    if y < height -1:
        y2 = y + 1
        if digits.find(lines[y2][x]) > -1:
            below = chonit(x, y2, lines)
            if below != 0: nums.append(below)
        else:
            below_left = left_number(x, y2, lines)
            below_right = right_number(x, y2, lines)
            if below_left != 0: nums.append(below_left)
            if below_right != 0: nums.append(below_right)

    if len(nums) == 2:
        res = nums[0] * nums[1]

    return res

coords = star_coords(lines)
for star in coords:
    sum += power(star, lines)

print(sum)




