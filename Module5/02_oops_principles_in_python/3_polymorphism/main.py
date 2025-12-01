# polymorphism= many forms
# Len is a function that works for strings ,lists, dicionaries, set
# sum is a function that works for strings ,numbers


from mensuration.circle import Circle
from mensuration.square import Square

c=Circle(2,0,0)
c2=Circle(4,0,0)
s=Square(5)

# lets say we put these both in a list
List=[s,c, c2]

# now we can find area
for i in List:
    print(i.area())


# area function takes any form depending on usage