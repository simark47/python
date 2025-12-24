# https://www.codechef.com/problems/CMED01

# cook your dish here
n=int(input())
sum_even=0
odd_sum=0
j =list(map(int, input().split()))
for i in range(0,n):
   
    if(i%2==0):
        sum_even+=j[i]
    else:
        odd_sum+=j[i]
    
max_coins = 2 * min(sum_even, odd_sum)
print(max_coins)