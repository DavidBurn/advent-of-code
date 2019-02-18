#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 21:34:40 2019

Advent of code day 1

@author: dave
"""
import time

start = time.time()

with open('day1input.txt') as file:
    data = file.read().split()
    
first_total = sum(int(x) for x in data)
print('Sum of all entries : {}'.format(first_total))
"""
Part 2
"""

total = 0
subtotals = {0}
run = True
while run:
    for x in data:
        total += int(x)
        if total in subtotals:
            print('First repeated total : {}'.format(total))
            run = False
            break
        subtotals.add(total)
        
end = time.time()

print(end-start)