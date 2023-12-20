#!/usr/bin/python3

# python3 -m doctest -v 05b.py

'''
'''


with open('input/05.txt', 'r') as f:
# with open('input/05-small.txt', 'r') as f:
    lines = f.readlines()
lines = [l.rstrip() for l in lines]
lines = [l for l in lines if l]

def parse_seeds(s):
    '''
    >>> parse_seeds('seeds: 79 14 55 13')
    [(79, 14), (55, 13)]
    '''
    nums = s.split(' ')[1:]
    nums = [int(n) for n in nums]

    seeds = []
    for i in range(0, len(nums), 2):
        seeds.append((nums[i], nums[i + 1]))
    return seeds

def parse_map(begin, end):
    triplets = []
    for s in range(begin + 1, end):
        dst, src, num = [int(l) for l in lines[s].split(' ')]
        triplets.append( (src, dst, num) )
    triplets = sorted(triplets)

    source_map = []
    for k in range(len(triplets) - 1):
        source_map.append(triplets[k])
        src, dst, num = triplets[k]
        next_src, _, next_num = triplets[k + 1]
        if src + num < next_src:
            source_map.append( (src + num, src + num, next_src - (src + num) ) )
    source_map.append(triplets[-1])
    last_src, last_dst, last_num = triplets[-1]
    source_map.append( (last_src + last_num, -1, -1) )

    return source_map

def mapped(seed, mapa):
    id = -1
    for k in range(len(mapa)):
        if seed >= mapa[k][0]:
            id = k
    if id < 0:
        return seed
    src, dst, _ = mapa[id]
    if dst < 0:
        return seed
    return dst + seed - src

maps = []
for row in range(len(lines)):
    if 'map:' in lines[row]: maps.append(row)

seed_soil = parse_map(maps[0], maps[1])
soil_fertilizer = parse_map(maps[1], maps[2])
fertilizer_water = parse_map(maps[2], maps[3])
water_light = parse_map(maps[3], maps[4])
light_temperature = parse_map(maps[4], maps[5])
temperature_humidity = parse_map(maps[5], maps[6])
humidity_location = parse_map(maps[6], len(lines))

seeds = parse_seeds(lines[0])
min_location = -1
for start, length in seeds:
    for i in range(length):
        soil = mapped(start + i, seed_soil)
        fertilizer = mapped(soil, soil_fertilizer)
        water = mapped(fertilizer, fertilizer_water)
        light = mapped(water, water_light)
        temperature = mapped(light, light_temperature)
        humidity = mapped(temperature, temperature_humidity)
        location = mapped(humidity, humidity_location)

        if min_location == -1:
            min_location = location
        if location < min_location:
            min_location = location

print(min_location)




