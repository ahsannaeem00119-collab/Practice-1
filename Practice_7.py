#Object-Oriented Programming (OOP) in Python

class bankaccount:
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} successful. New balance: {self.balance}")
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. New balance: {self.balance}")
            
        else:
            print("Insufficient funds. Withdrawal failed.")
            
    def transfer(self, amount, recipient_account):
        if amount <= self.balance:
            self.balance -= amount
            recipient_account.balance += amount
            print(f"Transfer of {amount} to {recipient_account.owner} successful. New balance: {self.balance}")
        else:
            print("Insufficient funds. Transfer failed.")
    
    #Add transaction history ,store deposits, withdrawals, and transfers in a list
           
    def transfer_history(self):
        self.history = []
        self.history.append(f"Deposit: {self.balance}")     
        self.history.append(f"Withdrawal: {self.balance}")
        self.history.append(f"Transfer: {self.balance}")
        
    #Add account number 
    def account_number(self, number):
        self.number = number
        print(f"Account number {self.number} assigned to {self.owner}")
        
        
            
    def show_balance(self):
        print(f"Account owner: {self.owner}, Balance: {self.balance}")
        
        
account1 = bankaccount("Alice", 1000)
account1.show_balance()
account1.deposit(500)
account1.withdraw(200)
account1.show_balance()
account1.account_number(12345)
account1.transfer(300, account1)  # Transfer to self for demonstration
account1.transfer_history()
