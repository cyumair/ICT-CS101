print('This program Calculates Factorial of a Number')
def factorial(n):
    if n==0:
        return 1
    else:
        return factorial(n-1)*n
while True:
    n = int(input('please enter any number ...'))
    print('factorial of number is:', factorial(n))    
