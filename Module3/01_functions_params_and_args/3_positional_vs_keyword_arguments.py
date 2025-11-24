def calculateBill(amount,tax=18,tip=0):
    print(((amount*(100+tax))/100)+tip)

calculateBill(1000,18,10)  #positional arguments

calculateBill(amount=2000, tax=5, tip=0) #keyword arguments

# calculateBill(2000, 0,tax=0) if you use mix , order matters
# calculateBill(2000,tax=0, 0) not allowed as keyword arguments must be at the end


calculateBill(2000, 0,tip=0) #allowed

def calculateBill(amount,tax=18,/, tip=0):
    print(((amount*(100+tax))/100)+tip)

# before/ all args will be positional only
# calculateBill(2000, tax=5,tip=0) gives error got some positional-only arguments passed as keyword arguments:
calculateBill(2000, 0,0) #allowed 
calculateBill(2000, 0,tip=0) #allowed

print("----------")

def calculateBill(amount,*, tax=18, tip=0):
    print(((amount*(100+tax))/100)+tip)
# aftr * all args will be positional only
# calculateBill(2000, 0,0) gives error  calculateBill() takes 1 positional argument but 3 were given

# calculateBill(2000, 0,tip=0)  calculateBill() takes 1 positional argument but 2 positional arguments (and 1 keyword-only argument) were given

calculateBill(2000,tax= 0,tip=0) #allowed

print("----------")

def calculateBill(tax,/, *, amount, tip=0): #keyword will be towards the end
    print(((amount*(100+tax))/100)+tip)

calculateBill(20, amount=5000,tip=0) #allowed