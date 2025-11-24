# def f():
#     f()
# f()
# function calling itself is recursion
def printnum(l,r):
    if l>r:
        return
    print(l)
    printnum(l+1,r)
printnum(1,10)
print("----------")
# reverse
def printnum(l,r):
    if l>r:
        return
    
    printnum(l+1,r)
    print(l)
printnum(1,10)