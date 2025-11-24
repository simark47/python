# functions are used so to avoid repitition
# function decalaration:
# use def keyword function name(parameters)

def calculateBill(amount,tax,tip):
    print(((amount*(100+tax))/100)+tip)

# function calling: function name in camel case(arguments)
calculateBill(1000,18,10)
calculateBill(2000,20,10)