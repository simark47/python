"""
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
"""
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lar=-100
    seclar=-100
    for i in arr:
        if i>lar:
            seclar=lar
            lar=i
        elif i>seclar and i<lar:
            seclar=i
    print(seclar)

#try 
"""
5
2 3 6 6 5

"""

