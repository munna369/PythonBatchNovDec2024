# sep 1: create a variable 'balance' with intial value 0

name_of_the_bank = "icici"
account_number = 1234567890
intial_balance = 0
bank_details = {
    "name_of_the_bank": "icici",
    "account_number": 1234567890,
    "initial_balance": 0
}
print(bank_details)

# enter a value for initail deposit
initial_deposit = int(input("Enter initial deposit amount: "))
bank_details["initial_balance"] += initial_deposit
print("Updated balance:", bank_details["initial_balance"])

# step 3: salary credited of 3300
salary_credited = 3300
bank_details["initial_balance"] += salary_credited
print("Updated balance afer salary:", bank_details["initial_balance"])

# step 4: online purchase of 33.33
online_purchase = 33.33
bank_details["initial_balance"] -= online_purchase
print("Updated balance after online purchase:", bank_details["initial_balance"])

# step 5: house rent paid of 1500
house_rent_paid = 1500
bank_details["initial_balance"] -= house_rent_paid
print("Updated balance after house emi:", bank_details["initial_balance"])