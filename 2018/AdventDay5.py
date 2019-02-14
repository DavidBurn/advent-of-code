#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 12:17:36 2018

Advent of Code - Day 5

@author: dave
"""

import string

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
            print('No more reactions, number left : ',len(chemical))
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





