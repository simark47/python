y=200
x=1000
m=25
def z():
    y=15
    x=200
    def h():
        x=20
        print(m) #uses global m
        print(y) #uses enclosed y
        print(x) #uses local x
    h()

z()
# LEGB PRINCIPLE
# local scope> enclosed > global scope >builtins