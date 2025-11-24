"""
https://leetcode.com/problems/defanging-an-ip-address/description/
"""

def defangIPaddr(address: str) -> str:
    a=address.split(".")
    b=("[.]").join(a)
    return b

#try:
print(defangIPaddr(address="100.100.100.100"))