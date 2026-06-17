'''
Q1:Create a 6x6 NumPy array with values from 0 to 35.

Extract all elements greater than 12 and less than 24.

Then calculate the sum of those elements.'''
import numpy as np
arr=np.arange(36)
arr3d=arr.reshape(6,6)
print(arr3d)
ext=arr3d[(arr3d>12)&(arr3d<24)]
print(ext)

print(ext.sum())