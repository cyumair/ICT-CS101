num = eval(input("enter a number"))
isPrime = True
checker =2
while checker < num:
    if num % checker == 0:
        isPrime = False
        break
    else:
       checker += 1  
    
if isPrime:
    print('Prime')
else:
    print('not prime')