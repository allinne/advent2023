#!/usr/bin/python3

# python3 -m doctest -v 01.py

with open('input/01.txt', 'r') as f:
    lines = f.readlines()

digits ='0123456789'
def find_first(s):
    '''
    >>> find_first('asdc')
    '0'

    >>> find_first('pqr3stu8vwx')
    '3'
    '''
    for ch in s:
        if ch in digits:
            return ch
    return '0'

def process_line(l):
    '''
    >>> process_line('asdc')
    0

    >>> process_line('treb7uchet')
    77
    >>> process_line('a1b2c3d4e5f')
    15
    '''
    first = find_first(l)
    last = find_first(reversed(l))
    return int(first + last)

nums = []
sum = 0
for l in lines:
    n = process_line(l)
    nums.append(n)
    sum += n

print(sum)




