a=1
print(type(a))
b=21.5
print(type(b))
c=True
print(type(c))
d="simarpreet"
print(d, type(d), id(d))
# strings are immutable in python
# if you try to change
# d[5]="a" is not alowed
d="ftyguhi"
print(d, type(d), id(d))
d=d+"s"
print(d, type(d), id(d))
e='R'
print(type(e))
d=5
print(type(d))
# variables are dynamically types - type is decided at run time
# codes may become bug prone due to this
 
#type conversion
x=input()
print(type(x))
# takes only str input for jkhgjf and 5 as well, we can later convert into int by int(x)

y=int(input()) #expects an int input
print(type(y))

#similarly we have str(), float(), bool()
y=str(input()) #converts to str
print(y, type(y))
y=float(input()) #converts int to float
print(y, type(y))
y=bool(int(input())) #converts int to bool->empty string and 0 False,  everything else True
print(y, type(y))
