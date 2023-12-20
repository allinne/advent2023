#!/usr/bin/python3

# python3 -m doctest -v 02.py

'''
As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue. Each time you play this game, he will hide a secret number of cubes of each color in the bag, and your goal is to figure out information about the number of cubes.
To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.

You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

For example, the record of a few games might look like this:
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once;
similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once.
If you add up the IDs of the games that would have been possible, you get 8.


Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
'''

import re

limits = (12, 13, 14) # RGB
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

sum = 0
for l in lines:
    game_id, rgb_list = parse_line(l)
    failed = False
    for r, g, b in rgb_list:
        if r > limits[0] or g > limits[1] or b > limits[2]:
            failed = True
            break
    if not failed: sum += game_id

print(sum)




