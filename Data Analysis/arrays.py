import numpy as np

#------------------------- Creating Arrays

# ar1 = np.arange(1,100,4) # Creates an array from 1-100, steps of 4
# ar2 = np.zeros(5) # Creates an array of five 0's
# ar3 = np.ones(5) # Creates an array of five 1's
# ar4 = np.eye(5) # Creates an 5x5 array with 1's as diagonals and the rest 0's

# print(ar1)
# print(ar2)
# print(ar3)
# print(ar4)

#------------------------- Arithmetics in Arrays

# arr1 = np.array([[1,2,3,4],[8,9,10,11]])

# print(arr1)
# print(arr1**2) # Multiplying numbers in the same spots
# print(arr1 - (arr1 + 1)) # All values will be -1
# print(arr1 + arr1) # Doubles all values
# print(2 / arr1) 

#------------------------- Indexing Arrays

arr1 = np.arange(0,11)
slice_of_arr1x = arr1[2:5].copy() # This will create a copy and not be affected by changes.
slice_of_arr1 = arr1[2:5]
print(arr1[0])
print(arr1[2:5],arr1[6:9])
arr1[0:5] = 100
print(arr1)
print(arr1[3:8])
print(slice_of_arr1)
print(slice_of_arr1x)
