#!/usr/bin/python3

# python3 -m doctest -v 11b.py

'''
The galaxies are much older (and thus much farther apart) than the researcher initially estimated.

Now, instead of the expansion you did before, make each empty row or column one million times larger. That is, each empty row should be replaced with 1000000 empty rows, and each empty column should be replaced with 1000000 empty columns.

(In the example above, if each empty row or column were merely 10 times larger, the sum of the shortest paths between every pair of galaxies would be 1030. If each empty row or column were merely 100 times larger, the sum of the shortest paths between every pair of galaxies would be 8410. However, your universe will need to expand far beyond these values.)

Starting with the same initial image, expand the universe according to these new rules, then find the length of the shortest path between every pair of galaxies. What is the sum of these lengths?
'''


with open('input/11.txt', 'r') as f:
# with open('input/11-small.txt', 'r') as f:
    lines = f.readlines()
lines = [l.rstrip() for l in lines]
lines = [l for l in lines if l]

empty_rows = []
empty_cols = []

for y, l in enumerate(lines):
    if l.find('#') < 0:
        empty_rows.append(y)

for x in range(len(lines[0])):
    objects = [lines[y][x] for y in range(len(lines)) if lines[y][x] != '.']
    if len(objects) < 1:
        empty_cols.append(x)

galaxies = []
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] != '.':
            galaxies.append((x, y))

# print(galaxies)
print(f'size of galaxies={len(galaxies)}')

# scale = 100
scale = 1_000_000
# d = []
total = 0
for k in range(len(galaxies) - 1):
    first = galaxies[k]
    for j in range(k + 1, len(galaxies)):
        second = galaxies[j]
        dx = abs(first[0] - second[0])
        dy = abs(first[1] - second[1])
        
        blank_x = 0
        if first[0] < second[0]:
            xx = [x for x in empty_cols if first[0] < x < second[0]]
            blank_x = len(xx)
        elif second[0] < first[0]:
            xx = [x for x in empty_cols if second[0] < x < first[0]]
            blank_x = len(xx)
            
        blank_y = 0
        if first[1] < second[1]:
            yy = [y for y in empty_rows if first[1] < y < second[1]]
            blank_y = len(yy)
        elif second[1] < first[1]:
            yy = [y for y in empty_rows if second[1] < y < first[1]]
            blank_y = len(yy)

        path = dx + dy + (blank_x + blank_y) * (scale - 1)
        # d.append(path)
        total += path
# print(d)
print(f'scale={scale}')
print(f'total={total}')

