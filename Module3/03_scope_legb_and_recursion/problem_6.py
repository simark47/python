"""
https://www.geeksforgeeks.org/problems/print-1-to-n-without-using-loops-1587115620/1?page=1&sortBy=submissions&category%5B%5D=Recursion

"""
class Solution:    
    def printNos(self,n):
        #Code here
        
        if(n>=1):
            self.printNos(n-1)
            print(n, end=" ")

#try
obj = Solution()
obj.printNos(10)
