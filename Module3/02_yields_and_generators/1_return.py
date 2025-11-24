
def calculate_bill(amount, tax=18, tip=0):
    print(((amount*(100+tax))/100)+tip)

calculate_bill(2000,0,0)
#  calling this function, staight away prints the value-but we want to store it instead or do further processing then we may use return instead of print

def calculate_bill2(amount, tax=18, tip=0):
    return(((amount*(100+tax))/100)+tip)

a=calculate_bill2(2000,0,0)
#  nothing is printed until we explictly say so
print(a)
print(a+20) #this is not possible without return
