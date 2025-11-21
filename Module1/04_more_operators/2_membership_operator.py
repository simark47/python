#membership operator in, not in 
s1="hello, today is such a good day"
if("good" in s1):
    print("good found at index:", s1.find("good"), "in", s1)
else:
    print("not found")
if("dood" not in s1):
    print("dood not found in", s1)

#calculator using single line input
print("------------\nenter operators and oeration in a single line")
x=input()
if "+" in x:
    idx=x.find("+")
    op="+"
elif "-" in x:
    idx=x.find("-")
    op="-"
elif "*" in x:
    idx=x.find("*")
    op="*"
elif "/" in x:
    idx=x.find("/")
    op="/"
else:
    print("operation can not be performed")
a=int(x[:idx])
b=int(x[idx+1:])
if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op=="*":
    print(a*b)  
elif op=="/":
    print(a/b)  
else:
    print("operation can not be performed")


# or way 2:
operators=["+","-","/","*"]
operator="none"
for op in operators:
    idx= x.find(op)
    if idx>-1:
        operator=op
        break
a=int(x[:idx])
b=int(x[idx+1:])
if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op=="*":
    print(a*b)  
elif op=="/":
    print(a/b)  
else:
    print("operation can not be performed")