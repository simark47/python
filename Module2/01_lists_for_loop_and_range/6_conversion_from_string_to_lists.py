# if we give single line of string input of space separated integers and want it to be converted into a list

# use split(" ")
#  it will split the integers on a space

# use split()
#  it will split the integers on uneven space

s="1 2  8  7 5  6"
print(s, type(s))
n=s.split(" ") 
m=s.split()

print(n, type(n))
print(m, type(m), type(m[0]))
print("----------")

# convert elements to int
for i in range(len(m)):
    m[i]=int(m[i])
print(m,type(m), type(m[0]))
m.sort()
print("sorted")
print(m)
print("----------")

s="simar:preet:kaur"
n=s.split(":") 
print(n, type(n))
# Joining a string is simple:

a = "-".join(n)
print(a)