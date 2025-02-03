# run as is then change j to 12
# use the debugger to show the i counter increasing
i = 1
# the value of i increases until the condition on the while statement is proven to be true ( i < 42)
j = 12
while i < 42:
    i = i * 2
    #  the value increases by multiples of two because that the condition set by the statement
    if i > j:
    # when the value of i is greater than j the 'while statement' is false and 'if statement' is true
        break
# the break interrupts the closest loop when the condition is met, in this case else : print ('print("Loop expired: ", i), it only runs when the if statement is false
# when i is greater than j skip the else condition and print the final value ( condition is met)
# break is sometimes associated with the Continue statement which skips certain iterations under certain conditions in a while or for loop
else:
    print("Loop expired: ", i)

print("Final value: ", i)
