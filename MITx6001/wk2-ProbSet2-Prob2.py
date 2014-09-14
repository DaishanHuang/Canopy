'''
Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

should not specify the values for the variables balance or annualInterestRate
'''
#test numbers
#balance = 3926
#annualInterestRate = 0.2
#test  
monthlyInterestRate = annualInterestRate/12
preppingPayment = True
lowestPayment = 0
monthlyPayment = 10

while preppingPayment:
    #print('monthlyPayment: ' + str(monthlyPayment) + ' balance: ' + str(balance) )
    workingBalance = balance
    for i in range(1, 13):
        monthlyUnpaidBalance = round((workingBalance - monthlyPayment),2)
        updatedUnpaidBalance = round(monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance),2)
        workingBalance = round(updatedUnpaidBalance,2)
        if workingBalance <= 0:
            lowestPayment = monthlyPayment
            preppingPayment = False
            break
    monthlyPayment += 10
print('Lowest Payment: ' + str(lowestPayment) )