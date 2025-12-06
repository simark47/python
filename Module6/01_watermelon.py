"""
https://codeforces.com/contest/4/problem/A
"""
w=int(input())
if(w%2!=0):
    print("NO")
elif(w==2):
    print("NO")
else:
    print("YES")

# "logic:
"""
w=even_1+even_2

any odd number can not be split into 2 evens
so odds are a no

2 has only possible splits 1,1, or 2 ,0 
former is odd and later is not allowed
so 2 is also no

else all other numbers which are even and gt 2 are Yes


"""