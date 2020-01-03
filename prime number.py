primecount = 0
compositecount = 0
for j in range(10):
    prime = True
    i = 2
    num = int(input('Enter any number '))
    if num < 2:
        prime = False
    else:
        while i < num:
            if num % i == 0:
                prime = False
                break
            else:
                i = i + 1

    if prime:
        print(num, ' is prime')
        primecount += 1
    else:
        print(num , ' is composite')
        compositecount -= -1
print(primecount, ' numbers are prime ')
print(compositecount, ' numbers are composite')

