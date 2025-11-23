"""
https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
"""
if __name__ == '__main__':
    
    b=[]
    c=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        a=[name, score]
        b.append(a)
        c.append(score)

    
    low=float("inf")
    sec_low=float("inf")
    

    
    for i in c:
        if i<low:
            sec_low=low
            low=i
        elif i > low and i < sec_low:
            sec_low=i
            
    c=[]
    for i in range(len(b)):
        if b[i][1]==sec_low:
            c.append(b[i][0])
    c.sort()
    for i in c:
        print(i)

    
#try
"""
5
Harsh
20
Beria
20
Varun
19
Kakunami
19
Vikas
21
"""