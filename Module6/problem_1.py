# https://www.hackerrank.com/challenges/halloween-sale/problem?isFullScreen=true


def howManyGames(p, d, m, s):
    # Return the number of games you can buy
     count=0
     a=[]
     while p<=s:
       s-=p
       count+=1
       p=max(m, p-d)
   
     return(count)


# try  
p, d, m, s=map(int, input().split())    
print(howManyGames(p,d,m,s))

# 100 19 1 180