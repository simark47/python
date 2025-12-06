"""
https://codeforces.com/problemset/problem/445/A
"""
n,m=map(int, input().split())
a=[]
for _ in range (n):
    b=list(input())
    a.append(b)

for i in range(n):
    for j in range(m):
        if(a[i][j]=="."):
            if((i+j)%2==0):
                a[i][j]="B"
            else:
                a[i][j]="W"

for i in a:
    print("".join(i))




