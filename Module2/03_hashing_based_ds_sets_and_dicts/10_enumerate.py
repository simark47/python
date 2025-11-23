l=[1,2,"apple", "none", 5.4]
# need both index and value
for i in enumerate(l):
    print(i[0],i[1])
print("----------")
for i, v in enumerate(l):
    print(i,v)

print("----------")
print(tuple(enumerate(l)))