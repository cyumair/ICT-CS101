x, y, z = eval(input('Enter three edges '))
if (x + y > z) or (x + z > y) or (z + y > x):
    perimeter = x + y + z
    print('Perimeter of the triangle is ', perimeter)
else:
    print('Wrong Input')