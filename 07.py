#!/usr/bin/python3

# python3 -m doctest -v 07.py

'''
--- Day 7: Camel Cards ---

Your all-expenses-paid trip turns out to be a one-way, five-minute ride in an airship. (At least it's a cool airship!) It drops you off at the edge of a vast desert and descends back to Island Island.

"Did you bring the parts?"

You turn around to see an Elf completely covered in white clothing, wearing goggles, and riding a large camel.

"Did you bring the parts?" she asks again, louder this time. You aren't sure what parts she's looking for; you're here to figure out why the sand stopped.

"The parts! For the sand, yes! Come with me; I will show you." She beckons you onto the camel.

After riding a bit across the sands of Desert Island, you can see what look like very large rocks covering half of the horizon. The Elf explains that the rocks are all along the part of Desert Island that is directly above Island Island, making it hard to even get there. Normally, they use big machines to move the rocks and filter the sand, but the machines have broken down because Desert Island recently stopped receiving the parts they need to fix the machines.

You've already assumed it'll be your job to figure out why the parts stopped when she asks if you can help. You agree automatically.

Because the journey will take a few days, she offers to teach you the game of Camel Cards. Camel Cards is sort of similar to poker except it's designed to be easier to play while riding a camel.

In Camel Cards, you get a list of hands, and your goal is to order them based on the strength of each hand. A hand consists of five cards labeled one of A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2. The relative strength of each card follows this order, where A is the highest and 2 is the lowest.

Every hand is exactly one type. From strongest to weakest, they are:

Five of a kind, where all five cards have the same label: AAAAA
Four of a kind, where four cards have the same label and one card has a different label: AA8AA
Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
High card, where all cards' labels are distinct: 23456
Hands are primarily ordered based on type; for example, every full house is stronger than any three of a kind.

If two hands have the same type, a second ordering rule takes effect. Start by comparing the first card in each hand. If these cards are different, the hand with the stronger first card is considered stronger. If the first card in each hand have the same label, however, then move on to considering the second card in each hand. If they differ, the hand with the higher second card wins; otherwise, continue with the third card in each hand, then the fourth, then the fifth.

So, 33332 and 2AAAA are both four of a kind hands, but 33332 is stronger because its first card is stronger. Similarly, 77888 and 77788 are both a full house, but 77888 is stronger because its third card is stronger (and both hands have the same first and second card).

To play Camel Cards, you are given a list of hands and their corresponding bid (your puzzle input). For example:

32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
This example shows five hands; each hand is followed by its bid amount. Each hand wins an amount equal to its bid multiplied by its rank, where the weakest hand gets rank 1, the second-weakest hand gets rank 2, and so on up to the strongest hand. Because there are five hands in this example, the strongest hand will have rank 5 and its bid will be multiplied by 5.

So, the first step is to put the hands in order of strength:

32T3K is the only one pair and the other hands are all a stronger type, so it gets rank 1.
KK677 and KTJJT are both two pair. Their first cards both have the same label, but the second card of KK677 is stronger (K vs T), so KTJJT gets rank 2 and KK677 gets rank 3.
T55J5 and QQQJA are both three of a kind. QQQJA has a stronger first card, so it gets rank 5 and T55J5 gets rank 4.
Now, you can determine the total winnings of this set of hands by adding up the result of multiplying each hand's bid with its rank (765 * 1 + 220 * 2 + 28 * 3 + 684 * 4 + 483 * 5). So the total winnings in this example are 6440.

Find the rank of every hand in your set. What are the total winnings?
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
        if len(counts) == 2:
            r = 5
        else:
            r = 4
    if max_v == 2:
        if len(counts) == 3:
            r = 3
        else:
            r = 2

    return r

cards = '23456789TJQKA'

def comparator(l, r):
    '''
    >>> comparator(('32T3K', 1), ('T55J5', 1) )
    -1

    >>> comparator(('T55J5', 1), ('KK677', 1) )
    1

    >>> comparator(('KK677', 1), ('KTJJT', 1) )
    1

    >>> comparator(('KTJJT', 1), ('QQQJA', 1) )
    -1

    >>> comparator(('T55J5', 1), ('QQQJA', 1) )
    -1

    >>> comparator(('23456', 1), ('34567', 1) )
    -1

    >>> comparator(('23456', 1), ('23456', 1) )
    0
    '''

    rank_left = determine(l[0])
    rank_right = determine(r[0])

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
