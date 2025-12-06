"""
https://codeforces.com/problemset/problem/69/A
"""
t=int(input())
ans=[0,0,0]
for _ in range(t):
    x,y,z=map(int, input().split())
    ans[0]+=x
    ans[1]+=y
    ans[2]+=z
if(ans==[0,0,0]):
    print("YES")
else:
    print("NO")



"""
logic:
any force being applied will be nullified to 0 if product is in equiliibrium
"""