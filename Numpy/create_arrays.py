import numpy as np
my_list1 = [1,2,3,4]
my_list2 = [11,22,33,44]

my_lists = [my_list1, my_list2]
my_array = np.array(my_lists)
print(my_array)
print(my_array.shape)
print(my_array.dtype)
print(np.zeros([5,5]))
print(np.eye(5))
print(np.arange(5,50,2))