'''
Question: Boolean Indexing and Masking

You are given the following NumPy array:

import numpy as np

arr = np.array([10, 23, 45, 8, 19, 30, 7])

Tasks:

1. Select all elements greater than 20.


2. Replace all elements less than 10 with 0.


3. Count how many elements are between 15 and 35 (inclusive).
'''

import numpy as np

arr = np.array([10, 23, 45, 8, 19, 30, 7])
print(arr[arr>20])
replace=np.copy(arr)
replace[replace<10]=0
print(replace)
count=np.sum((arr>=15)&(arr<=35))
print(count)