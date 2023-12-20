#!/usr/bin/python3

# python3 -m doctest -v 01b.py

with open('input/01.txt', 'r') as f:
    lines = f.readlines()

words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
words_reversed = [w[::-1] for w in words]
digits ='1234567890'

def find_digit(s):
    '''
    >>> find_digit('asdc')
    ('0', -1)

    >>> find_digit('pqr3stu8vwx')
    ('3', 3)
    '''
    for i in range(len(s)):
        ch = s[i]
        if ch in digits:
            return (ch, i)
    return ('0', -1)

def find_word(s, vcblr):
    '''
    >>> find_word('two1nine', words)
    ('2', 0)

    >>> find_word('eightwothree', words)
    ('8', 0)

    >>> find_word('abcone2threexyz', words)
    ('1', 3)

    >>> find_word('xtwone3four', words)
    ('2', 1)

    >>> find_word('4nineeightseven2', words)
    ('9', 1)

    >>> find_word('zoneight234', words)
    ('1', 1)

    >>> find_word('7pqrstsixteen', words)
    ('6', 6)

    >>> find_word('treb7uchet', words)
    ('0', -1)


    >>> find_word('two1nine'[::-1], words_reversed)
    ('9', 0)

    >>> find_word('eightwothree'[::-1], words_reversed)
    ('3', 0)

    >>> find_word('abcone2threexyz'[::-1], words_reversed)
    ('3', 3)

    >>> find_word('xtwone3four'[::-1], words_reversed)
    ('4', 0)

    >>> find_word('4nineeightseven2'[::-1], words_reversed)
    ('7', 1)

    >>> find_word('zoneight234'[::-1], words_reversed)
    ('8', 3)

    >>> find_word('7pqrstsixteen'[::-1], words_reversed)
    ('6', 4)


    >>> find_word('treb7uchet'[::-1], words_reversed)
    ('0', -1)

    '''
    ix_min = -1
    ch = '0'
    for i in range(len(vcblr)):
        w = vcblr[i]
        ix = s.find(w)
        if ix > -1:
            if ch == '0':
                ix_min = ix
                ch = digits[i]
            else:
                if ix < ix_min:
                    ix_min = ix
                    ch = digits[i]
    return (ch, ix_min)

def find_first(s, vcblr):
    '''
    >>> find_first('asdc', words)
    '0'

    >>> find_first('pqr3stu8vwx', words)
    '3'



    >>> find_first('two1nine', words)
    '2'

    >>> find_first('eightwothree', words)
    '8'

    >>> find_first('abcone2threexyz', words)
    '1'

    >>> find_first('xtwone3four', words)
    '2'

    >>> find_first('4nineeightseven2', words)
    '4'

    >>> find_first('zoneight234', words)
    '1'

    >>> find_first('7pqrstsixteen', words)
    '7'
    
    
    

    >>> find_first('two1nine'[::-1], words_reversed)
    '9'

    >>> find_first('eightwothree'[::-1], words_reversed)
    '3'

    >>> find_first('abcone2threexyz'[::-1], words_reversed)
    '3'

    >>> find_first('xtwone3four'[::-1], words_reversed)
    '4'

    >>> find_first('4nineeightseven2'[::-1], words_reversed)
    '2'

    >>> find_first('zoneight234'[::-1], words_reversed)
    '4'

    >>> find_first('7pqrstsixteen'[::-1], words_reversed)
    '6'
    '''

    ch_digit, ix_digit = find_digit(s)
    ch_word, ix_word = find_word(s, vcblr)
    if ix_digit > -1 and ix_word > -1:
        if ix_digit < ix_word: return ch_digit
        else: return ch_word
    else: # either not found
        if ix_digit > -1: return ch_digit
        else: return ch_word

def process_line(l):
    '''
    >>> process_line('asdc')
    0

    >>> process_line('treb7uchet')
    77

    >>> process_line('a1b2c3d4e5f')
    15

    >>> process_line('two1nine')
    29

    >>> process_line('eightwothree')
    83

    >>> process_line('abcone2threexyz')
    13

    >>> process_line('xtwone3four')
    24

    >>> process_line('4nineeightseven2')
    42

    >>> process_line('zoneight234')
    14

    >>> process_line('7pqrstsixteen')
    76
    '''
    first = find_first(l, words)
    last = find_first(l[::-1], words_reversed)
    return int(first + last)

nums = []
sum = 0
# lines = ['two1nine']
for l in lines:
    n = process_line(l)
    nums.append(n)
    sum += n

print(sum)




