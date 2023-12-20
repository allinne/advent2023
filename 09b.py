#!/usr/bin/python3

# python3 -m doctest -v 09b.py

'''
--- Part Two ---

Of course, it would be nice to have even more history included in your report. Surely it's safe to just extrapolate backwards as well, right?

For each history, repeat the process of finding differences until the sequence of differences is entirely zero. Then, rather than adding a zero to the end and filling in the next values of each previous sequence, you should instead add a zero to the beginning of your sequence of zeroes, then fill in new first values for each previous sequence.

In particular, here is what the third example history looks like when extrapolating back in time:

5  10  13  16  21  30  45
  5   3   3   5   9  15
   -2   0   2   4   6
      2   2   2   2
        0   0   0
Adding the new values on the left side of each sequence from bottom to top eventually reveals the new left-most history value: 5.

Doing this for the remaining example data above results in previous values of -3 for the first history and 0 for the second history. Adding all three new values together produces 2.

Analyze your OASIS report again, this time extrapolating the previous value for each history. What is the sum of these extrapolated values?
'''


with open('input/09.txt', 'r') as f:
# with open('input/09-small.txt', 'r') as f:
    lines = f.readlines()
lines = [l.rstrip() for l in lines]
lines = [l for l in lines if l]

def deep_diff(a, b):
    return b - a

def get_numbers(line):
    '''
    >>> get_numbers('1   3   6  10  15  21  28')
    [1, 3, 6, 10, 15, 21, 28]
    '''

    return [int(n) for n in line.split(' ') if n]

def vse_nuli(razniza):
    for r in razniza:
        if r != 0:
            return False
    return True

def iteraten(nums):
    razniza = []
    for n, n1 in zip(nums[:-1], nums[1:]):
        r = n1 - n
        razniza.append(r)
    if vse_nuli(razniza):
        r1 = [0]
        r1.extend(razniza)
        return r1
    else:
        snizu = iteraten(razniza)
        eshe_odin = razniza[0] - snizu[0]
        r1 = [eshe_odin]
        r1.extend(razniza)
        return r1

sum = 0
for l in lines:
    nums = get_numbers(l)
    razniza = iteraten(nums)
    posledniy = nums[0] - razniza[0]
    sum += posledniy

print(f'sum={sum}')
