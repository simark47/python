# is it possible to return a function?
# yes ,  because functions are first-class objects.
# like we give a function some shape and it returns the function to calculate area of that shape
def areaOfShape(shape_name):
    def areaOfCircle(r):
        return 3.14*r*r
    def areaOfSquare(s):
        return s*s
    if shape_name=="circle":
        return areaOfCircle
    elif shape_name=="square":
        return areaOfSquare
    
# lets call it
x=areaOfShape("circle")
print(x,type(x))

# since this has returned a function we can call it to find area
print(x(3))

# or using a short cut you can directly call it after its returned
x=areaOfShape("circle")(3)
print(x)

# Currying means converting a function returns a function , that also expects an argument.. we chain it into a sequence

# Example of currying: Currying requires 1-arg → 1-arg → ... chain

def multiply(a):
    def inner(b):
        return a * b
    return inner

print(multiply(5)(3))
