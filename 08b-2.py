#!/usr/bin/python3

# python3 -m doctest -v 08b-2.py

'''
--- Part Two ---

The sandstorm is upon you and you aren't any closer to escaping the wasteland. You had the camel follow the instructions, but you've barely left your starting position. It's going to take significantly more steps to escape!

What if the map isn't for people - what if the map is for ghosts? Are ghosts even bound by the laws of spacetime? Only one way to find out.

After examining the maps a bit longer, your attention is drawn to a curious fact: the number of nodes with names ending in A is equal to the number ending in Z! If you were a ghost, you'd probably just start at every node that ends with A and follow all of the paths at the same time until they all simultaneously end up at nodes that end with Z.

For example:

LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
Here, there are two starting nodes, 11A and 22A (because they both end with A). As you follow each left/right instruction, use that instruction to simultaneously navigate away from both nodes you're currently on. Repeat this process until all of the nodes you're currently on end with Z. (If only some of the nodes you're on end with Z, they act like any other node and you continue as normal.) In this example, you would proceed as follows:

Step 0: You are at 11A and 22A.
Step 1: You choose all of the left paths, leading you to 11B and 22B.
Step 2: You choose all of the right paths, leading you to 11Z and 22C.
Step 3: You choose all of the left paths, leading you to 11B and 22Z.
Step 4: You choose all of the right paths, leading you to 11Z and 22B.
Step 5: You choose all of the left paths, leading you to 11B and 22C.
Step 6: You choose all of the right paths, leading you to 11Z and 22Z.
So, in this example, you end up entirely on nodes that end in Z after 6 steps.

Simultaneously start on every node that ends with A. How many steps does it take before you're only on nodes that end with Z?
'''
import sys

with open('input/08.txt', 'r') as f:
# with open('input/08-small-3.txt', 'r') as f:
    lines = f.readlines()
lines = [l.rstrip() for l in lines]
lines = [l for l in lines if l]

instructions = lines[0]
graph = dict()

for l in lines[1:]:
    eq = l.split('=')
    key = eq[0].strip()
    right = eq[1].strip().rstrip(')').lstrip('(')
    pair = right.split(',')
    to_left = pair[0].strip()
    to_right = pair[1].strip()
    graph[key] = (to_left, to_right)

def is_finish(nodes):
    r = True
    for n in nodes:
        if n[-1] != 'Z':
            r = False
    return r

cc = [k for k in graph if k[-1] == 'A']
print(f'cc={cc}')

def n_counts(cc, limit):
    z_at_count = []
    count = 0
    IP = 0
    if is_finish(cc):
            z_at_count.append(count)

    while count < limit:
        if is_finish(cc):
            z_at_count.append(count)

        new_cc = []
        for c in cc:
            if c == 'XXX':
                print('XXX!')
                sys.exit(22)
            if instructions[IP] == 'L':
                nc = graph[c][0]
            else:
                nc = graph[c][1]
            new_cc.append(nc)
        cc = new_cc
        IP += 1
        if IP > len(instructions) - 1:
            IP = 0
        count += 1
    if is_finish(cc):
            z_at_count.append(count)

    return z_at_count


lmt = 100_000
visits_at_count = []
for i, c in enumerate(cc):
    v = n_counts([c], lmt)
    visits_at_count.append(v)
    print(f'start id={i} c={c} visited at count={lmt} v={v}')

# print(count)
print('end')

# first Z for starts:
# 19637 = 269 73
# 18023 = 269 67
# 21251 = 269 79
# 16409 = 269 61
# 11567 = 269 43
# 14257 = 269 53

m = 43 * 53 * 61 * 67 * 73 * 79 * 269
print(f'm={m}')

