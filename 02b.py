#!/usr/bin/python3

# python3 -m doctest -v 02.py

'''
As you continue your walk, the Elf poses a second question: in each game you played, what is the fewest number of cubes of each color that could have been in the bag to make the game possible?

Again consider the example games from earlier:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If any color had even one fewer cube, the game would have been impossible.
Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
Game 4 required at least 14 red, 3 green, and 15 blue cubes.
Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.
The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286.

For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?

'''

import re

with open('input/02.txt', 'r') as f:
# with open('input/02-small.txt', 'r') as f:
    lines = f.readlines()

def search_color(s, color):
    '''
    6 blue, 1 green, 3 red
    >>> search_color('1 red', 'red')
    1

    >>> search_color('1 red', 'blue')
    0

    >>> search_color('5 red', 'red')
    5

    >>> search_color('9 green, 2 red, 1 blue', 'red')
    2

    >>> search_color('9 green, 2 red, 1 blue', 'blue')
    1

    >>> search_color('9 green, 2 red, 1 blue', 'green')
    9
    '''
    n = 0
    res = re.search('(\d+) ' + color, s)
    if res: n = int(res.group(1))

    return n

def parse_round(s):
    r = search_color(s, 'red')
    g = search_color(s, 'green')
    b = search_color(s, 'blue')
    return r, g, b

def parse_line(s):
    '''
    >>> parse_line('Game 21: 1 red; 4 red; 2 red, 2 green, 1 blue')
    (21, [(1, 0, 0), (4, 0, 0), (2, 2, 1)])

    >>> parse_line('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green')
    (1, [(4, 0, 3), (1, 2, 6), (0, 2, 0)])

    >>> parse_line('Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue')
    (2, [(0, 2, 1), (1, 3, 4), (0, 1, 1)])

    >>> parse_line('Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red')
    (3, [(20, 8, 6), (4, 13, 5), (1, 5, 0)])

    >>> parse_line('Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red')
    (4, [(3, 1, 6), (6, 3, 0), (14, 3, 15)])

    >>> parse_line('Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green')
    (5, [(6, 3, 1), (1, 2, 2)])
    '''

    res_id = re.search('Game (\d+):', s)
    id = int(res_id.group(1))

    right = s.split(':')[1]
    games = right.split(';')

    rgbs = []
    for one_game in games:
        rgbs.append(parse_round(one_game))

    return (id, rgbs)

def power(rgb_list):
    maxRGB = [0, 0, 0]

    for r, g, b in rgb_list:
        if r > maxRGB[0]:
            maxRGB[0] = r
        if g > maxRGB[1]:
            maxRGB[1] = g
        if b > maxRGB[2]:
            maxRGB[2] = b

    return maxRGB[0] * maxRGB[1] * maxRGB[2]

sum = 0
for l in lines:
    _, rgb_list = parse_line(l)
    sum += power(rgb_list)

print(sum)




