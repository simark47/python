x=50
def z():
    
    x=200
    def h():
        x=45
        def g():
            nonlocal x
            x=1
            print(x) #uses closely enclosed x and updates to 1
        g()
        print(x)  # will print 1 too 
        
    h()
    print(x) # will print 200

z()
print(x) # will print 50 because its global


print("----------")
x=50
def z():
    
    x=200
    def h():
        x=45
        def g():
            global x
            x=1
            print(x) #uses global x and updates to 1
        g()
        print(x)  # will print 45
        
    h()
    print(x) # will print 200

z()
print(x) # will print 1 because its global
