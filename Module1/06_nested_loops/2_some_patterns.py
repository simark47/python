
print("enter number of rows and columns")

#square pattern n=3

'''
* * * 
* * * 
* * *
'''
print("square pattern")
n= int(input())
i=1
while i<=n:
    j=1
    
    while j<=n:
        print("*", end=" ")
        j+=1
    print()
    i+=1

#star pattern n=4

'''
* 
* *  
* * *
* * * *
'''

print("star pattern")
i=1
while i<=n:
    j=1
    
    while j<=i:
        print("*", end=" ")
        j+=1
    print()
    i+=1

#new 123 pattern n=3
'''
1 
xxxxxxx
1
1 2
xxxxxxx
1
1 2
1 2 3
xxxxxxx
'''



print("enter the number m")

m=int(input())
i=1
while(i<=m):
    j=1
    while j<=i:
        k=1
        while k<=j:
            print(k, end=" ")
            k+=1
        print()
        j+=1
    print("xxxxxxx")
    i+=1



#new 12321 pattern n=5
"""
1 
1 2 1
1 2 3 2 1
1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
"""    
print("enter the number m")

m=int(input())
i=1
while i<=m:
    j=1
    while j<i:
                      
            print(j,end=" ")
            j+=1
            
    while j>=1:
            print(j,end=" ")
            j-=1
        
    print()
    i+=1


#diamond pattern n=5
'''

    * 
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
'''    
print("enter the number m")

m=int(input())
i=1
while i<=m:
    j=1
    while j<=m-i:
        print(" ", end="")
        j+=1
    k=1
    while k<=i:
        print("*", end=" ")
        k+=1
    print()
    i+=1
    
i=m-1
while i>=1:
    j=1
    while j<=m-i:
        print(" ", end="")
        j+=1
    k=1
    while k<=i:
        print("*", end=" ")
        k+=1
    print()
    i-=1


        
        


