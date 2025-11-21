"""
https://www.hackerrank.com/challenges/30-binary-numbers/problem?isFullScreen=true
"""
if __name__ == '__main__':
    n = int(input().strip())
    bina=""
    while n>0:
        rem= n%2
        bina=str(rem)+bina
        n//=2
    # print(bina) check if binary is correct
    
    count=0
    maxCount=0
    for i in bina:
        if i=="1":
            count+=1
            if maxCount<count:
                maxCount=count
        else:
            count=0
    print(maxCount)
