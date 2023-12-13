#!/usr/bin/python3

# python3 -m doctest -v 13b.py

'''
--- Part Two ---

You resume walking through the valley of mirrors and - SMACK! - run directly into one. Hopefully nobody was watching, because that must have been pretty embarrassing.

Upon closer inspection, you discover that every mirror has exactly one smudge: exactly one . or # should be the opposite type.

In each pattern, you'll need to locate and fix the smudge that causes a different reflection line to be valid. (The old reflection line won't necessarily continue being valid after the smudge is fixed.)

Here's the above example again:

#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
The first pattern's smudge is in the top-left corner. If the top-left # were instead ., it would have a different, horizontal line of reflection:

1 ..##..##. 1
2 ..#.##.#. 2
3v##......#v3
4^##......#^4
5 ..#.##.#. 5
6 ..##..##. 6
7 #.#.##.#. 7
With the smudge in the top-left corner repaired, a new horizontal line of reflection between rows 3 and 4 now exists. Row 7 has no corresponding reflected row and can be ignored, but every other row matches exactly: row 1 matches row 6, row 2 matches row 5, and row 3 matches row 4.

In the second pattern, the smudge can be fixed by changing the fifth symbol on row 2 from . to #:

1v#...##..#v1
2^#...##..#^2
3 ..##..### 3
4 #####.##. 4
5 #####.##. 5
6 ..##..### 6
7 #....#..# 7
Now, the pattern has a different horizontal line of reflection between rows 1 and 2.

Summarize your notes as before, but instead use the new different reflection lines. In this example, the first pattern's new horizontal line has 3 rows above it and the second pattern's new horizontal line has 1 row above it, summarizing to the value 400.

In each pattern, fix the smudge and find the different line of reflection. What number do you get after summarizing the new reflection line in each pattern in your notes?
'''


with open('input/13.txt', 'r') as f:
# with open('input/13-small.txt', 'r') as f:
    lines = f.readlines()
lines = [l.rstrip() for l in lines]

fields = []
summs = []

def parse_input():
    field = []
    summ = []
    for l in lines:
        if l:
            su = 0
            for c in l:
                if c == '#':
                    su += 1
            summ.append(su)
            field.append(l)
        else:
            if len(field) > 0:
                fields.append(field)
                summs.append(summ)
                field = []
                summ = []

    if len(field) > 0:
        fields.append(field)
        summs.append(summ)
        field = []
        summ = []
parse_input()


def find_mirror(field, su):
    res = []

    for k in range(0, len(field) - 1):
        if su[k] == su[k + 1]: # a candidate
            match = True
            d = 0
            while match and k + 1 + d < len(field) and k - d > -1:
                if su[k - d] != su[k + 1 + d] or field[k - d] != field[k + 1 + d]:
                    match = False
                d += 1
            if match: # confirmed
                above = k + 1
                res.append(above)
    return res

def find_fix(field, su):
    res = []

    height = len(field)
    for k in range(0, height - 1):
        consider_lines = min(k + 1, height - (k + 1) )
        sum_diff = 0
        for d in range(consider_lines):
            su_above = su[k - d]
            su_below = su[k + 1 + d]
            sum_diff += abs(su_above - su_below)

        if sum_diff == 1: # a candidate
            smudges = 0
            for d in range(consider_lines):
                line_above = field[k - d]
                line_below = field[k + 1 + d]
                for j in range(len(line_above)):
                    if line_above[j] != line_below[j]:
                        smudges += 1

            if smudges == 1:
                above = k + 1
                res.append(above)
    return res

horizontal = []
vertical = []
not_found = []
for id_field in range(len(fields)):
    f = fields[id_field]
    h = find_fix(f, summs[id_field])
    horizontal.extend(h)

    su_vertical = []
    f_vertical = []
    width = len(f[0])
    height = len(f)
    for x in range(width):
        col_str_lst = [f[y][x] for y in range(height)]
        col_str = ''.join(col_str_lst)
        f_vertical.append(col_str)
        s1 = 0
        for c in col_str_lst:
            if c == '#':
                s1 += 1
        su_vertical.append(s1)

    v = find_fix(f_vertical, su_vertical)
    vertical.extend(v)

    if len(h) < 1 and len(v) < 1:
        not_found.append(id_field)

print(f'horizontal={horizontal}')
print(f'vertical={vertical}')
print(f'not_found={not_found}')

total = 0
for h in horizontal:
    total += h * 100
for v in vertical:
    total += v

print(f'total={total}')

