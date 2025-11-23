#reverse
list=[5,6,8,4,2,6,7]
n=len(list)

first=0
last=n-1
while first<last:
    list[first],list[last] =list[last] , list[first]
    first+=1
    last-=1
    
print(list)
# or 
list=[5,6,8,4]
list.reverse()
print(list)

# sort
list=[5,6,8,4,2,6,7]
list.sort()
print(list)
list.sort(reverse=True) #descending
print(list)
list=[5,6,8,4,2,6,"apple", "mango"]

# list.sort() wont work here because of a mixed list

list=[5,6,8,4,2,6,7]
#if you want to save sorted list in another list
l2=sorted(list)

print(l2)