# whenever we return  some integer , it will print non stop
# like printing odd integers till n
# what if we want to generate the next number whenever we call function?
#memory will not be used until next is called unlike storing in a list
def generateOddNums(limit):
    i=1
    while i<=limit:
        yield i #whenever function is called, a number is returned and execution is stopped here
        i+=2 #next execution starts here
    
a=generateOddNums(7)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a)) #StopIteration

    