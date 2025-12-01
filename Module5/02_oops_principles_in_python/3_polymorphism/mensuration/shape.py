print("Shape imported") 
class Shape: # class name uppercase
    def __init__(self, sides):
        self.sides = sides
    def get_sides(self): 
        return self.sides


# lets try to inherit this in our circle and square classes
