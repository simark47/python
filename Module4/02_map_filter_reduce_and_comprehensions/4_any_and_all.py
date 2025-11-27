# check if any even number is there

l=[1,3]
s=list(map(lambda x:True if x%2==0 else False, l))
print(s)

import functools
u=functools.reduce(lambda x, y:x or y, s)
print(u)

# using any keyword in map object if any of the values is truthy
v=any(map(lambda x:True if x%2==0 else False, l))
# or
w=any(s) # in list
print(v, w)


k=[1,3,2]
y=any(map(lambda x:True if x%2==0 else False, k))
z=any(list(map(lambda x:True if x%2==0 else False, k)))
print(y,z)


# using all keyword in map object if any of the values is truthy

l=[1,3,2]
y=all(map(lambda x:True if x%2 else False, l))
print(y)
k=[1,3]
y=all(map(lambda x:True if x%2 else False, k))
print(y)