# https://www.codechef.com/problems/EXOCODE7
n=int(input())
if(n<=50):
    bill=n*0.50
elif n>50 and n<=150:
    bill=(50*0.50)+((n-50)*0.75)
elif n>150 and n<=250:
    bill=(50*0.50)+(100*0.75)+((n-150)*1.20)
elif n>250:
    bill=(50*0.50)+(100*0.75)+(100*1.20)+((n-250)*1.50)
    
bill*=1.20
print(f"{bill:.2f}")