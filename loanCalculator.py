# initializing the variables
monthlyPayment = 0
loanAmount = 0
interestRate = 0
loanDurationInYear = 0
numberOfPayments = 0

# Asking the user to provide necessary information to calculate monthly payment
strLoanAmount = input("Enter the loan you want to borrow- \n")
strInterestRate = input("Enter the interest rate you have to give- \n")
strLoanDurationInYear = input("Enter how many years later you'll back the loan- \n")

# Converting string values to float values
loanAmount = float(strLoanAmount)
interestRate = float(strInterestRate)
loanDurationInYear = float(strLoanDurationInYear)

# monthly payment will be once in a month so number of payments in a year will be multipy by 12
numberOfPayments = loanDurationInYear*12

# Calculate monthly payment based on the formula
monthlyPayment = loanAmount * interestRate * (1+interestRate) * numberOfPayments \
    / ((1+interestRate) * numberOfPayments -1)

# Printing the result to the user
print("\n your monthly payment will be %.2f " % monthlyPayment)


