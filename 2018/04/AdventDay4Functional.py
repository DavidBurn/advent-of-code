#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 07:56:05 2019

@author: dave
"""
import pandas as pd
import time
import re
import numpy as np

start = time.time()

with open('day4input.txt') as file:
    data = file.read().split('\n')
    
def change_date(row):
    date = row[0].strip('[').replace('1518','2000')
    return pd.to_datetime(date)

def get_mins(row):
    try:
        mins = row['diff'].total_seconds() / 60
        if 'wake' not in row[1]:
            mins = 0
        return int(mins)
    except AttributeError:
        pass
    
def get_guard(row):
    m = re.search(r'\d+', row[1])
    if m:
        return int(m.group())
    return 0

df = (
    pd.DataFrame([x.split(']') for x in data])
    .drop(1267)
    .assign(date=lambda df: df.apply(change_date,axis=1))
    .sort_values(by='date')
    .assign(
        diff=lambda df: df['date'].diff(),
        minutes=lambda df: df.apply(get_mins, axis=1),
        guard=lambda df: df.apply(get_guard, axis=1),
    )
    .assign(guard=lambda df: df['guard'].replace(to_replace=0, method='ffill'))
)
    
mins_per_guard = df.groupby('guard',as_index=False)['minutes'].sum()
top_sleeper_idx = mins_per_guard['minutes'].idxmax()
top_sleeper = mins_per_guard['guard'][top_sleeper_idx]

def minute_array(row):
    empty = np.zeros(60)
    if 'wake' in row[1]:
        m = row['date'].minute
        lead = [0 for x in range(m-row['minutes'])]
        ones = [1 for x in range(row['minutes'])]
        post = [0 for x in range(60-len(lead)-len(ones))]
        return empty + (lead+ones+post)
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