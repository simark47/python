def f():
    x=200
f()
# print(x) this throws error as x is declared out of global scope and is in function scope
x=200
def y():
    print(x) #uses globally declared x

y()

x=200
def z():
    x=15

    print(x) #uses local x

z()
# local scope>global scope