"""
https://codeforces.com/problemset/problem/1703/B
"""
# t=int(input())

# for _ in range (t):
#     a=[]
#     count=0
#     n=int(input())
#     li=list(input())
#     for i in li:
#         if i in a:
#             count+=1
#         else:
#             a.append(i)
#             count+=2
#     print(count)

t=int(input())

for _ in range (t):
    a=[]

    n=int(input())
    s=input()
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=2
            
    print(sum(d.values()))
