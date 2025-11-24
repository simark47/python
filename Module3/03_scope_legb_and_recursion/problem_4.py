"""
https://leetcode.com/problems/jewels-and-stones/description/
"""

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
       
            
        count=0
        for i in stones:
            if i in jewels:
                count+=1
        return count

#try
obj=Solution()
print(obj.numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))