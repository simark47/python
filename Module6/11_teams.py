# https://codeforces.com/problemset/problem/231/A

n=int(input())
count=0
for _ in range(n):
    li=map(int, input().split())
    if(sum(li)>=2):
        count+=1
print(count)

