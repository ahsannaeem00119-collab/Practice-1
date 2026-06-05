# Mini banking system
def greet_user():
    print("Welcome to the Mini Banking System!")
    
balance = float(input("Please enter your initial balance: "))

def check_balance():
    print(f"Your current balance is: ${balance}")
    
def deposit():
    global balance
    amount = float(input("Enter the amount to deposit: "))
    balance += amount
    print(f"Deposit successful! Your new balance is: ${balance}")
    
def withdraw():
    global balance
    amount = float(input("Enter the amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print(f"Withdrawal successful! Your new balance is: ${balance}")
        
    else:
        print("Insufficient funds. Please try again.")
def Transfer():
    global balance
    recipient = input("Enter the recipient's name: ")
    amount = float(input("Enter the amount to transfer: "))
    if amount <= balance:
        balance -= amount
        print(f"Transfer successful! You have transferred ${amount} to {recipient}. Your new balance is: ${balance}")
    else:
        print("Insufficient funds. Please try again.")

def view_transaction_history():
    print("Transaction history is currently unavailable. Please check back later.")

def prevent_negative_deposit():
    global balance
    amount = float(input("Enter the amount to deposit: "))
    if amount < 0:
        print("Negative deposits are not allowed. Please enter a valid amount.")
    else:
        balance += amount
        print(f"Deposit successful! Your new balance is: ${balance}")

        
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username == "admin" and password == "password":
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False

def main():
  if not login():
        return
  
  
  while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. View Transaction History")
    print("6. Exit")
  
    choice = input("Enter your choice: ")
    
    if choice == '1':
        check_balance()
        
    elif choice == '2':
        deposit()
        
    elif choice == '3':
        withdraw()
        
    elif choice == '4':
        Transfer()
        
    elif choice == '5':
        view_transaction_history()
        
    elif choice == '6':
        print("Thank you for using the Mini Banking System. Goodbye!")
        break
    
       
if __name__ == "__main__":
    greet_user()
    main()
        
        