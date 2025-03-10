class ATM:
    def __init__(self, initial_balance=5000.00):
        self.balance = initial_balance

    def check_balance(self):
        print(f"Your current balance is: ₹{self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited ₹{amount:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Successfully withdrawn ₹{amount:.2f}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount.")

def main():
    atm = ATM()  # Initialize ATM with ₹5000
    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            amount = float(input("Enter deposit amount: ₹"))
            atm.deposit(amount)
        elif choice == "3":
            amount = float(input("Enter withdrawal amount: ₹"))
            atm.withdraw(amount)
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
