# -*- coding: utf-8 -*-
"""
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance. 
At the end of 12 months, print out the remaining balance. 
Be sure to print out no more than two decimal digits of accuracy. 



"""
def min_balance(balance,annualInterestRate,monthlyPaymentRate):
    
    monthlyInterestRate=annualInterestRate/12.0
    
    for i in range(0,12):
        
        min_mo_payment=(monthlyPaymentRate*balance)
        mo_unpaid_bal=(balance-min_mo_payment)
        balance=mo_unpaid_bal+(monthlyInterestRate*mo_unpaid_bal)

    return print("Remaining balance: " + str(round(balance,2)))
     
min_balance(balance,annualInterestRate,monthlyPaymentRate)

# Passes All test cases (10/10)
        
        
        
            
