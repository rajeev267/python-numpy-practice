'''Q5:
Create a 10x10 array with values from 1 to 100.

Split it into two arrays:

1. One with all even numbers
2. One with all odd numbers'''
import numpy as np
arr=np.arange(1,101).reshape(10,10)
print(arr)
even=arr[arr%2==0]
print(even)
odd=arr[arr%2==1]
print(odd)
