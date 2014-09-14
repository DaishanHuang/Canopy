'''
Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0
should not specify the values for the variables balance or annualInterestRate
'''
#test numbers
#balance = 320000
#annualInterestRate = 0.2
balance = 999999
annualInterestRate = 0.18
#test
monthlyInterestRate = annualInterestRate/12
preppingPayment = True
upperBound = False
lowestPayment = 0
attempt = 0

paymentLower = (balance / 12)
paymentUpper = ((balance * (1 + monthlyInterestRate)**12) / 12.0)

while preppingPayment:
    attempt += 1
    workingBalance = balance
    monthlyPayment = round(((paymentLower + paymentUpper)/2),2)
    #print('paymentUpper: ' + str(paymentUpper) + ' paymentLower: ' + str(paymentLower) )
    #print('montlyPayment: ' + str(monthlyPayment) )
    for i in range(1, 13):
        monthlyUnpaidBalance = (workingBalance - monthlyPayment)
        updatedUnpaidBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
        workingBalance = updatedUnpaidBalance
        if workingBalance < 0:
            upperBound = True
            #print('Upper Bound: ' + str(paymentUpper) + ' i = ' + str(i) )
            #print('Balance: ' + str(workingBalance) )
            break
        if workingBalance == 0 and i == 12:
            lowestPayment = monthlyPayment
            preppingPayment = False
            break
    if preppingPayment and upperBound:
        paymentUpper = monthlyPayment  # reset upper bound
        upperBound = False
    else:
        paymentLower = monthlyPayment  # reset lower bound
        upperBound = False
    if (paymentUpper - paymentLower) < .12:  # we can't get any closer
        lowestPayment = paymentUpper
        preppingPayment = False
    if paymentUpper == paymentLower:  # we have a problem
        preppingPayment = False
        print('Error')
print('Lowest Payment: ' + str(lowestPayment) )
print('Attempts: ' + str(attempt) )