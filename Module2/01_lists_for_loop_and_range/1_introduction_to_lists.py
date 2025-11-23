# LISTS are mutable , can change the elements
# lists maintain the order of elements
# duplicates are allowed
a=[1,2,3,4,5,1]
print(a, type(a), len(a))
b=["apple", "banana", "grapes", "oranges"]
c=["simar", 23,"f",["dance", "code","paint" ] ]



#printing item at an index
print(c[2])
print("----------")
print(c[3][0])
print("----------")
print(c[-1])

#slicing
print(a[1:3])
print(a[:3])
print(a[1:])
print(a[1:4:2])
print(a[::2])
print(a[::-1])
print("----------")

#updating
print(a, id(a))
a[2]="e"
print(a, id(a))
print(c, id(c[3]))
c[3][2]="cricket"
print(c, id(c[3]))

# create a new list
s=list() # or s=[]
s.append(1)
print(s)