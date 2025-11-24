def displayMarks(name, marks):
    sum=0
    for i in marks:
        sum+=i
    print(f"Hi, {name}.Your marks are {sum}")

displayMarks("Simar", [40,60,50,80])
print("----------")
# What if we have arbitrary number of arguments and we need it to be in a list

# displayMarks("Simar", 40,60,50,80,60,40)  throws TypeError: displayMarks() takes 2 positional arguments but 7 were given

# use star before that parameter name to convert to a tuple
def displayMarks2(name, *args):
    print(args, type(args))
    sum=0
    for i in args:
        sum+=i
    print(f"Hi, {name}.Your marks are {sum}")

displayMarks2("Simar", 40,60,50,80,60,40)
print("----------")
# there is similar way for it to be done as keywords
# use ** star before that parameter name to convert to a dictionary with name value pairs

def displayMarks3(name, **kwargs):
    print(kwargs, type(kwargs))
    sum=0
    for i in kwargs.values():
        sum+=i
    print(f"Hi, {name}.Your marks are {sum}")

displayMarks3("Simar", english=40,hindi=60,maths=50,punjabi=80,history=60,sst=40)