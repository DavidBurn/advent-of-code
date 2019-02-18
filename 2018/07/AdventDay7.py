#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 14:06:36 2019

Advent of Code day 7

@author: dave
"""
import string
import re
from collections import defaultdict

with open('day7input.txt') as file:
    data = file.read().split('\n')
    
letters = [re.findall(r'[A-Z]', x)[1:] for x in data]
del letters[-1]
letter_map = {k:v for v, k in enumerate(string.ascii_uppercase)}
pre_numbers = list(map(letter_map.get,[x[0] for x in letters]))
next_numbers = list(map(letter_map.get,[x[1] for x in letters]))

l = dict((x,[]) for x in range(26))

for v, k in zip(pre_numbers, next_numbers):
    l[k].append(v)
    
order = []

def remove():
    while True:
        ready = [x for x in l.keys() if not l[x]]
        for k, v in l.items():
            n = sorted(ready)[0]
            if n in l[k]:
                l[k].remove(n)
        order.append(n)
        del l[n]
        if len(order) == 26:
            break
    
remove()
n_map = {k:v for k, v in enumerate(string.ascii_uppercase)}
print(''.join(list(map(n_map.get,order))))