"""
https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true
"""


def miniMaxSum(arr):
    maxi=max(arr)
    mini=min(arr)
    sumofarr=sum(arr)
    minisum=sumofarr-maxi
    maxisum=sumofarr-mini
    print(minisum, maxisum)

#try
# 1 2 3 4 5

arr = list(map(int, input().rstrip().split()))

miniMaxSum(arr)