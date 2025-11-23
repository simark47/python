# tuples are immutable forms of a list
# tuples are ordered and allow duplicates
# used to declare things that remain same throughout
t=(1,2,3,4,5,6,2,3)
print(t[2])
print(t[1:4])
print(t[::-1])
for i in t:
    print(i, end="")
print()
print(len(t))
print(t*2)
t2=(5,6,7,8, "aple", True, 5.4)
t=t+t2
print(t)
z=tuple() #or()
print(z)

 #you cant do:
# t[3]="banana"
# t.append(9)