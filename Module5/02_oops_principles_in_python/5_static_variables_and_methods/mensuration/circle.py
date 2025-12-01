from .shape import Shape

class Circle(Shape): 
    PI=3.14  #static variable
    def __init__(self, radius,x, y):
       
        super().__init__(0) 
        self.__radius = radius 
        self.x = x
        self.y = y
        self.PI=7
        
    @staticmethod
    def get_PI():
        return Circle.PI

    def get_radius(self):
        return self.__radius
    def area(self):
        return self.__radius * self.__radius * Circle.PI
    def perimeter(self):
        return self.__radius * 2 *self. PI
    def point_on_circle(self,x,y):
        return (self.x-x)**2 + (self.y-y)**2==self.__radius**2
  
         
