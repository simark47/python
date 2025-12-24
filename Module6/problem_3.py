# https://www.codechef.com/problems/CHN15A

t=int(input())
for _ in range(t):
    n, k=map(int, input().split())
    
    li=map(int, input().split())
    count=0
    for i in li:
        if ((i+k)%7==0):
            count+=1
            
        
    print(count)
        