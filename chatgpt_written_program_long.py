class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited ${amount}")
            print(f"Added ${amount} to the balance.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                self.transactions.append(f"Withdrew ${amount}")
                print(f"Withdrew ${amount} from the balance.")
            else:
                print("Insufficient balance to complete withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance

    def calculate_interest(self, rate=0.01):  # Simple interest for one period
        interest = self.balance * rate
        self.balance += interest
        self.transactions.append(f"Interest added: ${interest:.2f}")
        return interest

    def show_transactions(self):
        for transaction in self.transactions:
            print(transaction)


def main():
    account_name = input("Enter the account holder's name: ")
    account = BankAccount(account_name)

    while True:
        print("\nOptions:")
        print("1. Deposit money")
        print("2. Withdraw money")
        print("3. Check balance")
        print("4. Add interest")
        print("5. Show transactions")
        print("6. Exit")

        user_choice = input("Choose an option: ")

        if user_choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif user_choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif user_choice == "3":
            print(f"Current balance: ${account.get_balance()}")
        elif user_choice == "4":
            rate = float(input("Enter the interest rate (as a decimal): "))
            account.calculate_interest(rate)
        elif user_choice == "5":
            account.show_transactions()
        elif user_choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
