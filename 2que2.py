'''Q2:Create a 4x5 array with random integers.

Find the maximum value in each row.

Then calculate the average of those maximum values.'''
import numpy as np

rows = 4
cols = 5
min_val = 1
max_val = 100

array = np.random.randint(min_val, max_val + 1, size=(rows, cols))
print(array)
max_value=np.max(array,axis=1)
print(max_value)
print(np.mean(max_value))