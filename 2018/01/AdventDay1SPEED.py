#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 23:19:39 2019

@author: dave
"""

import itertools
import time
start = time.time()

with open('day1input.txt') as file:
    data = file.read().split()

first_total = sum(int(x) for x in data)
print('Sum of all entries : {}'.format(first_total))

cycler = itertools.cycle([int(x) for x in data])
acc = itertools.accumulate(cycler)

totals = {0}

print(next(x for x in acc if x in totals or totals.add(x)))

end = time.time()

print(end-start)