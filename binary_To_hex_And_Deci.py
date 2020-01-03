
def isbinary(num):
    check = 0
    for i in range(len(num)):
        if num[i] == "0" or num[i] == "1":
            check += 1
    if check == len(num):
        return True
    else:
        return False
    
def todeci(binary):
    d1 = int(binary[0])
    d2 = int(binary[1])
    d3 = int(binary[2])
    d4 = int(binary[3])
    d5 = int(binary[4])
    d6 = int(binary[5])
    deci = d1 * (2 ** 5) + d2 * (2 ** 4) + d3 * (2 ** 3) + d4 * (2 ** 2)+ d5 * (2 ** 1) + d6 * (2 ** 0)
    return deci



def tohex(num):
    lh = num[2:6]
    uh = num[0:2]
    LH = int(lh , 2)
    UH = int(uh, 2)
    if LH == 10:
        LH = 'A'
    elif LH == 11:
        LH = 'B'
    elif LH == 12:
        LH = 'C'
    elif LH == 13:
        LH = 'D'
    elif LH == 14:
        LH = 'E'
    elif LH == 15:
        LH = 'F'
    return (str(UH) + str(LH))

num = input('Please enter 6 digit binary number ')
if len(num) != 6:
    print('Invalid input')
else:
    checkbin = isbinary(num)
    if checkbin:
        deci = todeci(num)
        hexa = tohex(num)
        print('Decimal of ' , num, ' is ' , deci, ' and hexadecimal of ', num, ' is ', hexa)
    else:
        print('Number is not binary')