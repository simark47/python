"""
https://codeforces.com/problemset/problem/136/A
"""
n=int(input())
li=list(map(int, input().split()))


for i in range(1,n+1):
    print(li.index(i)+1,end=(" "))


# or
# n=int(input())
# li=list(map(int, input().split()))
# c={}
# for i, a in enumerate(li):
#    c[a]=i+1
# for j in range(1,n+1):
#    print(c[j], end=" ")
   
   