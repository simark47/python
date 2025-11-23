'''
https://www.hackerrank.com/challenges/simple-array-sum/problem?isFullScreen=true
'''

def simpleArraySum(ar):
    sum=0
    for i in ar:
        sum+=i
    return(sum)




#try
arr=[1,2,3,4,5,0,8,6,120]
print(simpleArraySum(arr))