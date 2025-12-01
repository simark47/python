# to acccess a class's methods, we need to create object of it first
from mensuration.circle  import Circle
s=Circle(2,0,0)

#  these are non static methods- which needs to have a object created to use

# but we can create some static variables and methods
print(Circle.PI)   #class variable remains unchanged and is attached to class
print(s.PI)         #instance variable 
print(s.area()) #uses class's variable
print(s.perimeter()) #uses self.pi

print(Circle.get_PI())