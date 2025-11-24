"""
https://leetcode.com/problems/defanging-an-ip-address/description/
"""

class Solution:
    def defangIPaddr(self, address: str) -> str:
        a=address.split(".")
        b=("[.]").join(a)
        return b

#try:
obj=Solution()
print(obj.defangIPaddr(address="100.100.100.100"))
