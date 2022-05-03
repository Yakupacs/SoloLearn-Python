text = input()
dict = {}
for x in text:
    if x in dict.keys():
        dict[x] += 1
    else:
        dict[x] = 1
print(dict)