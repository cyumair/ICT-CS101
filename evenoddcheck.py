def evenodd(num1, num2):
    if num1 % 2 == 0:
        n1 =  True
    else:
        n1 = False
    if num2 % 2 == 0:
        n2 = True
    else:
        n2 = False
    return n1, n2

num1 = int(input('Enter first number'))
num2 = int(input('Enter second number'))
n1 , n2 = evenodd(num1, num2)
if n1:
    if n2:
        print('BOth numbers are even')
    else:
        print(num1, ' is even and ', num2, ' is odd')
else:
    if n2:
        print(num1, ' is odd and ', num2, ' is even' )
    else:
        print(' both numbers are odd')