# https://codeforces.com/problemset/problem/71/A

t=int(input())
for _ in range(t):
    stri=input()
    if(len(stri)>10):
        stri=stri[0]+str(len(stri)-2)+stri[-1]
    print(stri)