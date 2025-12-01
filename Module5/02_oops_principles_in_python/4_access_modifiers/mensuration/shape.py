print("Shape imported") 
class Shape: 
    def __init__(self, sides, color):
        self.__sides = sides #sides is private
        self._color = color # color is protected

    def get_sides(self): 
        return self.__sides


# lets try to inherit this in our circle and square classes
