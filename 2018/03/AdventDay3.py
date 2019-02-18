#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 23:00:02 2019

Advent Of Code Day3

@author: dave
"""

import pandas as pd
import numpy as np

df = pd.read_csv('day3input.txt',delimiter=' ', skip_blank_lines=True,header=None)

df['x_space'], df['y_space'] = df[2].str.strip(':').str.split(',',1).str
df['x_length'], df['y_length'] = df[3].str.split('x',1).str

df.drop(columns=[0,1,2,3],inplace=True)
df = df.astype(int)

max_x = df['x_space'].max() + df['x_length'].max()
max_y = df['y_space'].max() + df['y_length'].max()

fabric = np.zeros((max_x,max_y))

for i in range(len(df)):
    x, y, x_length, y_length = df.loc[i,:]
    claim = np.ones((x_length, y_length))
    fabric[x:x+x_length, y:y+y_length] += claim
    
unique, counts = np.unique(fabric,return_counts=True)

total_double_matched = counts[2:].sum()

print(total_double_matched)

for i in range(len(df)):
    x, y, x_length, y_length = df.loc[i,:]
    claim = np.ones((x_length, y_length))
    if np.array_equal(fabric[x:x+x_length, y:y+y_length], claim):
        print('Thats the one! : ', df.loc[i,:])