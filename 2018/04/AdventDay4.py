#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 12:08:10 2019

@author: dave
"""

import numpy as np
import pandas as pd
import re
import time

start = time.time()

with open('day4input.txt') as file:
    data = file.read().split('\n')

df = pd.DataFrame([x.split(']') for x in data])
df.drop(1267, inplace=True)

def change_date(row):
    date = row[0].strip('[').replace('1518','2000')
    return pd.to_datetime(date)

df['date'] = df.apply(change_date,axis=1)

df.sort_values(by='date',inplace=True)
df['diff'] = df['date'].diff()

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

def minute_array(row):
    empty = np.zeros(60)
    if 'wake' in row[1]:
        m = row['date'].minute
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

end = time.time()

print('Time taken : {}'.format(end-start))