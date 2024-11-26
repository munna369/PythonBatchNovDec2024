# Input name, principal amount, rate of interest, and time period
name = input("Enter your name: ")
account_number = input("Enter your account number: ")
loan_amount = float(input("Enter the loan amount: "))

# Define the rate of interest
rate = float(input("Enter the rate of interest: "))

# Define the time period in years
time = float(input("Enter the time period in years: "))

# Calculate simple interest
simple_interest = (loan_amount * rate * time) / 100

# Calculate compound interest
compound_interest = loan_amount * ((1 + rate / 100) ** time - 1)

# Print the results
print("Name:", name)
print("Account Number:", account_number)
print("Loan Amount:", loan_amount)
print("Simple Interest: {: .2f}".format(simple_interest))
print("Compound Interest:{: .2f}".format(compound_interest))