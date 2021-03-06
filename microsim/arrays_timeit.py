#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quick test to compare the speed of numpy and pandas arrays.
Conclusions: pandas apply method(s) are vary quick, followed by map and numpy.
Looping through numpy arrays is OK but 10* slower than with apply. 
Iterating through pandas Series is much too slow.

Created on Mon May  4 15:25:32 2020

@author: Nick Malleson
"""

import random
from tqdm import tqdm
tqdm.pandas() # Activate tqdm for pandas, provides df.progress_apply()
import pandas as pd
import numpy as np
import timeit


age = []
print("Creating initial array", flush=True)
for _ in tqdm(range(1000000)):
    age.append(int(random.uniform(0,100)))


age_pd = pd.DataFrame({'age':age})
age_np = np.array(age)

def increment_age_np1():
    for i in range(len(age)):
        age[i] += 1
        
def increment_age_np2():
    return map( lambda x: x+1, age_np)

def increment_age_pd1(): # THIS TAKES AGES!
    for i in range(len(age)):
        age_pd.iloc[ i,:] =+ 1
        
def increment_age_pd2():
    return age_pd.apply(lambda x: x+1)
    #return age_pd.progress_apply(lambda x: x+1) # progress bar version
    
print(f"Time using numpy (for loop):")
print(timeit.timeit( increment_age_np1, number=100), flush=True)

print(f"Time using numpy (map):")
print(timeit.timeit( increment_age_np2, number=100), flush=True)

print(f"Time using pd (apply):")
print(timeit.timeit(increment_age_pd2, number=100), flush=True)

#print(f"Time using pd (normal)") # Takes too long
#print(timeit.timeit(increment_age_pd1, number=100))