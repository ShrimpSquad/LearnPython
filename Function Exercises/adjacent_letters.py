# Define a function that when given a list of letters,
# it returns true if adjacent letters are the same

def adjacent_letters(list):
    for i in range(len(list)):
        if list[i - 1] == list[i]:
            return True
    return False

adj_list = ["a","a","b"]
non_adj_list = ["a","b","c"]

print(adjacent_letters(adj_list))
print(adjacent_letters(non_adj_list))

