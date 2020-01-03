import math
temp = eval(input('Enter the Temperature in C '))
wind = eval(input('Enter the Wind Speed in mps '))
if temp < 10 and wind > 0.000833:
    wci = (10 * math.sqrt(wind) - wind + 10.5) * (33 - temp)
    print('Wind Speed Index is ', round(wci, 3))
else:
    print('Invalid Input')