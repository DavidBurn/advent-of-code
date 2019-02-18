#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 12:17:36 2018

Advent of Code - Day 5

@author: dave
"""

import string
import time

start = time.time()

with open('/home/dave/Downloads/adventday5.txt') as file:
    chemical = file.read().strip('\n')
    
l = list(string.ascii_lowercase)
u = list(string.ascii_uppercase)

lu = list(zip(l,u))
ul = list(zip(u,l))
lowerU = [''.join(x) for x in lu]
upperL = [''.join(x) for x in ul]

reactions = lowerU + upperL

def fully_react(chemical):
    letsgo = True
    while letsgo:    
        counter = 0
        for r in reactions:
            if r in chemical:
                chemical = chemical.replace(r,'')
                counter+=1
        if counter == 0:
            letsgo = False
    return len(chemical)

part1_answer = fully_react(chemical)
print(part1_answer)

"""
Part Two
"""
answers = []

for lower, upper in zip(l, u):
    modified_chemical = chemical.replace(lower,'').replace(upper,'')
    remainder = fully_react(modified_chemical)
    answers.append(remainder)
    
print(sorted(zip(answers,l)))

end =time.time()

print(end-start)

def equal_opposite_case(x, y):
    return x != y and x.lower() == y.lower()


def react(so_far, new_element):
    if equal_opposite_case(so_far[-1], new_element):
        so_far = so_far[:-1]
    else:
        so_far.append(new_element)
    return so_far

functools.reduce(react, chemical, [])