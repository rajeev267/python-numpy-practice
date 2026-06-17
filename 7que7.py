'''Q7:
Create an array of 20 random float values between 0 and 1.

Normalize the array so that the maximum becomes 1 and the minimum becomes 0.

'''
import numpy as np

arr=np.random.random(20)
normal=(arr-arr.min())/(arr.max()-arr.min())
print(normal)
# i dont now what is this 