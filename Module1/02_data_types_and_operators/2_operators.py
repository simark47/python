# arithmetic and assignment operators
a=30
b=8
print(a+b)

print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**2)

print("----------")
a+=2
print(a)
a-=2
print(a)
a*=2
print(a)
a//=2 #integer division
print(a)
a=30
a/=2.5 #returns float
a=int(a)
print(a)
a%=5
print(a)

#bitwise
'''
and &
or |
xor ^ same bits give 0 otherwise 1
x << y x * (2**y)
x >>y x /(2**y)

'''
x=5 #0101
y=3 #0011
print(x&y) #0001
print(x|y) #0111
print(x^y) #0110
print(2<<3)
print(56>>3)

#relational(comparision) and logical operators
print(x>y)
print(x>=y)
print(x<y)
print(x<=y)
print("abc"=="abc")
print("abs"!= "abc")

print(x>y or x==y)
print(x>y and x==y)
print(not(x>y))
