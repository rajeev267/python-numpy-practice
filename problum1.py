# create a array of 20 elements 
# 1.reverse the array 
# 2.print every 3rd element 
# change every even element to 0
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

print(arr[::-1]) #1st 
print(arr[::3])#2nd 
new_arr=np.copy(arr)
new_arr[new_arr%2==0]=0
print(new_arr)#3rd 
print(np.var(new_arr))
print(np.std(new_arr))