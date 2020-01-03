today = int(input('Enter the day today(BETWEEN 0 AND 6)'))
days = int(input('No. of Days'))
current_day = today

# THIS PART PRINTS THE DAY TODAY
if today == 0:
    print('Sunday')
if today == 1:
    print('Monday')
if today == 2:
    print('Tuesday')
if today == 3:    
    print('Wednesday')
if today == 4:
    print('Thursday')
if today == 5:
    print('Friday')
if today == 6: 
    print('Satureday')

#CALCULATION TO PREDICT WHAT WOULD BE AFTER CERTAIN AMOUNT OF
calculation = (days + current_day) % 7

#THIS PART PRINTS THE DAY AFTER SOME AMOUNT OF DAYS
if calculation == 0:
    print('Sunday')
if calculation == 1:
    print('Monday')
if calculation == 2:
    print('Tuesday')
if calculation == 3:
    print('Wednesday')
if calculation == 4:
    print('Thursday')
if calculation == 5:
    print('Friday')
if calculation == 6:
    print('Satureday')