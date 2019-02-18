#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 13:01:37 2018

Advent of code - Day 6 - Functional

@author: dave
"""

import time
import numpy as np
import itertools

start = time.time()

with open('day6input.txt') as file:
    coords = file.read().split()

x_coords = [int(coords[i].strip(',')) for i in range(0,len(coords),2)]
y_coords = [int(coords[i]) for i in range(1, len(coords),2)]

coords= list(zip(x_coords, y_coords))

def get_shortest_distance(point):
    distances = [abs(point[0] - coord[0]) + abs(point[1] - coord[1]) for coord in coords]
    distances = np.array(distances)
    if sorted(distances)[0] == sorted(distances)[1]:
        return -1
    return distances.argmin() + 1

perm = itertools.product(list(range(max(x_coords+y_coords))),repeat=2)
distances = [get_shortest_distance(x) for x in perm]
grid = np.array(distances).reshape(354,354)
edges = [grid[0], grid[max(x_coords)-1], grid[:,0], grid[:, max(y_coords)-1]]

flattened_edges = [y for x in edges for y in x]
unique, count = np.unique(grid, return_counts=True)
inner_areas = [x for x in sorted(zip(count, unique)) if x[1] not in flattened_edges]

print(inner_areas[-1])

"""
Part 2 - Find all areas with less than 10000 total distance from all points
"""

def is_point_under_total_distance(point, distance=10000):
    distances = [abs(point[0] - coord[0]) + abs(point[1] - coord[1]) for coord in coords]
    if sum(distances) < 10000:
        return 1
    return 0

p = itertools.product(list(range(max(x_coords+y_coords))),repeat=2)
under_10k = [is_point_under_total_distance(x) for x in p]
print(sum(under_10k))


end = time.time()

print(end-start)
