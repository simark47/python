# what if we want to create a list of elements having squares of first 10 natural numbers
# we can add them through a loop or 
# write a criteria for every element of that list, set or dict

s=[x*x for x in range(1,11,2)] #from 1 to 11 gap of 2===> 1 3 5 7 9
print(s)
a={x for x in range(5)}
print(a)
names=["simar", "neha", "preet"]
lnames=["makkar", "kakkar", "chauhan"]
b={name:lname for(name, lname)in zip(names, lnames)}
print(b)