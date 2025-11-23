s={"apple", "banana", "grape", "orange", "banana", False, 1.2}
# set is hashing based ds
# does not maintain order as slot value can be anywhere
# duplicates not allowed
print(s, type(s))
print(len(s))

# traversal
for i in s:
    print(i , end=" ")
print("\n----------")
if "apple" in s:
    print("present")

# tuple is allowed as its hashable
s={"apple", "banana", "grape", "orange", "banana", False, 1.2, (4,6,80)}
print(s, type(s))

# list is not allowed as its unhashable
s={"apple", "banana", "grape", "orange", "banana", False, 1.2, [4,6,80]}
print(s, type(s))