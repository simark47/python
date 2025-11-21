i=1
print("Enter number of testcase")
n=int(input())
while i<=n:
    print("Enter testcase #",i)
    m=int(input())
    j=2
    flag=True
    while j<m:
        if(m%j==0):
            flag=False
            break

        j+=1
    if(flag):
        print(m,"is prime")
    else:
        print(m,"is not prime")

    i+=1