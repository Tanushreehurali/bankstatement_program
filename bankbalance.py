# bank_balance.py

# Ask user for initial balance and deposit amount
initial_balance = float(input("Enter Initial Balance: ₹"))
deposit_amount = float(input("Enter Deposit Amount: ₹"))

# Calculate new balance after deposit
new_balance = initial_balance + deposit_amount
print(f"New Balance after deposit: ₹{new_balance}")

# Ask for withdrawal amount
withdraw_amount = float(input("Enter Withdrawal Amount: ₹"))

# Calculate final balance
final_balance = new_balance - withdraw_amount
print(f"Final Balance: ₹{final_balance}")
