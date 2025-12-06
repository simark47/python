"""
https://codeforces.com/problemset/problem/144/A
"""

n=int(input())
li= list(map(int, input().split()))

maxi=max(li)

mini=min(li)

max_idx=li.index(maxi)
min_idx=len(li)-1-li[::-1].index(mini)
ans=max_idx+len(li)-1-min_idx
if(min_idx<max_idx):
    ans-=1
print(ans)