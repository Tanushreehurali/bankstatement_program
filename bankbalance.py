Bank Account Balance Program
Problem Statement:
Create a Python program that asks the user to enter an initial balance and deposit amount.
Display the updated balance after the deposit. Push the program to a GitHub repository.
Then, create a new branch called withdraw-feature and modify the program to 
allow the user to withdraw money and show the new balance. Push and merge the branch
 into the main branch by commands of git from terminal 
Expected Output:
Initial Balance: ₹5000 
Deposit: ₹2000 
New Balance after deposit: ₹7000 
Withdraw: ₹1500 
Final Balance: ₹5500

initial_balance = float(input("Enter Initial Balance: ₹"))
deposit_amount = float(input("Enter Deposit Amount: ₹"))


new_balance = initial_balance + deposit_amount


print(f"New Balance after deposit: ₹{new_balance}")