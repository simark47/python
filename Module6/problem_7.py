# https://www.codechef.com/problems/CFPRIME
t=int(input())
for _ in range (t):
    n=int(input())
    a=list(map(int, input().split()))
    count_sum=0
    for i in range(n):
        count=1
        while a[i]>9:
            count+=1
            a[i]//=10
        count_sum+=count
    if count_sum<=2:
        print("No")
    else:
        prime=True
        for i in range(2,count_sum):
            if(count_sum%i==0):
                prime=False
                break
            
    
        if(prime):
            print("Yes")
        else:
            print("No")
    print()