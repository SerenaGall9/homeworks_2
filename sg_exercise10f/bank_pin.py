import getpass
# we imported this module to hide the input when inserting the PIN
correct_pin = 9999
#  variable 'correct pin' is the value assigned for the correct pin and it is
attempt = 3
# variable 'attempt' is the value assigned to the n of attempt that user can try to enter the pin
# while attempt > 0:
# def getpass(input)

while attempt > 0 :
    # while loop works when we don't know how many times we want to repeat the condition so it continues until the condition is met
    (supplied_pin) = getpass.getpass("Please enter your pin: ", None)
    #as expected we get "GetPassWarning" as pycharm doesn't handle secure password input correctly
    if correct_pin ==  int(supplied_pin) :
          # made the value supplied_pin an integer to be able to be able to run the conditional
         # if is expected the statement is true
        print("Correct pin, welcome")
        break
 #        exits the loop
    else:
     attempt -= 1
   # else expect that is statement is false.
    print('incorrect pin, try again')
if attempt == 0 :
    print('Too many attempts access blocked')

