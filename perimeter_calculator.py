sides = [(1,3), (2,7), (3,9), (-1,8)]
perimeter = 0
for i in range(len(sides)-1):
    dist = (((sides[i+1][0] - sides[i][0])**2) + ((sides[i+1][1] - sides[i][1])**2))** 0.5
    perimeter += dist

distance = (((sides[-1][0] - sides[0][0])**2) + ((sides[-1][1] - sides[0][1])**2))** 0.5
perimeter += dist
print(perimeter)