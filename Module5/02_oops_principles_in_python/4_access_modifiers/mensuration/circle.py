from .shape import Shape
PI=3.14
class Circle(Shape): 
    def __init__(self, radius,x, y):
        super().__init__(0, "blue") 
        self.__radius = radius #private radius
        self.x = x
        self.y = y

    def get_radius(self):
                return self.__radius
    def area(self):
        return self.__radius * self.__radius * PI
    def perimeter(self):
        return self.__radius * 2 * PI
    def point_on_circle(self,x,y):
        return (self.x-x)**2 + (self.y-y)**2==self.__radius**2
    def get_color(self):
         return self._color
         
