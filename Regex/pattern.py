import re

pattern = re.compile("^(7|8|9)[0-9]{9}")
number = input("Number? ")
if pattern.match(number): 
    print("YES")
else: 
    print("NO")