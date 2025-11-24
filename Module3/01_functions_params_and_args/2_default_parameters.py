def calculateBill(amount,tax=18,tip=0):
    print(((amount*(100+tax))/100)+tip)
# non default arguments follow default ones
# if you want to give default value- it must be at the end parameters
calculateBill(1000,18,10)
calculateBill(1000,18)
calculateBill(1000)