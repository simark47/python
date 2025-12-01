from mensuration import circle # this means circle.py
c=circle.Circle(4,0,0) # this means to create object from circle.py's Circle class
print(c.area())
c2=circle.Circle(2,0,0)
print(c2.perimeter())
c.radius=7
print(c.area())

from mensuration.circle import Circle # this means from circle.py import Circle object directly
c=Circle(4,0,0)