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

l = dict((x,[]) for x in string.ascii_uppercase)

for le in letters:
    l[le[1]].append(le[0])
    
order = []

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
    
print(''.join(order))