name=["simar", "anchal", "naina", "rohit", "ashish"]
surname=["makkar", "singla", "gupta", "patekar", "solanki"]
for o in range(len(name)):
    print(name[o], surname[o])
# use zip to get a tuple of both elements
for i in zip(name, surname):
    print(i)
# elements:
for i in zip(name, surname):
    print(i[0], i[1])