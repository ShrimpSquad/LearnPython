
names = ["seb", "nick", "jules"]
weight_lbs = ["200", "185", "220"]

d = {}
for name in names:
    for weight in weight_lbs:
        d[name] = weight
        weight_lbs.remove(weight)
        break
    
print(d)