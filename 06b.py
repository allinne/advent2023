#!/usr/bin/python3

# python3 -m doctest -v 06b.py

'''
As the race is about to start, you realize the piece of paper with race times and record distances you got earlier actually just has very bad kerning. There's really only one race - ignore the spaces between the numbers on each line.

So, the example from before:

Time:      7  15   30
Distance:  9  40  200
...now instead means this:

Time:      71530
Distance:  940200
Now, you have to figure out how many ways there are to win this single race. In this example, the race lasts for 71530 milliseconds and the record distance you need to beat is 940200 millimeters. You could hold the button anywhere from 14 to 71516 milliseconds and beat the record, a total of 71503 ways!

How many ways can you beat the record in this one much longer race?
'''

import re
import math

with open('input/06.txt', 'r') as f:
# with open('input/06-small.txt', 'r') as f:
    lines = f.readlines()
lines = [l.rstrip() for l in lines]

# def parse_time(lines):
#     '''
#     >>> parse_time(['Time:      7  15   30'])
#     [7, 15, 30]
#     '''
#     res = re.findall(' (\d+)', lines[0])
#     times = []
#     if res:
#         times = [int(l) for l in res]
#
#     return times
#
# times = parse_time(lines)
# distances = [int(s) for s in lines[1].split(' ')[1:] if len(s) > 0]

def parse(s):
    '''
    >>> parse('Time:      7  15   30')
    71530

    >>> parse('Distance:  9  40  200')
    940200
    '''
    a = s.split(':')[1]
    str_v = [ch for ch in a if ch != ' ']
    return int(''.join(str_v))

time = parse(lines[0])
distance = parse(lines[1])

def swim_dist(push_time, full_time):
    '''
    >>> swim_dist(0, 7)
    0

    >>> swim_dist(1, 7)
    6

    >>> swim_dist(2, 7)
    10

    >>> swim_dist(3, 7)
    12

    >>> swim_dist(4, 7)
    12

    >>> swim_dist(5, 7)
    10

    >>> swim_dist(6, 7)
    6

    >>> swim_dist(7, 7)
    0
    '''
    v = 1 * push_time
    t = full_time - push_time
    return v * t

D = time * time - 4 * distance
sq = math.sqrt(D)

start_ceil = math.ceil((time - sq) / 2)
start_floor = math.floor((time - sq) / 2)
end_ceil = math.ceil((time + sq) / 2)
end_floor = math.floor((time + sq) / 2)

start = start_ceil
if swim_dist(start_floor, time) > distance:
    start = start_floor
if swim_dist(start, time) <= distance:
    start += 1

end = end_floor
if swim_dist(end_ceil, time) > distance:
    end = end_ceil

if swim_dist(end, time) <= distance:
    end -= 1

ways = end - start + 1
print(ways)
