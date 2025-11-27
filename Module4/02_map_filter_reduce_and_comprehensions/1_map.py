#  we already have used the inbuilt map function which takes an iterable and a function and stores the value in map object, we can later convert 
# (int function, string iterable)
a=map(int, input().split())

print(list(a), type(a))

# lets say we want a tuple's squares in another tuple

t=(1,2,3,4)
l=[]
for i in t:
    l.append(i*i)
print(tuple(l))

# or
a=tuple(map(lambda x:x*x, t))
print(a)