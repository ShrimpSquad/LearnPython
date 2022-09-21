import numpy as np

arr1 = np.arange(0,11)
print(arr1)
print(arr1[8])
print(arr1[:5])
arr2 = arr1
arr2[0:5] = 100
print(arr2)
arr = np.arange(0,11)
slice_of_arr = arr[0:6]
print(slice_of_arr)