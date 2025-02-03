# if th traffic light is green print go
# if the traffic light is amber print slow down
# if the traffic light is red - print stop - end the loop

traffic_light = input('Choose a traffic light colour: ')
# The input function triggers to allow the user to enter a color
if traffic_light == 'red':
    print('Stop')
    # 'if' is a conditional statement used to execute a block of code if the condition evaluates to True
elif traffic_light == 'amber':
    print('Slow down')
elif traffic_light == 'green':
    print('Go')
