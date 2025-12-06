"""
https://codeforces.com/problemset/problem/918/B
"""
n,m=map(int, input().split())
ips_name={}
for _ in range(n):
    name, ip=input().split()

    ips_name[ip]=name

for _ in range(m):
    command, ips=input().split()
    ip=ips[:-1]
    print(command, ips, "#"+ips_name[ip])
