#!/usr/bin/python3

# python3 -m doctest -v 12.py

'''
There's just one problem - many of the springs have fallen into disrepair, so they're not actually sure which springs would even be safe to use! Worse yet, their condition records of which springs are damaged (your puzzle input) are also damaged! You'll need to help them repair the damaged records.

In the giant field just outside, the springs are arranged into rows. For each row, the condition records show every spring and whether it is operational (.) or damaged (#). This is the part of the condition records that is itself damaged; for some springs, it is simply unknown (?) whether the spring is operational or damaged.

However, the engineer that produced the condition records also duplicated some of this information in a different format! After the list of springs for a given row, the size of each contiguous group of damaged springs is listed in the order those groups appear in the row. This list always accounts for every damaged spring, and each number is the entire size of its contiguous group (that is, groups are always separated by at least one operational spring: #### would always be 4, never 2,2).

So, condition records with no unknown spring conditions might look like this:

#.#.### 1,1,3
.#...#....###. 1,1,3
.#.###.#.###### 1,3,1,6
####.#...#... 4,1,1
#....######..#####. 1,6,5
.###.##....# 3,2,1
However, the condition records are partially damaged; some of the springs' conditions are actually unknown (?). For example:

???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
Equipped with this information, it is your job to figure out how many different arrangements of operational and broken springs fit the given criteria in each row.

In the first line (???.### 1,1,3), there is exactly one way separate groups of one, one, and three broken springs (in that order) can appear in that row: the first three unknown springs must be broken, then operational, then broken (#.#), making the whole row #.#.###.

The second line is more interesting: .??..??...?##. 1,1,3 could be a total of four different arrangements. The last ? must always be broken (to satisfy the final contiguous group of three broken springs), and each ?? must hide exactly one of the two broken springs. (Neither ?? could be both broken springs or they would form a single contiguous group of two; if that were true, the numbers afterward would have been 2,3 instead.) Since each ?? can either be #. or .#, there are four possible arrangements of springs.

The last line is actually consistent with ten different arrangements! Because the first number is 3, the first and second ? must both be . (if either were #, the first number would have to be 4 or higher). However, the remaining run of unknown spring conditions have many different ways they could hold groups of two and one broken springs:

?###???????? 3,2,1
.###.##.#...
.###.##..#..
.###.##...#.
.###.##....#
.###..##.#..
.###..##..#.
.###..##...#
.###...##.#.
.###...##..#
.###....##.#
In this example, the number of possible arrangements for each row is:

???.### 1,1,3 - 1 arrangement
.??..??...?##. 1,1,3 - 4 arrangements
?#?#?#?#?#?#?#? 1,3,1,6 - 1 arrangement
????.#...#... 4,1,1 - 1 arrangement
????.######..#####. 1,6,5 - 4 arrangements
?###???????? 3,2,1 - 10 arrangements
Adding all of the possible arrangement counts together produces a total of 21 arrangements.

For each row, count all of the different arrangements of operational and broken springs that meet the given criteria. What is the sum of those counts?
'''


# with open('input/12.txt', 'r') as f:
with open('input/12-small.txt', 'r') as f:
    lines = f.readlines()
lines = [l.rstrip() for l in lines]
lines = [l for l in lines if l]

def parse(s):
    '''
    >>> parse('???.### 1,1,3')
    ('???.###', [1, 1, 3])

    >>> parse('?#?#?#?#?#?#?#? 1,3,1,6')
    ('?#?#?#?#?#?#?#?', [1, 3, 1, 6])
    '''
    strs = s.split(' ')
    nums = [int(n) for n in strs[1].split(',') if n]
    return (strs[0], nums)

def permute_one(qq, n):
    '''
    >>> permute_one('', 1)
    []

    >>> permute_one('#', 1)
    ['#']

    >>> permute_one('?', 1)
    ['#']

    >>> permute_one('??', 1)
    ['#.', '.#']

    >>> permute_one('???', 1)
    ['#..', '.#.', '..#']

    >>> permute_one('????', 1)
    ['#...', '.#..', '..#.', '...#']

    >>> permute_one('??', 2)
    ['##']

    >>> permute_one('???', 2)
    ['##.', '.##']

    >>> permute_one('????', 2)
    ['##..', '.##.', '..##']
    '''

    l = []
    if not qq: return []

    dashes = ''
    for i in range(n): dashes += '#'

    if n >= len(qq):
        l = [dashes]
    else:
        remaining = ''
        for i in range(n, len(qq)): remaining += '.'   # must be at least one
        l.append(dashes + remaining)

        right = qq[1:]
        sub = permute_one(right, n)
        for su in sub:
            l.append('.' + su)

    return l

def permute_sparse_char(num_sparse, num_buckets):
    '''
    >>> permute_sparse_char(0, 0)
    []

    >>> permute_sparse_char(0, 1)
    [[0]]

    >>> permute_sparse_char(1, 1)
    [[1]]

    >>> permute_sparse_char(1, 2)
    [[1, 0], [0, 1]]

    >>> permute_sparse_char(2, 2)
    [[2, 0], [1, 1], [0, 2]]

    >>> permute_sparse_char(0, 2)
    [[0, 0]]

    >>> permute_sparse_char(0, 3)
    [[0, 0, 0]]
    '''
    if num_buckets < 1: return []
    if num_sparse < 1:
        a = [0 for i in range(num_buckets)]
        return [a]
    l = []


    return l

def permute_n(s, nums):
    '''
    >>> permute_n('?', [1])
    ['#']

    >>> permute_n('???', [1])
    ['#..', '.#.', '..#']

    >>> permute_n('??', [1])
    ['#.', '.#']

    >>> permute_n('???', [1, 1])
    ['#.#']

    >>> permute_n('????', [1, 1])
    ['#.#.', '.#.#', '#..#']

    >>> permute_n('?????', [1, 1])
    ['#.#..', '#..#.', '#...#', '.#.#.', '.#..#', '..#.#']

    '''
    l = []
    num_dots = len(nums) - 1
    if num_dots < 1:
        l = permute_one(s, nums[0]) #####
    else:
        must = num_dots
        for n in nums:
            must += n
        sparse_chars_num = len(s) - must
        dot_positions = []
        if sparse_chars_num < 1:
            traversed = 0
            for k in nums[:-1]:
                traversed += k
                dot_positions.append(traversed)
            res = ['#' for c in s]

            for pos in dot_positions:
                res[pos] = '.'
            l.append(''.join(res))
        else:
            pass #####
            # get permutations of sparse chars
            sparse_chars = permute_sparse_char()
        
            # call each part plus sparse char


    return l

def count(s, nums):
    # '''
    # >>> count('???.###', [1,1,3])
    # 1
    #
    # >>> count('.??..??...?##.', [1,1,3])
    # 4
    #
    # >>> count('?#?#?#?#?#?#?#?', [1,3,1,6])
    # 1
    #
    # >>> count('????.#...#...', [4,1,1])
    # 1
    #
    # >>> count('????.######..#####.', [1,6,5])
    # 4
    #
    # >>> count('?###????????', [3,2,1])
    # 10
    #
    # >>> count('WWW', [WWW])
    # 1
    #
    # >>> count('WWW', [WWW])
    # 1
    #
    # '''
    r = 1
    
    

    return r

# rrr = permute_one('?', 1)
# rrr = permute_one('??', 1)
# rrr = permute_one('???', 1)
rrr = permute_n('???', [1, 1])
print(rrr)

# sum = 0
# for row in lines:
#     s, n = parse(row)
#     sum += count(s, n)
#
# print(sum)




