def primecounter(num):
    primecount = 0
    for i in range(3, num+1):
        prime = True
        fact = 2
        while fact < i:
            if i % fact == 0:
                prime = False
                break
            else:
                fact += 1
        if prime:
            primecount += 1
    return primecount

num = int(input('enter number'))
pc = primecounter(num)
print(pc)