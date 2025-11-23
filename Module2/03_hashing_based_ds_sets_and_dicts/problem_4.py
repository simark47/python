"""
https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true
"""
n=int(input())
li=list(map(int, input().split()))
s=set(li)

sum_is=sum(li) 
sum_should=sum(s)*n
print(int((sum_should-sum_is)/(n-1)))


''' try
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2

'''