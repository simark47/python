# lets see what are pure functions and pure anonymous/lambda functions
x=100
def impureF():
    global x
    x+=1
    print(x)
print("start:", x)
impureF()
impureF()
print("end:", x)
# it is an impure function as it gives different output each time its called and affects the outside variable
print("----------")

x=200
def pureF(x):
    x+=1
    print(x)
print("start:", x)
pureF(x)
pureF(x)
print("end:", x)  
# it is an pure function as it gives same output each time its given same input and does not affect the outside variable
print("----------")
# better and easy way to write the pure function is lambda function- where we do not provide the name 
def cube(x):
    return x*x*x
s=cube(5)
print(s)
# or 
s= lambda x: x*x*x
print(s(5))

# or  imediately invoked function expression if we do not want it to be stored in a variable
print((lambda x:x*x*x) (5))
# here you returned a function and immediately called it
print("----------")
def evenOrOdd(x):
    if(x%2==0):
        return("even")
    else:
        return("odd")
print(evenOrOdd(7))
print(evenOrOdd(70))

parity=lambda x:"even" if x%2==0 else "odd"
print(parity(7))
print(parity(70))

print("----------")

def greaterOfTwo(x,y):
    if(x>y):
        return("x")
    elif(x==y):
        return("x=y")
    else:
        return("y")
    """ think of it as
    if(x>y):
        return("x")
    else:
        if(y==x):
            return("x=y")
        else:
            return("y")
    elif is another if else loop inside else
    """

print(greaterOfTwo(7,10))
print(greaterOfTwo(7,7))
print(greaterOfTwo(70,10))

greaterOfTwo2=lambda x,y:"x" if x>y else ("x=y" if x==y else "y")
print(greaterOfTwo2(7,10))
print(greaterOfTwo2(7,7))
print(greaterOfTwo2(70,10))