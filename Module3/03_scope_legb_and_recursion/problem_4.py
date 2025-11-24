"""
https://leetcode.com/problems/jewels-and-stones/description/
"""

def numJewelsInStones( jewels: str, stones: str) -> int:
       
            
    count=0
    for i in stones:
        if i in jewels:
            count+=1
    return count

#try
print(numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))