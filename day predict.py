nameOfday = input('Enter name of the Day: ')
noOfdays = int(input('Enter no. of Days: '))
index = 0
daysList = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Satureday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Satureday', 'Sunday']

for i in range(len(daysList)):
    if nameOfday == daysList[i]:
        index = i
        break

check = noOfdays % 7

if check == 0:
    print('It will be ','"',daysList[i],'"', ' after ',noOfdays, ' days.')
if check == 1:
    print('It will be ','"',daysList[i+1],'"', ' after ',noOfdays, ' days.')
elif check == 2:
    print('It will be ','"',daysList[i+2],'"', ' after ',noOfdays, ' days.')
elif check == 3:
    print('It will be ','"',daysList[i+3],'"', ' after ',noOfdays, ' days.')
elif check == 4:
    print('It will be ','"',daysList[i+4],'"', ' after ',noOfdays, ' days.')
elif check == 5:
    print('It will be ','"',daysList[i+5],'"', ' after ',noOfdays, ' days.')
elif check == 6:
    print('It will be ','"',daysList[i+6],'"', ' after ',noOfdays, ' days.')