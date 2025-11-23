t=(1,2,3,[4,5,6],7)
# as lists are mutable, we can access this list out of tuple and change it
for i in t:
    print(id(i))
print(t[3])
t[3][1]="aple"
print(t)
t[3].append(9)
print(t)

for i in t:
    print(id(i))
# it happens because when we create a tuple, it combines and stores all the ids of its elements
# we can acess the tuple and change the elements as the memory location remains same