"""
https://www.hackerrank.com/challenges/30-review-loop/problem?isFullScreen=true
"""
n=int(input())
while n>0:
    
    string=str(input())
    i=0
    streve=""
    strodd=""
    while i< len(string):
        if i%2==0:
            streve+=string[i]
        else:
            strodd+=string[i]
        i+=1
        
    print(streve, strodd)
    n-=1