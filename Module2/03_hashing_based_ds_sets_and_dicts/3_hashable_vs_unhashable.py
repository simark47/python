# python has a hash defined for strings, int, tuples 
# but not for a list as its mutable so not able to generate a hashvalue for it

print(hash({1,2,3,4}))
# set itself is also unhashable and mutable