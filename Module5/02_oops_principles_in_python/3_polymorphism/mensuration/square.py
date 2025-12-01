from .shape import Shape

print("Square imported") 
class Square(Shape):

    def __init__(self, s):
        super().__init__(4)
        self.side = s
    def area(self):
        return self.side ** 2
    def perimeter(self):
        return 4*self.side