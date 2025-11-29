# like you are in an atm and you put your diving license in the machine
# machine recognises that it is an error and does not give you cash
# but lets say you inserted the correct card but the wrong pin
# this is an exception that has to be gracefully handled
# put it in try catch blocks
classResults={
    "nimar":[10,20,10,20],
    "simar":[20,15,10,5],
    "jeet":[10,20,5],
    "geet":[] #did not appear in exams
}

# for i in classResults.values():
#     print(sum(i)/len(i))
# ZeroDivisionError: division by zero

for i in classResults.items():
    try:
        print(sum(i[1])/len(i[1]))
    except ZeroDivisionError:
        print(i[0], "did not give exams")
    finally:
        print("Finally always prints")

print("------")
for i in classResults.items():
    try:
        print(sum(i[2])/len(i[2]))
    except IndexError:
        print("Index out of range")
    finally:
        print("Finally always prints")