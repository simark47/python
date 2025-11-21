# when we write a program, it stays in the hard disk 
#id() — Built-in Function

# id(obj) returns a unique integer that identifies the object during its lifetime
# On Python, this is typically the object’s memory address.
#  Identity Operators: is and is not that checks ids
a = [1, 2, 3]
b = a
print(a is b, id(a), id(b))   # True, strings are immmutable
a = [1, 2, 3]
b = [1, 2, 3]
print(a is not b, id(a), id(b)) #True lists are mutable
# to compare content
if(a==b):
    print("a==b")
else:
    print("not a=b")
 