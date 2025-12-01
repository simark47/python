from .shape import Shape
print("Circle imported") #to  be printed everytime circle is imported
PI=3.14
class Circle(Shape): 
    def __init__(self, radius,x, y):
        super().__init__(0) 

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

