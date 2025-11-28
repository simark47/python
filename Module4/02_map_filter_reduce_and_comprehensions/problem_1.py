"""
https://www.hackerrank.com/challenges/map-and-lambda-expression/problem?isFullScreen=true

"""
cube = lambda x:x*x*x
def fibonaci(n):
    def fib(i):
        if i<=1:
            return i
        return fib(i-1)+fib(i-2)
    return list(map(fib, range(n)))
    


# or
def fibonaci2(n):
    # return a list of fibonacci numbers
    if(n==0):
        return []
    if(n==1):
        return [0]
    if(n==2):
        return [0,1]
    first=0
    second=1
    a=[0,1]
    for _ in range(3,n+1):
        third=first+second
        a.append(third)
        first=second
        second=third
    
    return a

# or
def fibonaci3(n):
    def fib(i):
        if i<=1:
            return i
        return fib(i-1)+fib(i-2)
    a=[fib(i) for i in range(0,n)]
    return a


print(list(map(cube, fibonaci(5))))
print(list(map(cube, fibonaci2(5))))
print(list(map(cube, fibonaci3(5))))
