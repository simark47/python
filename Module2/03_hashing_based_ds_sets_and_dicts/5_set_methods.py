s=set() #empty set
t={"s", "y", "u", 4}
z={1,2,3,4, "u"}
#union= combine all elements in 2 sets
for i in t:
    s.add(i)
for i in z:
    s.add(i)
print(s)
print("----------")

#intersection= common element of 2 sets
m=set()
for i in t:
   if i in z:
      m.add(i)
print(m)
print("----------")

#symmetric difference: unique elements in both lists but not common
sd=set()
for i in t:
    if i not in z:
        sd.add(i)
for i in z:
    if i not in t:
        sd.add(i)
print(sd)

print("----------")

s= t.union(z)
print(s)
s= t.intersection(z)
print(s)
s= t.symmetric_difference(z)
print(s)