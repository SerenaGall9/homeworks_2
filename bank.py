# from itertools import count
import sys
import getpass

bank_pin = "1111"

count = 0
while count < 3:
    supplied_pin = getpass.getpass("Enter your PIN: ",None)
    if supplied_pin == bank_pin:
         print("Successful PIN")
         break
    else:
     count += 1
     print("PIN incorrect,Try again")
print("You've used too many attempts")





