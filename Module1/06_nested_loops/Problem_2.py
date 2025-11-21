"""
https://www.hackerrank.com/challenges/30-loops/problem?isFullScreen=true
"""
if __name__ == '__main__':
    n = int(input().strip())
    i=1
    while i<=10:
        print(n, "x", i, "=", n*i)
        i+=1