# Define a function that checks how many unique numbers are within a list

def unique_nums(my_list):
    new_list = []
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
    return new_list

print(unique_nums([1, 1, 1, 3, 4, 5, 6, 7, 8]))


# An easier solution would be simply to return a list of the set of a list

def set_from_list(my_list):
    return list(set(my_list))

print(set_from_list([1, 1, 1, 3, 4, 5, 6, 7, 8]))