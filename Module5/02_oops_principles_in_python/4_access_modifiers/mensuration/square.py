from .shape import Shape

class Square(Shape):

    def __init__(self, s):
        super().__init__(4, "pink")
        self.__sideLength = s #side is private
    def area(self):
        return self.__sideLength ** 2
    def perimeter(self):
        return 4*self.__sideLength
    def get_side_length(self):

        return self.__sideLength
    def get_color(self):
        
        return self._color