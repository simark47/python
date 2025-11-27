# as the name suggests , filter method takes some iterables and filter them based on the function

l=[1,2,3,4,5,6,7,8,9,10]
r=filter(lambda x:True if x%2==0 else False, l)
print(r,type(r))

s=list(filter(lambda x:True if x%2==0 else False, l))
t=list(filter(lambda x: x%2==0 , l))
u=list(filter(lambda x: x%2 , l)) #odd as even is falsy
# same 
print(s, type(s))
print(t, type(t))
print(u, type(u))

# only filter odd numbers and then map them to their squares
v=list(map(lambda x:x*x, filter(lambda y:y%2, l)))
print(v)
