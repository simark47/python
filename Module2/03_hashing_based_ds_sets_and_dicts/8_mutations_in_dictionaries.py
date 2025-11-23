iphone={
    "color":"brown", 
    "model":"13 pro",
    "ratings":4.56, 
    "RAM":128
}
iphone["color"]="pink" #update
print(iphone)   

# if the key is not present it will create a new one
iphone["price"]=750000 #add
print(iphone)   

# remove
iphone.pop("model")
print(iphone)   

iphone.popitem()
print(iphone)   

iphone.clear()
print(iphone)   