 # are we allowed to raise our own errors?
 # yes
 # like in an atm if we try to withdraw a greater amount than bank  balance
balance=5000
withdrawal=int(input("Enter the amount you want to withdraw: "))
if (withdrawal>balance):
     raise ValueError("Withdrawal cannot be greater than balance")
else:
     balance-=withdrawal
     print("Withdrawal is done.\navailable balance")
     print(balance)
