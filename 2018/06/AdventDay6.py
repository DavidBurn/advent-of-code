#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 13:01:37 2018

Advent of code - Day 6

@author: dave
"""
import numpy as np

with open('day6input.txt') as file:
    coords = file.read().split()

x_coords = [int(coords[i].strip(',')) for i in range(0,len(coords),2)]
y_coords = [int(coords[i]) for i in range(1, len(coords),2)]

COORDS= list(zip(x_coords, y_coords))

#Distance from one point to another is x1+y1 - x2+y2

grid = np.zeros((max(x_coords), max(y_coords)))

def get_shortest_distance(point,coords=COORDS):
    distances = [abs(point[0] - coord[0]) + abs(point[1] - coord[1]) for coord in coords]
    distances = np.array(distances)
    if sorted(distances)[0] == sorted(distances)[1]:
        return -1
    return distances.argmin() + 1
    
for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
        grid[(i,j)] = get_shortest_distance((i,j))

edges = [grid[0], grid[max(x_coords)-1], grid[:,0], grid[:, max(y_coords)-1]]

flattened_edges = [y for x in edges for y in x]
unique, count = np.unique(grid, return_counts=True)
inner_areas = [x for x in sorted(zip(count, unique)) if x[1] not in flattened_edges]

print(inner_areas[-1])

"""
Part 2 - Find all areas with less than 10000 total distance from all points
"""

def is_point_under_total_distance(point, coords = COORDS, distance=10000):
    distances = [abs(point[0] - coord[0]) + abs(point[1] - coord[1]) for coord in coords]
    if sum(distances) < 10000:
        return 1
    return 0

grid2 = np.zeros((max(x_coords), max(y_coords)))
for i in range(grid2.shape[0]):
    for j in range(grid2.shape[1]):
        grid2[(i,j)] = is_point_under_total_distance((i,j))

print(grid2.sum())

