#FUNCTION PROGRAMMING FOR BULIDING A SIMPLE CALCULATOR WITHOUT GRAPHICAL USER INTERFACE
#SUM FUNCTION
def sum():
    print('Sum Calculator')
    n1 = float(input('Enter First Number: '))
    n2 = float(input('Enter Second Number: '))
    total = n1 + n2
    print('sum =',total)
    while True:
        n3 = input('(type b to exit and r to reset) ' + str(total) + ' + ' )
        if n3 == 'r':
              sum()  
        elif n3 == 'b':
              calculator()
        else :
            try:
                total = total + float(n3)
                print(total)
            except:
                print('Error: Please Enter Valid Inputs')
                sum()
                
#SUBTRACTION FUNCTION
def subtract():
    print('Subtraction Calculator')
    n1 = float(input('Enter First Number: '))
    n2 = float(input('Enter Second Number: '))
    total = n1 - n2
    print('Answer =',total)
    while True:
        n3 = input('(type b to exit and r to reset) ' + str(total) + ' - ' )
        if n3 == 'r':
              subtract()  
        elif n3 == 'b':
              calculator()
        else :
            try:
                total = total - float(n3)
                print(total)
            except:
                print('Error: Please Enter Valid Inputs')
                subtract()
                
#MULTIPLICATION FUNCTION            
def multiply():
    print('Multiplication Calculator')
    n1 = float(input('Enter First Number: '))
    n2 = float(input('Enter Second Number: '))
    total = n1 * n2
    print('Answer =',total)
    while True:
        n3 = input('(type b to exit and r to reset) ' + str(total) + ' * ' )
        if n3 == 'r':
              multiply()  
        elif n3 == 'b':
              calculator()
        else :
            try:
                total = total * float(n3)
                print(total)
            except:
                print('Error: Please Enter Valid Inputs')
                multiply()
                
#DIVISION FUNCTION
def divide():
    print('Division Calculator(b to exit)')
    n1 = input('Enter First Number: ')
    if n1 == 'b':
        calculator()
    else:
        try:     
            n2 = float(input('Enter Second Number: '))
            total = float(n1) / n2
            print('Answer =',total)
            divide()
        except:
            print('Error: Please Enter Valid Inputs')
            divide()
            
#REMAINDER FUNCTION
def remainder():
    print('Remainder Calculator(b to exit)')
    n1 = input('Enter First Number: ')
    if n1 == 'b':
        calculator()
    else:
        try:
            n2 = float(input('Enter Second Number: '))
            total = float(n1) % n2
            print('Answer =',total)
            remainder()
        except:
            print('Error: Please Enter Valid Inputs')
            remainder()
            
#POWER FUNCTION
def power():
    print('Power Calulator(Type b to exit)')
    n1 = input('Enter Number: ')
    if n1 == 'b' :
        calculator()
    else:
        try:
            n2 = int(input('Power: '))
            total = float(n1) * n2
            print('Answer =', total)
            power()
        except:
            print('Error: Please Enter Valid Inputs')
            power()
#ROOT FUNTION
def root():
    print('Root Calulator(Type b to exit)')
    n1 = input('Enter Number: ')
    if n1 == 'b' :
        calculator()
    else:
        try:
            n2 = int(input('Root: '))
            for guess in range(int(n1)+1):
                check = n2 ** guess
                if check >= abs(int(n1)):
                    break
            if check != int(n1):
                print(str(n2) + ' root of the Number doesnot Exist')
                root()
            elif check == int(n1):
                print(str(n2) +' root of number is: ', guess)
                root()
        except:
            print('Error: Please Enter Valid Inputs')
            root()
         
#FACTORIAL FUNTION
def factorial():
    print('Factorial Calculator(b to exit)')
    n = input('Enter Your Number: ')
    def fact(n):
        if n == 0:
            return 1
        else :
            return fact(n-1)*n
    if n == 'b':
        calculator()
    else:
        try:
            print('Answer =', fact(int(n)))
            factorial()
        except:
            print('Error: Please Enter Valid Input')
            factorial()
    
#MAIN FUNCTION              
def calculator():
    print('For Sum Press 1 \nFor Subtraction Press 2 \nFor Multiplication Press 3 \nFor Division Press 4 \nFor Remainder Press 5 \nFor Power Press 6 \nFor Root Press 7 \nFor Factorail Press 8')
    type = (input(''))
    if type == '1':
        sum()
    elif type == '2':
        subtract()
    elif type == '3':
        multiply()
    elif type == '4':
        divide()
    elif type == '5':
        remainder()
    elif type == '6':
        power()
    elif type == '7':
        root()
    elif type == '8':
        factorial()
    else :
        print('PLEASE CHOOSE A SPECIFIC CALCULATOR!')
        calculator()

#RUNNING THE MAIN(calculator()) FUNCTION AS SOON AS PROGRAM RUNS
calculator()