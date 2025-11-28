"""
https://www.hackerrank.com/challenges/any-or-all/problem?isFullScreen=true
"""
n=int(input())
li=list(map(int, input().split()))[:n]
t=all(map(lambda x: x>0,li ))
pal=lambda n:True  if n<10 else(True if((str(n)[::-1])==str(n)) else False)
u=any(map(pal, li))
print(u and t)
# or
n=int(input())
li=list(map(int, input().split()))[:n]
print(all(map(lambda x:x>0, li)) and any(map((lambda n:str(n)[::-1]==str(n)), li)))

# input 
"""
5
12 9 61 5 14  

5
12 9 61 5 14 
"""