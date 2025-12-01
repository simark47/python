# ways to import
from mensuration import circle
from mensuration.square import Square

# create instance
c=circle.Circle(4,0,0)
s=Square(5)

print(c.get_radius())
print(s.perimeter())
print(s.area())

#now we can check sides too
print(c.sides)
print(s.sides)

