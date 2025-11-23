li=[1,2,3,4]

print(tuple(li))
print(set(li)) #should only have hashable items and not a list inside like li=[1,2,3,4, [4,5]]

tu=(5,6,7,8)
print(set(tu)) #should only have hashable items and not a list inside like tu=(5,6,7,8, [4,5])
print(list(tu))

se={9,10,11}
print(tuple(se))
print(list(se))
# all of them are possible

a=["simar", "preet", "kaur"]
st=(" ").join(a) #only string elements
print(st)
