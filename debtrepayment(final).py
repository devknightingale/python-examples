#Purpose: Program to calculate monthly payments for a debt entered by the user. 

#Program parts: 
#User input(loop?): Collect debt amount(s)
#User input: Input time to pay off (in months)
#Function: Calculate monthly payment amount for debt amount/time 
import math 

#Get list of user Debts 
billNumber = int(input("Enter number of bills to calculate:\n"))


def GetUserDebts(): 
    debtList = []
    for i in range(0, billNumber):
        userDebt = float(input("Enter the amount owed per bill.\n"))
        debtList.append(userDebt)
    return debtList


#Get list of bills from input
billsList = GetUserDebts()

#Get total sum of bills input by user 
billTotal = sum(billsList)



# Function to return monthly payment based on time frame. 
# Months   
def PayOffMonths():
    monthlyPayments = f'{billTotal / (monthsNumber):.2f}'
    return monthlyPayments

# Years 
def PayOffYears():
    monthlyPayments = f'{billTotal / (yearsNumber * 12):.2f}'
    return monthlyPayments

def paymentOptions():
    paymentOptions = input("Would you like to see repayment options? (Yes/Y or No/N)")
    if paymentOptions == "yes" or paymentOptions == "y":
        # have user choose options 1, 2, 3 - x2 monthly payments, x3 monthly payments, set manual payment 
        selectedOption = input("Please choose a repayment option: 1) Minimum Payment 2) Double payment or 3) Quadruple payment. (Please enter 1, 2, or 3.\n)") 
        if selectedOption == 1:
            #minimum payments
            minimumPayments()
        elif selectedOption == 2:
            #insert function to print out x2 monthly payments & time to pay off
            doublePayments()
        elif selectedOption == 3:
            #insert function to print out x4 monthly payments & time to pay off
            quadPayments()
    elif paymentOptions == "no" or paymentOptions == "n":
        print("Thank you for using the debt repayment calculator.")
       

paymentAmount = ""

# Asks user to input a timeframe for paying off debts in either months or years. 

paymentTime = str(input("Calculate payments based on number of months or years? (Answer months or years.)\n"))
if paymentTime == "months" or paymentTime == "Months":
    monthsNumber = int(input("Enter number of months.\n"))
    paymentAmount = PayOffMonths()
    paymentOptions()
elif paymentTime == "years"  or paymentTime ==  "Years":
    yearsNumber = int(input("Enter number of years.\n"))
    paymentAmount = PayOffYears()
    paymentOptions()




# Outputs monthly payment amount based on timeframe entered by user. 

if paymentTime == "months" or paymentTime == "Months":
    print("To pay off", "$" + str(f'{billTotal:.2f}'), "in", str(monthsNumber),  "months, the monthly payment will be", "$" + str(paymentAmount), "per month.")
    
elif paymentTime == "years"  or paymentTime ==  "Years":
    print("To pay off", "$" + str(f'{billTotal:.2f}'), "in", str(yearsNumber),  "years, the monthly payment will be", "$" + str(paymentAmount), "per month.")
    

# Ask user if they would like to see other repayment options, in x2 monthly payments, x4 monthly payments, OR enter monthly payment amount desired & return how long to pay off. 


def minimumPayments():
    # calculate x2 monthly payments & adjusted time frame 
    timeToPay = math.ceil(billTotal / (paymentAmount))
    print("With a monthly payment amount of", "$" + str(paymentAmount * 2), "it will take", timeToPay, "months to pay off", "$" + str(billTotal) + ".")
    return 

    
def doublePayments():
    # calculate x2 monthly payments & adjusted time frame 
    timeToPay = math.ceil(billTotal / (paymentAmount * 2))
    print("With a monthly payment amount of", "$" + str(paymentAmount * 2), "it will take", timeToPay, "months to pay off", "$" + str(billTotal) + ".")
    return 

def quadPayments():
    # calculate x4 monthly payments & adjusted time frame
    timeToPay = math.ceil(billTotal / (paymentAmount * 4)) 
    print("With a monthly payment amount of", "$" + str(paymentAmount * 4), "it will take", timeToPay, "months to pay off", "$" + str(billTotal) + ".")
    return

input("Thank you for using my program. Press ENTER to exit.")

# Code to ask user if they would like to set a monthly payment & see projected time for paying off debt. 
# [NOTE]: for some reason I could not get this code to work properly. Not sure why. It kept calling the SetMonthlyPayment() function at the end of the program even if that option wasn't chosen. 


    
