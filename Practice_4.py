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

def main():
  while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        check_balance()
        
    elif choice == '2':
        deposit()
        
    elif choice == '3':
        withdraw()
        
    elif choice == '4':
        print("Thank you for using the Mini Banking System. Goodbye!")
        break

if __name__ == "__main__":
    greet_user()
    main()
        
        