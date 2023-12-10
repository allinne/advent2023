#!/usr/bin/python3

# python3 -m doctest -v 07b.py

'''
--- Part Two ---

To make things a little more interesting, the Elf introduces one additional rule. Now, J cards are jokers - wildcards that can act like whatever card would make the hand the strongest type possible.

To balance this, J cards are now the weakest individual cards, weaker even than 2. The other cards stay in the same order: A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J.

J cards can pretend to be whatever card is best for the purpose of determining hand type; for example, QJJQ2 is now considered four of a kind. However, for the purpose of breaking ties between two hands of the same type, J is always treated as J, not the card it's pretending to be: JKKK2 is weaker than QQQQ2 because J is weaker than Q.

Now, the above example goes very differently:

32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
32T3K is still the only one pair; it doesn't contain any jokers, so its strength doesn't increase.
KK677 is now the only two pair, making it the second-weakest hand.
T55J5, KTJJT, and QQQJA are now all four of a kind! T55J5 gets rank 3, QQQJA gets rank 4, and KTJJT gets rank 5.
With the new joker rule, the total winnings in this example are 5905.

Using the new joker rule, find the rank of every hand in your set. What are the new total winnings?
'''

import functools

with open('input/07.txt', 'r') as f:
# with open('input/07-small.txt', 'r') as f:
    lines = f.readlines()
lines = [l.rstrip() for l in lines]

def parse(line):
    '''
    >>> parse('32T3K 765')
    ('32T3K', 765)

    >>> parse('T55J5 684')
    ('T55J5', 684)
    '''
    l = line.split(' ')
    m = int(l[1])
    return (l[0], m)

input = [parse(i) for i in lines]

def calculator(s):
    '''
    >>> calculator('32T3K')
    {'3': 2, '2': 1, 'T': 1, 'K': 1}

    >>> calculator('KK677')
    {'K': 2, '6': 1, '7': 2}
    '''
    mapped_str = {}
    for key in s:
        if key in mapped_str:
            mapped_str[key] += 1
        else:
            mapped_str[key] = 1
    return mapped_str


def determine(s):
    '''
    >>> determine('A23A4')
    2

    >>> determine('23456')
    1

    >>> determine('23432')
    3

    >>> determine('TTT98')
    4

    >>> determine('23332')
    5

    >>> determine('AA8AA')
    6

    >>> determine('AAAAA')
    7

    >>> determine('A')
    1

    >>> determine('AA')
    2

    >>> determine('AAA')
    4

    >>> determine('AAAA')
    6

    >>> determine('A33A')
    3

    >>> determine('K33A')
    2

    >>> determine('K53A')
    1

    1 High card
    2 One pair
    3 Two pair
    4 Three of a kind
    5 Full house
    6 Four of a kind
    7 Five of a kind
    '''

    r = 1
    counts = calculator(s)
    max_v = 0
    for k, v in counts.items():
        if v > max_v:
            max_v = v
    if max_v == 5:
        r = 7
    if max_v == 4:
        r = 6
    if max_v == 3:
        found_pair = False
        for k, v in counts.items():
            if v == 2:
                found_pair = True
        if found_pair:
            r = 5
        else:
            r = 4
    if max_v == 2:
        pair_count = 0
        for k, v in counts.items():
            if v == 2:
                pair_count += 1
        if pair_count == 2:
            r = 3
        else:
            r = 2

    return r

def determine1(s):
    cleaned = [c for c in s if c != 'J']
    j_count = 0
    for i in s:
        if i == 'J': j_count += 1
    rank = determine(cleaned)
    if j_count > 0:
        if j_count == 5: rank = 7
        elif j_count == 4: rank = 7
        elif j_count == 3:
            if rank == 2:
                rank = 7
            else:
                rank = 6
        elif j_count == 2:
            if rank == 4: rank = 7
            elif rank == 2: rank = 6
            else: rank = 4
        else: # 1
            if rank == 6: rank = 7
            elif rank == 4: rank = 6
            elif rank == 3: rank = 5
            elif rank == 2: rank = 4
            else: rank = 2
    return rank
cards = 'J23456789TQKA'

def comparator(l, r):
    '''
    >>> comparator(('32T3K', 1), ('T55J5', 1) )
    -1

    >>> comparator(('T55J5', 1), ('KK677', 1) )
    1

    >>> comparator(('KK677', 1), ('KTJJT', 1) )
    -1

    >>> comparator(('KTJJT', 1), ('QQQJA', 1) )
    1

    >>> comparator(('T55J5', 1), ('QQQJA', 1) )
    -1

    >>> comparator(('23456', 1), ('34567', 1) )
    -1

    >>> comparator(('23456', 1), ('23456', 1) )
    0
    '''

    rank_left = determine1(l[0])
    rank_right = determine1(r[0])

    if rank_left < rank_right: return -1
    elif rank_left > rank_right: return 1
    else:
        cards_left = [cards.find(ch) for ch in l[0]]
        cards_right = [cards.find(ch) for ch in r[0]]

        for k in range(len(cards_left)):
            if cards_left[k] < cards_right[k]: return -1
            if cards_left[k] > cards_right[k]: return 1

    return 0

ranked = sorted(input, key=functools.cmp_to_key(comparator) )
# print(ranked)

sum = 0
for i in range(len(ranked)):
    sum += ranked[i][1] * (i + 1)

print(sum)
