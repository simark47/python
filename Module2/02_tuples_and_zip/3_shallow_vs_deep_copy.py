t=[1,2,3,4,[4,5,6],(7,8,9),"apple",True, 5.4]
t2=t
print(t2, id(t), id(t2))
print("----------")
# ids are same,both are pointing to the same object now lets try to make a change
t2.append(9)
print(t,  id(t))
print(t2, id(t2))
print("----------")
t[4].append("7")
print(t,  id(t))
print(t2, id(t2))
# both of them got changed

# what if we dont want them to change?
# lets try another method
print("----------")
t3=t.copy()
print(t3, id(t3))
# ids are different,both are pointing to the different object now lets try to make a change

t3.append(7)
print(t,  id(t))
print(t3, id(t3))
print("----------")
# t3 alone changed
# what if change the inside list
t3[4].append("shallow copy")

print(t,  id(t))
print(t3, id(t3))
print("----------")
# this is reflecting in both the lists
# it happens because it is a shallow copy and all elements are copied to one level through copying thei ids,(not their internal objects) for lists it is still the id and we can access and change
print(id(t[4]), id(t3[4]))

# to create a deep copy,  use import copy
import copy
t4=copy.deepcopy(t)
print(id(t[4]), id(t4[4]))
# ids are different,both are pointing to the different object now lets try to make a change
print("----------")
t4[4].append("deep copy")
print(t,  id(t))
print(t4, id(t4[4]))
print("----------")
# this is reflecting in only t4
# it happens because it is a deep copy and all elements are copied to every level
# shallow is fast, deep is slow