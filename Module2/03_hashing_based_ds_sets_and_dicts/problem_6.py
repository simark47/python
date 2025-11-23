"""
https://www.hackerrank.com/challenges/electronics-shop/problem?isFullScreen=true
"""
def getMoneySpent(keyboards, drives, b):
    #   
    # Write your code here.
   
    max_spent=-1
    for i in keyboards:
        for j in drives:
            
            if(i+j)<=b and (i+j)>max_spent:
                    max_spent=i+j

    return max_spent

#try
keyboards=[3 ,1]
drives=[5, 2, 8]
b=10
print(getMoneySpent(keyboards, drives, b))