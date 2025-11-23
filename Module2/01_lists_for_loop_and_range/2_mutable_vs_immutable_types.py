# strings and integers are immutable(non changeable), but lists are mutable
#  any operation changes the id
name="simar"
print(name, id(name))
name="preet"
print(name, id(name))
name= name+"kaur"
print(name, id(name))
b=24
print(b, id(b))
b=75
print(b, id(b))
b+=1
print(b, id(b))
print("----------")
a=["apple", ["mango", "banana", "pear"], 4,5,6]
print(a,id(a))
a.insert(0, 1)
print(a,id(a))
a.append(7)
print(a,id(a))
b=[9,10]
a.extend(b)
print(a,id(a))


a.remove(1) #exact element
print(a,id(a))
a.pop(3) # index
print(a,id(a))
a.pop() # by default last
print(a,id(a))
del a[1]
print(a,id(a))
a.clear()
print(a,id(a))
a=["apple", ["mango", "banana", "pear"], 4,5,6]
#remove throws error if element is not present
#pop and del throw error if index is out of range

a=["apple", ["mango", "banana", "pear"], 4,5,6]
b=[9,10]
a=a+b
print(a,id(a))

print(b*3)
