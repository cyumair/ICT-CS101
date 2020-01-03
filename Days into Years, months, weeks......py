#Keep running the Program using an Infinite Loop
while True:
    # Taking input from the user (no. of days)
    days = eval(input('Enter no. of Days '))
    # Calculating no. of Years in ?days
    years = days // 365
    # Calulating no. of Months if Days are not enough for a complete year
    months = (days % 365) // 30
    # Calculating no. of weeks if Days are not enough for a complete month
    weeks = ((days % 365 ) % 30 ) // 7
    # Calculating no. of Days if days are not enough for a complete week
    noOfdays = ((days % 365 ) % 30 ) % 7
    # Printing our calculated Results
    print(days, ' is ', years, ' years ', months, ' months ', weeks, ' weeks ', noOfdays,' days.')
