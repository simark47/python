# multiline string
a="""
20
"""
print(a)

#concatenation
b="simar"
c='preet kaur'
print(b+c)
#duplication
print(b*3)
# slicing
print(b[3])
print(c[1:7]) #start, stop-1
print(c[1:11:2])
print(c[8:1:-1])
print(b[::-1]) #reverse
# return index
print(b.find("a"))
print(b.index("a"))
print(b.find("b")) # find returns-1 
print(b.index("b"))# causes error