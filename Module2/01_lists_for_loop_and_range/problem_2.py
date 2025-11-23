'''
https://www.hackerrank.com/challenges/compare-the-triplets/problem?isFullScreen=true
'''
def compareTriplets(a, b):
    al=0
    bob=0
    for i in range(len(a)):
        if(a[i]>b[i]):
            al+=1
        elif (a[i]<b[i]):
            bob+=1
            


    return [al, bob]

#try
a=[5, 6, 70]
b=[3, 6 ,10]
print(compareTriplets(a,b))