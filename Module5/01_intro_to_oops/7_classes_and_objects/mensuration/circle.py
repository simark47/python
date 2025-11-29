class circle:
    def __init__(self, radius, x, y):
        # initialise function =declare all variables in init = data we want to have in class
        self.radius = radius
        self.x = x
        self.y = y
    # this is a constructor

    def area(self):
        return 3.14*self.radius**2
    def perimeter(self):
        return 3.14*2*self.radius
    def pointOnCircle(self, x, y):
        return (self.x-x)**2 + (self.y-y)**2==self.radius**2

# classes: we can have our own data type say a product and that product will have attributes and functions
