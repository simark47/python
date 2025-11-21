#lcm = least common multiple

'''
like 6,18 have 18
6,11 have 66
lcm is the least number which is divisble by both
logic:
it must start from the greatest of two and go till product of both, if found, break
'''
print("enter both nums")
n=int(input())
m=int(input())

maxi=max(m,n)
prod=n*m
lcm=maxi
while lcm<=prod:
    if(lcm%m==0 and lcm%n==0):
        print(lcm)
        break

    lcm+=1
