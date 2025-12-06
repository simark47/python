"""
https://codeforces.com/problemset/problem/263/A    
"""
n=5
a=[]
for i in range(n):
    b=list(map(int, input().split()))
    a.append(b)
r=0
c=0

for i in range(n):
    for j in range(n):
        if(a[i][j]==1):        
            r=i+1
            c=j+1

print(abs(3-r)+abs(3-c))

"""or
n=5
a=[]
for i in range(n):
    b=list(map(int, input().split()))
    a.append(b)
r=0
c=0

for i,v in enumerate(a):
    for j,w in enumerate(v):
        if w==1:
            r=i+1
            c=j+1
count=0
def counting(x):
    global count
    while(x>3):
        x-=1
        
        count+=1
        
    while(x<3):
        x+=1
        count+=1
        
counting(r)
counting(c)
print(count)



"""