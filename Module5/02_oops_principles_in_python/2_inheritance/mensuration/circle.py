from .shape import Shape
print(Shape)
PI=3.14
class Circle(Shape): # inherited shape class
    def __init__(self, radius,x, y):
        super().__init__(0) # you can not initialise a circle without initialising its parent class shape
        #check the parameters of parent class and pass arguments

        self.radius = radius
        self.x = x
        self.y = y

    def get_radius(self):
        return self.radius
    def area(self):
        return self.radius * self.radius * PI
    def perimeter(self):
        return self.radius * 2 * PI
    def point_on_circle(self,x,y):
        return (self.x-x)**2 + (self.y-y)**2==self.radius**2


'''
❌ You cannot run a Python file inside a package directly using:
python mensuration/circle.py
क्यों?
क्योंकि जब आप package ke andar ki file directly run करते हो,
Python us folder ko package nahi maanta.
और फिर imports fail हो जाते हैं 

Python kya expect karta hai?
Agar koi file package ke andar hai,
उसे हमेशा module ki tarah run karna padta है:
-------------------------------------------

from .shape import Shape
ImportError: attempted relative import with no known parent package
# To run this file in VS Code:
python -m mensuration.circle

# To run in PyCharm:
Click "Run current file" arrow > Edit Configurations > + >
Choose Python > Set "Type" = Module instead of Script
Set "Module name" = mensuration.circle
Set the Working Directory to the parent folder of 'mensuration'
(Up to the 'inheritance' folder, not inside the mensuration folder)
Then click Run

-------------------------------
# Reason:

If you run a file directly, Python does NOT treat the folder as a package,
so package imports do not work.

When you run circle.py directly, Python only looks in the current folder,
not in the parent folder. So it cannot find the 'mensuration' package.

Edit Configuration is a setting where you tell Python how to run your file.
Python must run your code from the parent directory of the package;
otherwise it cannot find the package.

'''