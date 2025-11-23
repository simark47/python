iphone={
    "color":"brown", 
    "model":"13 pro",
    "ratings":4.56, 
    "RAM":128
}
for i in iphone:
    print(i, iphone[i])
# i is by default keys

print(iphone.keys())
print(iphone.values())
print(iphone.items()) #list of tuples like zip

for i in iphone.items():
    print(i)
for i in iphone.items():
    print(i[0], i[1])