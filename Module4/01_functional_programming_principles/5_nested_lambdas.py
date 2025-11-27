# lambda functions can be returned from a function
def a():
    return lambda x:x*x

sq=a()
print(sq(2))

# can be passed as function arguments in another function
def b(func):
    return func

s=b(lambda x:x*x)(3)
print(s)

# lets try to create a function that sums up a list and passes it to another function in its parameter
'''
def square(x):
    return x*x
def sumOfList(l, func):
    a=sum(l)
    return func(a)
print(sumOfList([1,2,3,4,5], prodOfDig))

'''
sumOfList=lambda l, func:func(sum(l))
# can be passed as function arguments in another lambda function

print(sumOfList([1,2,3,4,5], lambda x:x*x))

# a function that takes a shape name and return shapename's area function
'''

def areaOfShapeName(shape_name):
    def areaOfCircle(r):
        return 3.14*r*r
    def areaOfSquare(s):
        return s*s
    if shape_name=="circle":
        return areaOfCircle
    elif shape_name=="square":
        return areaOfSquare
    
a=areaOfShapeName("square")
print(a(4))
'''
areaOfShapeName2=lambda s:(lambda r:3.14*r*r )if s=="circle" else (lambda s:s*s )

print(areaOfShapeName2("square")(4))