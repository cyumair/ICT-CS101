interestList = []
amount = eval(input('Enter Amount (eg 100)'))
interest = eval(input('The annual interest rate '))
months = eval(input('no. of months eg(6) '))
def interestrate(amount, interest, months):
    balance = 0
    for i in range(months):
        balance = (amount + balance) * ( 1 + interest / 1200)
        interestList.append(balance)
        
interestrate(amount, interest, months)
m = 1
for i in interestList:
    print('After ' , m, ' month, The value in account becomes ', i)
    m -= -1
               
    
