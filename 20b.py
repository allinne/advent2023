#!/usr/bin/python3

# python3 -m doctest -v 20b.py

'''
--- Part Two ---

The final machine responsible for moving the sand down to Island Island has a module attached named rx. The machine turns on when a single low pulse is sent to rx.

Reset all modules to their default states. Waiting for all pulses to be fully handled after each button press, what is the fewest number of button presses required to deliver a single low pulse to the module named rx?
'''
import datetime
import sys

with open('input/20.txt', 'r') as f:
# with open('input/20-small.txt', 'r') as f:
# with open('input/20-small-2.txt', 'r') as f:
    lines = f.readlines()
lines = [l.rstrip() for l in lines]
lines = [l for l in lines if l]

machine = {}
conjunction = []
for l in lines:
    p = l.split('->')
    n = p[0].strip()
    outs = [s.strip() for s in p[1].split(',')]
    if n == 'broadcaster':
        machine['broadcaster'] = ['broadcaster', outs] # to have outs at [1]
    else:
        ch = n[0]
        key = n[1:]
        if ch == '%': # flip-flop
            machine[key] = [False, outs] # they are initially off
        else: # conj
            if ch != '&': # if not conj: err
                print('Err!')
                sys.exit(11)
            ins = dict()
            machine[key] = [ins, outs] # ins to be filled later
            conjunction.append(key)

conjunction_set = set(conjunction)
for name, instuction in machine.items():
    for k in instuction[1]:
        if k in conjunction_set: # if dst node k is a conjunction node, add input to the conj node
            # they initially default to remembering a low pulse for each input
            machine[k][0][name] = 0

# conj node controlling rx
inputs_lvl1 = list(machine['mg'][0])
count_to_first_1 = { i:0 for i in inputs_lvl1}

counts =[0, 0] # low, high
def press(pressed):
    res = False
    q = [('broadcaster', 0, 'button')] # 0: low, 1:high
    while len(q) > 0:
        to, signal, src = q.pop(0)
        counts[signal] += 1
        # ss = '-low' if signal == 0 else '-high'
        # print(f'{src} {ss}-> {to}')

        # if signal == 1:
        #     if to in count_to_first_1:
        #         if count_to_first_1[to] < 1:
        #             count_to_first_1[to] = pressed
        #         print(count_to_first_1)

        if to == 'broadcaster':
            for dst in machine[to][1]:
                q.append((dst, signal, to))
        elif to == 'rx':
            if signal == 0:
                res = True
                break
        elif to == 'output':
            pass # printed
        elif to in conjunction_set:
            machine[to][0][src] = signal
            new_signal = 1
            # if it remembers high pulses for all inputs, it sends a low pulse
            all_high = True
            for k, i in machine[to][0].items():
                if i != 1:
                    all_high = False
            if all_high:
                new_signal = 0
            for dst in machine[to][1]:
                q.append((dst, new_signal, to))
        else: # % flip-flop
            if signal == 0: # low, ignore high
                old = machine[to][0]
                machine[to][0] = not old
                new_signal = 1 # was off: send high
                if old: # was on
                    new_signal = 0
                for dst in machine[to][1]:
                    q.append((dst, new_signal, to))
            # ignore high
    return res

# pressed = 0
# # dt = datetime.datetime.now()
# # print(f'{dt} pressed={pressed}')
# chunk = 1_000_000
# found = False
# while not found:
#     if pressed % chunk == 0:
#         dt = datetime.datetime.now()
#         print(f'{dt} pressed={pressed}')
#     pressed += 1
#     found = press(pressed)
#
# print(f'{dt} RESULT: pressed={pressed}')
for i in range(10):
    press(i + 1)
    print(f'counts=[{counts[0]}, {counts[1]}] mul = {counts[0] * counts[1]}')
    counts = [0, 0]
