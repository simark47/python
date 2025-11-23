a=[1,2,3,4,5,1]
b=["apple", "banana", "grapes", "oranges"]
c=["simar", 23,"f",["dance", "code","paint" ] ]
#traversal
i=0
while i< len(b):
    print(b[i])
    i+=1
print("----------")

for i in a:
    print(i)
print("----------")
for i, g in enumerate(c):  
    print(i,g)
print("----------")


a="apple"
for i in a:
    print(i)

# in same line
for i in a:
    print(i, end=" ")