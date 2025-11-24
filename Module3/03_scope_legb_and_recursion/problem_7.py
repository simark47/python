"""
https://www.geeksforgeeks.org/problems/juggler-sequence3930/1?sortBy=submissions&category%5B%5D=Recursion&page=1&difficulty%5B%5D=-1
"""

class Solution:
    
    def jugglerSequence(self, n):
        a=[]
        a.append(int(n))
        while n!=1:
            if(n%2==0):
              n=int(n ** 0.5) 
            else:
              n=int(n ** 1.5)
            a.append((int(n)))
            
        
        return(a)

obj = Solution()

# Print the sequence
print(obj.jugglerSequence(9))
