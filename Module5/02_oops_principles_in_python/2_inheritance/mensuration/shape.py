class Shape: # class name uppercase
    def __init__(self, sides):
        self.sides = sides
    def get_sides(self): # function name should be lower case
        return self.sides


# lets try to inherit this in our circle and square classes
