"""
https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true
"""
# t=int(input())
# for i in range(t):
#     n= int(input())
#     l=input().split()
#     for i in range(n):
#         l[i]=int(l[i])
#     s=set(l)
#     m= int(input())
#     o=input().split()
#     for i in range(m):
#         o[i]=int(o[i])
#     t=set(o)
#     if s<t:
#         print("True")
#     else:
#         print("False")



# or
t=int(input())
for i in range(t):
    n=int(input())
    a=set(list(map(int, input().split()))[:n])
    m=int(input())
    b=set(list(map(int, input().split()))[:m])
    print(a.issubset(b))

#try
'''
3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2

'''

