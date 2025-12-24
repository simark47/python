# https://www.codechef.com/problems/TRAPLOOP
t=int(input())
while(t>0):
    x=int(input())
    print(360//(180-(2*x)))
    t-=1