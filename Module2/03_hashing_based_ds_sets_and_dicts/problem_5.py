"""
https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true
"""

a=set(list(map(int, input().split())))
n=int(input())
flag=True
for _ in range(n):
    b=set(list(map(int, input().split())))
    if(not(a>b)):
        flag=False
print(flag)


#try
'''
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12
'''