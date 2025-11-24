"""
https://www.geeksforgeeks.org/problems/gf-series3535/1?sortBy=submissions&category%5B%5D=Recursion&page=1&difficulty%5B%5D=-1
"""

class Solution:
    def gfSeries(self, N : int) -> None:
        # code here
        first=0
        second=1
        a=[0,1]
        
        
    
        for i in range(2,N):
            
            a.append(a[i-2]**2-a[i-1])
        
        
        for i in a:
            print(i, end=(" "))
        print() 
    
            
#try:
obj=Solution()
obj.gfSeries(N= 6)