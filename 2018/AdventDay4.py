#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 12:08:10 2019

@author: dave
"""

import numpy as np
import pandas as pd
import re

with open('day4input.txt') as file:
    data = file.read().split('\n')

df = pd.DataFrame([x.split(']') for x in data])
df.drop(1267, inplace=True)

df[0] = df[0].str.strip('[').str.replace('1518','2000')
df[0] = pd.to_datetime(df[0])

df.sort_values(by=0,inplace=True)
df['diff'] = df[0].diff()

def get_mins(row):
    try:
        mins = row['diff'].total_seconds() / 60
        if 'wake' not in row[1]:
            mins = 0
        return int(mins)
    except AttributeError:
        pass
    
df['minutes'] = df.apply(get_mins,axis=1)

def get_guard(row):
    m = re.search(r'\d+', row[1])
    if m:
        return int(m.group())
    return 0

df['guard'] = df.apply(get_guard, axis=1)
df['guard'].replace(to_replace=0, method='ffill', inplace=True)

mins_per_guard = df.groupby('guard',as_index=False)['minutes'].sum()
top_sleeper_idx = mins_per_guard['minutes'].idxmax()
top_sleeper = mins_per_guard['guard'][top_sleeper_idx]

def min_of_waking(row):
    if 'wake' in row[1]:
        return row[0].minute
    return 0

df['min_of_waking'] = df.apply(min_of_waking,axis=1)

def minute_array(row):
    empty = np.zeros(60)
    m = row['min_of_waking']
    empty[m-row['minutes']:m] += 1
    return empty

minute_arrays = df[df['guard']==top_sleeper].apply(minute_array, axis=1)

most_frequent = sum(minute_arrays).argmax()

print('Guard asleep most on the same minute :  {}'.format(top_sleeper))
print('On minute {}'.format(most_frequent))
print('Answer : {}'.format(top_sleeper * most_frequent))

def most_asleep_min(x):
    minute_arrays = df[df['guard']==x].apply(minute_array, axis=1)
    most_freq = sum(minute_arrays).argmax()
    total = sum(minute_arrays).max()
    return total, most_freq, x

min_and_total = [most_asleep_min(x) for x in [x for x in mins_per_guard['guard']]]
top = sorted(min_and_total, reverse=True)[0]

print('Guard number {} was asleep {} times on minute {}'.format(top[2],top[0],top[1]))
print('Answer : {}'.format(top[2]*top[1]))

