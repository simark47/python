s={"apple", "banana", "grape", "orange", "banana", False, 1.2}
s.add(5)
print(s)
s1={5,6,7}
s.update(s1)
print(s)

s.remove("apple")
print(s)
s.discard("banana")
print(s)

#difference between these two is when element is not present

s.discard("watermelon") #silent
print(s)
s.remove("watermelon") #throws error
print(s)