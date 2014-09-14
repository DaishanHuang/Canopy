'''
Monthly interest rate= 
    (Annual interest rate) / 12.0
Minimum monthly payment = 
    (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = 
    (Previous balance) - (Minimum monthly payment)
Updated balance each month = 
    (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

The code you paste into the following box 
should NOT specify the values for the variables 

balance 
annualInterestRate
monthlyPaymentRate 

our test code will define those values before testing your submission.
'''
# test numbers
#balance = 4213
#annualInterestRate = 0.2
#monthlyPaymentRate = 0.04
# test end

monthlyInterestRate = annualInterestRate/12
totalPaid = 0 

for i in range(1,13):
    
    minimumMonthlyPayment = round((monthlyPaymentRate * balance),2)
    monthlyUnpaidBalance = round((balance - minimumMonthlyPayment),2)
    updatedUnpaidBalance = round(monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance),2)
       
    print('Month: ' + str(i) )
    print('Minimum monthly payment: ' + str(minimumMonthlyPayment) )
    print('Remaining balance: ' + str(updatedUnpaidBalance) )
    
    balance = round(updatedUnpaidBalance,2)
    totalPaid += minimumMonthlyPayment
    
print('Total paid: ' + str(totalPaid) )
print('Remaining balance: ' + str(updatedUnpaidBalance) )
