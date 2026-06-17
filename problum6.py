'''

Question 1: Array Manipulation

Given the following 1D NumPy array:

import numpy as np

arr = np.array([3, 5, 7, 9, 11, 13])

Tasks:

1. Reshape the array into a 2D array with 2 rows and 3 columns.


2. Add 5 to each element in the array.


3. Compute the square of each element in the array.

Question 2: Advanced Array Operations

Given the following 2D NumPy array:

import numpy as np

matrix = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])

Tasks:

1. Extract the second row of the matrix.


2. Extract the first column of the matrix.


3. Compute the sum of all the elements in the matrix.


4. Find the mean of each row in the matrix.
'''
import numpy as np

arr = np.array([3, 5, 7, 9, 11, 13])
array=arr.reshape(2,3)
print(array)
print(arr+5)
print(arr**2)
# que2

matrix = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])
secrow=matrix[1]
print(secrow)
seccol=matrix[:,0]
print(seccol)
print(matrix.sum())
print(matrix.mean(axis=1))