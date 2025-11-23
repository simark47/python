"""
https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true

"""
def diagonalDifference(arr):
    diag_sum1=0
    diag_sum2=0
    for i in range(len(arr)):
        diag_sum1+=arr[i][i]
    for i in range(len(arr)):#range starts from 0
        diag_sum2+=arr[i][len(arr)-i-1] 
    diff=diag_sum1-diag_sum2
    return(abs(diff))



#try
arr=[[1, 2, 3], 
[4, 5, 6],
[9 ,8, 9 ] ]
print(diagonalDifference(arr))

