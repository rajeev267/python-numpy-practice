import numpy as np
# arr=np.ones((6,6),dtype=int)
# print(arr)
# arr[1:-1,1:-1]=0
# print(arr)
arr2=np.zeros((8,8))
# print(arr2)
arr2[1::2,::2]=1
arr2[ ::2,1::2]=1
print(arr2)

