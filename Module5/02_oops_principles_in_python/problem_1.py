"""
https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true
"""
t=int(input())
for _ in range(t):
    a, b=input().split()
    try:
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)

# try
"""

3
1 0
2 $
3 1
"""