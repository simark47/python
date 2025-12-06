
"""
https://codeforces.com/contest/977/problem/A
"""

n, k =map(int,  input().split())
def sub(n):
    if n%10==0:
        n=n//10
    else:
        n-=1
    return n
for _ in range(k):
    n=sub(n)
print(n)
