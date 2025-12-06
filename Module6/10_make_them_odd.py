"""
https://codeforces.com/problemset/problem/1277/B
"""
t=int(input())
for i in range(t):
        
    n=int(input())
    s=list(map(int, input().split()))
    t=set()
    for i in s:
        while(i%2==0):
            t.add(i)
            i//=2

    print(len(t))




