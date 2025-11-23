"""
https://www.hackerrank.com/challenges/linkedin-practice-dictionaries-and-maps/problem?h_r=internal-search
"""
t=int(input())
dict={}
for _ in range(t):
    str=input().split()
    name=str[0]
    phone=str[1]
    dict[name]=phone
while(True):
    try:
        query=input()
        if query in dict.keys():
            print(query+ "="+dict[query])
        else:
            print("Not found")
    except EOFError:
        break
"""
try
3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry
    
    """