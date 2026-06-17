'''

Question: You are given the following 2D NumPy array:

import numpy as np

a = np.array([[3, 7, 5],
              [8, 4, 3],
              [6, 2, 9]])

Tasks:

1. Find the maximum value in each row.


2. Find the index of the minimum value in each column.


3. Normalize the array so that all values are between 0 and 1.
'''
import numpy as np

a = np.array([[3, 7, 5],
              [8, 4, 3],
              [6, 2, 9]])
print(np.max(a,axis=1))
print(np.min(a,axis=0))
normalized_a=(a-a.min())/(a.max()-a.min())
print(normalized_a)