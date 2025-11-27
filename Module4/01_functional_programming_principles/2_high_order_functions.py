# Higher order functions are functions which take another function as a parameter and use them later in code execution
# lets have a function that sums a list of numbers and passes that to its internal function for product of digits
#  lets write the internal function first
def prodOfDig(n):
    print(n)
    prod=1
    while n>0:
        ld=n%10
        prod=prod*ld
        n=n//10
    return prod
# now lets write the higher order function that sums up a list and passes it to another function
def sumOfList(list, func):
    a=sum(list)
    print(func, type(func)) #function type
    return func(a) #here we are returning a function from a function

# now lets call it
print(sumOfList([102,27,35,40,100,20],prodOfDig))