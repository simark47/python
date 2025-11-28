"""
https://www.hackerrank.com/challenges/reduce-function/problem?isFullScreen=true
"""
from fractions import Fraction
from functools import reduce

def product(fracs):
    prodn=1
    prodd=1
    for i  in range(len(fracs)):
        a,b=fracs[i].numerator, fracs[i].denominator
        prodn*=a
        prodd*=b
    t=Fraction(prodn, prodd) 
    
    return t.numerator, t.denominator

# or

def product(fracs):
    t = reduce(lambda x, y: x * y, fracs)
    return t.numerator, t.denominator
# --------------

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)

# ---
'''
3
1 2
3 4
10 6
'''