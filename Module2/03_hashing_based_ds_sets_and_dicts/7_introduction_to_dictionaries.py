a={}
print(a)
# dictionary is also hashing based ds, but are a step ahead of sets because they store key value pairs of objects
iphone={
    "color":"brown", 
    "model":"13 pro",
    "ratings":4.56, 
    "RAM":128
}
print(iphone, type(iphone))
print(iphone["model"])
# hashing is on keys only so you can not find the key using a value like print(iphone[4.56])
#slots store keys
print(iphone.get("model"))
print("----------")

#difference is when key does not exist
# print(iphone["charger"]) //error 
print(iphone.get("charger")) #returns None

# keys should be of the type hashable - like strings, numbers, tuples
# not unhashable like lists, sets or dictionaries [1,2,3]:"nana" not allowed
# dictionaries are unhashable and mutable
# print(hash(a)) TypeError: unhashable type: 'dict'
# values can be anything even another dictionary
# duplicates are replaced by the last value and dictionary is ordered


iphone={
    "color":"brown", 
    "model":"13 pro",
    "ratings":4.56, 
    "RAM":128,
    True:1,
    1:"nani", 
    ("a", "b"):"hyphen", 
    "model":"14 pro", #replaced

}
print(iphone)