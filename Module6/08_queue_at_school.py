"""
https://codeforces.com/problemset/problem/266/B
"""
n,t=map(int, input().split())

a=list(input())

while t>0:
    i=0
    while(i<n-1):
       
        if (a[i]=="B" and a[i+1]=="G"):
            a[i+1], a[i]= a[i],a[i+1]
            i+=1
        i+=1


    t-=1

print("".join(a))