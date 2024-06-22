class bank_account:

    def __init__(self, customer_name, initial_balance=0):
        self.customer_name = customer_name
        self.balance = initial_balance
        self.history_file = f"{self.customer_name}_transactions.txt"

        
        with open(self.history_file, "w") as file:
            file.write("Transaction History:\n")
            file.write(f"initial Balance: {self.balance}\n")

        print(f"Welcome {self.customer_name}! ")
        print(f"Starting Balance: {self.balance}")

    def record_transaction(self, transaction):
        with open(self.history_file, "a") as file:
            file.write(transaction+ "\n")

    def deposit(self, amount):
        self.balance += amount
        transaction = f"deposited: {amount}, New Balance: {self.balance}"
        self.record_transaction(transaction)
        print(f"\namount deposited: {amount}")

    def withdrew(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            transaction = f"withdrew: {amount}, New Balance: {self.balance}"
            self.record_transaction(transaction)
            print(f"\nyou withdrew: {amount}")
        else:
            print("\n Insufficient balance")
            transaction = f"Failed withdrawal Attempt: {amount}, Available Balance: {self.balance}"
            self.record_transaction(transaction)

    def show_balance(self):
        print(f"\nCurrent Balance: {self.balance}")

    def show_transaction_history(self):
        try:
            with open(self.history_file, "r") as file:
                history = file.read()
                print("\nTransaction History:\n")
                print(history)
        except FileNotFoundError:
            print("\nTransaction history not available.")


customer_name = input("Enter customer name: ")
initial_balance = float(input("Enter initial balance: "))
account = bank_account(customer_name, initial_balance)


while True:
    print("\n1. deposit")
    print("2. withdraw")
    print("3. display balance")
    print("4. display Transaction History")
    print("5. Exit")
    
    choice = input("enter your choice: ")
    
    if choice == '1':
        amount = float(input("Enter amount to be deposited: "))
        account.deposit(amount)
    elif choice == '2':
        amount = float(input("Enter amount to be withdrawn: "))
        account.withdrew(amount)
    elif choice == '3':
        account.show_balance()
    elif choice == '4':
        account.show_transaction_history()
    elif choice == '5':
        break
    else:
        print("Invalid choice.")

