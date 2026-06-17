'''Q6:
Given two arrays:

a = [1, 2, 3, 4, 5]  
b = [3, 4, 5, 6, 7]

Find the common elements between them.

Then find elements that are only in a (but not in b).'''
import numpy as np
a =np.array ([1, 2, 3, 4, 5] ) 
b =np.array([3, 4, 5, 6, 7])
common=np.intersect1d(a,b)
diff_a=np.setdiff1d(a,b)
print(common)
print(diff_a)
# 2d
c=np.array([[1,2,3],[4,5,6]])
d=np.array([[2,3,1],[5,6,7]])
flat_c=c.flatten()
flat_d=d.flatten()
common2d=np.intersect1d(flat_c,flat_d)
print(common2d)
