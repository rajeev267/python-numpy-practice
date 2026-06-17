'''4:Create a 1D array with 25 numbers.

Reshape it into a 5x5 matrix.

Set all values except the diagonal to 0.
'''
import numpy as np
array=np.arange(1,26)
print(array)
arr_2d=array.reshape(5,5)
print(arr_2d)
col=np.eye(5)*arr_2d
print(col)

