import math
x = eval(input('Enter any number '))
sol1 = (2/(math.sin(x))) - (math.cos(x)/math.sin(x))
sol2 = math.sin(x) / math.cos(x)
print(sol1 , " = " , sol2, " Hence Proved!")