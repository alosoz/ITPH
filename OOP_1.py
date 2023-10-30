
# You are required to implement this using OOP concepts

# Bank account

# BASIC
# Level 1
# 	Create a BankAccount class with attributes: account number, balance.
# 	Implement methods for deposit, withdrawal, and displaying the account balance.
# 	Instantiate two account objects and perform transactions.
# 	Add comments.

class BankAccount:
    def __init__(self,account_number, balance=0.0) -> None:
        self.account_number = account_number
        self.balance = balance
    
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"€{amount:.2f} deposited successfully")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")
    
    
    def withdrawal(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"€{amount:.2f} withdrawn successfully")
        else:
            print("Invalid withdrawal amount. Amount must be greater than 0.")
    

    def display_balance(self):
        print(f"""
    Account Number: {self.account_number}
    Balance: €{self.balance:.2f}""")
        
    
    
    
# ------------------------------------------------------------------------------------------------------------------------------------


# INTERMEDIATE
# Level 2
# 	Let the users choose if they want to deposit, withdraw or display balance.
    def user_menu(self):
        
        while True:
            print("""
    MAIN MENU:
    1. Deposit
    2. Withdrawal
    3. Diplay Balance
    4. Exit
    """)
            chs = input("Enter your chouse (1-2-3-4): ")
            if chs == "1":
                amount = float(input("Enter the amount to deposit: €"))
                self.deposit(amount)
            elif chs == "2":
                amount = float(input("Enter the amount to withdraw: €"))
                self.withdrawal(amount)
            elif chs == "3":
                self.display_balance()
            elif chs == "4":
                sure = input("do you wanna exit the menu: yes or no: ").lower()
                # print(sure)
                if sure == "yes":
                    break
                elif sure == "no":
                    continue
              
            else:
                print("Invalid choice. Please select a valid option (1/2/3/4).")

# ------------------------------------------------------------------------------------------------------------------------------------


# ADVANCED
# Level 3
# 	Integrate private variables.


# ------------------------------------------------------------------------------------------------------------------------------------


# Level 4
# 	Add more functionality, of your own choosing.




#call the class and functions
account1 = BankAccount("12345", 100.0)
account2 = BankAccount("67890", 2000.0)

print("Welcome to the Banking System.")
account1.user_menu()
# account2.user_menu()