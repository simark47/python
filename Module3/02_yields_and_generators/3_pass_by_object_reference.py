x=10
y="abc"
z=[1,2,3]
def func(x,y,z):
    x=x+5
    y=y+"def"
    z.append(4)
func(x,y,z)
print(x,y,z)
# for immutable types, a copy is created like int and string. original value remains intact. it is pass by value
# for mutable types, refers to the same container like list. original value gets changed.

# to pass a list by value only
z=[1,2,3,[4,0]]
def func2(x,y,z):
    x=x+5
    y=y+"def"
    z.append(5)
    z[3][1]=1
    print(x,y,z)
func2(x,y,z.copy())
print(x,y,z)

# it implies a shallow copy, which will still change the inside list
import copy
z=[1,2,3,[4,0]]
def func3(x,y,z):
    x=x+5
    y=y+"def"
    z.append(5)
    z[3][1]="deepcopy"
    print(x,y,z)
func3(x,y,copy.deepcopy(z))
print(x,y,z)