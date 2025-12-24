# https://www.codechef.com/problems/HS08TEST
input=  input().split()
x=int(input[0])
y=float(input[1])
if(x%5==0 and x+0.50<=y):
    print(f"{y-x-0.50:.2f}")
else:
    print(f"{y:.2f}")