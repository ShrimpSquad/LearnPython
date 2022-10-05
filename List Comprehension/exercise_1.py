# Use list comprehension to turn the following code(s) into a single line


# Expected output -> [0, 3, 6, 9, 12]
# BEFORE
list = []
for i in range(5):
    list.append(i*3)

print(list)
# AFTER 
print([i*3 for i in range(5)])


# Expected output --> [2, 4, 6, 8, 10]
# BEFORE
list = []
for i in range(2,11,2):
    list.append(i)

print(list)

# AFTER
print([i for i in range(2,11,2)])





