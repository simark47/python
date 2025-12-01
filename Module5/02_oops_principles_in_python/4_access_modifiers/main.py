#  we discussed that python does not suppot data hiding too much 
# like you could access radius after initialising 
# print(c.radius)
# also sides of inherited shape like circle. sides

# to make the variables private, use __ before its name
from mensuration import circle, square
c=circle.Circle(2,0,0)
s=square.Square(5)

a=[c,s]
for i in a:
    print(i.area())

# now you can not access sides or radius as they are private
# print(c.radius)
# print(c.sides)

print(c.get_radius()) 
print(c.get_sides())
print(s.get_side_length())
print(s.get_sides())



# print(s.number_of_sides())
# still gives an error if the variable sides is private and we can not acccess number of sides in circle or square which is a child class

# but we might need the sides (variable of parent) in child/inherited classes 
# for  this reason we make the color variable protected by using single _

print(c.get_color())
print(s.get_color())
# allowed becuase color is protected


