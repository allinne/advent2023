#!/usr/bin/python3

# python3 -m doctest -v 03.py

'''
You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

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
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?
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

sum = 0
for row in range(len(lines)):
    line = lines[row]
    num_col = parse_nums(line) # [('467', 0), ('114', 5)]
    for num_str, col in num_col:
        if is_attached(num_str, row, col, lines):
            sum += int(num_str)

print(sum)




