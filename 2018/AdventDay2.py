#!/usr/bin/env ·python3→─→njlĸ 
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 22:00:12 2019

Advent Of Code Day 2

@author: dave
"""
from collections import defaultdict
import itertools

with open('day2input.txt') as file:
    data = file.read().split()

twos = 0
threes = 0

def check_pairs(string, twos, threes):
    letters = defaultdict(int)
    for s in string:
        letters[s] += 1
    if 2 in letters.values():
        twos += 1
    if 3 in letters.values():
        threes += 1
    return twos, threes

for d in data:
    twos, threes = check_pairs(d, twos, threes)
    
print('Twos = {}, Threes = {}'.format(twos, threes))

print('Checksum = {}'.format(twos*threes))

def check_matches(string1, string2, num_diffs=1):
    diffs = 0
    matched = []
    for l1, l2 in zip(string1, string2):
        if l1 != l2:
            diffs += 1
            if diffs > num_diffs:
                pass
        else:
            matched.append(l1)
    if diffs == num_diffs:
        print('String 1 : {}. String 2 : {}.'.format(string1, string2))
        print('Matching characters : {}'.format(''.join(matched)))
        
for x in itertools.combinations(data,2):
    check_matches(*x)
