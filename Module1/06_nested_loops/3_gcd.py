# GCD= Greatest common divisor:
'''
6 and 18 have many divisors like
6= 1,2,3,6
18= 1,2,3,6,9,18
common among them are 1,2,3,6
greatest is 6

LOGIC:
start from 1, loop till the smallest of two numbers, find the greatest that divides both
or 
start from lowest number of both till it reaches 1, find the first largest number that divides both the numbers and break loop

'''
m=int(input())
n=int(input())
mini=min(m,n)
i=1
gcd=i
while i<=mini:
    if(m%i==0 and n%i==0):
        gcd=i
    i+=1
print(gcd)

#way2 using break
mini=min(m,n)

gcd=1
while mini>=1:
    if(m%mini==0 and n%mini==0):
        gcd=mini
        break
    mini-=1
print(gcd)