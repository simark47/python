n=int(input())
sum=0
copy=n
while copy>0:
    ld=copy%10
    sum+=ld
    copy//=10
print(sum)

# count number of digits 
count=0
while n>0:
    n//=10
    count+=1
print(count)
