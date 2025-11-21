# if
a=20
b=10
if(a>b):
    print("a is greater than b")

# if- else
a=20
b=100
if(a>b):
    print("a is greater than b")
else:
    print("b is greater than a")

# if-elif- else
a=20
b=20
if(a>b):
    print("a is greater than b")
elif(a==b):
     print("a is equal to b")
else:
    print("b is greater than a")

#nested if else:
a=200
b=40
c=50
if(a>b):
    if(a>c):
        print("a is greatest of 3")
    else:
        print("c is greatest of 3")
else:
    if(b>c):
        print("b is greatest of 3")
    else:
        print("c is greatest of 3")


#calculator
print("Enter first integer")
x=int(input())
print("Enter operation")
o=input()
print("Enter second integer")
y=int(input())
if o=="+":
    print(x+y)
elif o=="-":
    print(x-y)
elif o=="*":
    print(x*y)  
elif o=="/":
    print(x/y)  
else:
    print("operation can not be performed")