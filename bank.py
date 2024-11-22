class Bank:
    """
    A simple Bank class that allows a user to manage their balance by 
    depositing, withdrawing, and checking their balance.

    Attributes:
        balance (float): The current balance in the bank account.
    """

    def __init__(self, balance):
        """
        Initializes the Bank object with a specified balance.

        Args:
            balance (float): Initial balance for the account.
        """
        self.balance = balance

    def deposit(self, amount=0):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float): The amount to deposit. Must be non-negative.
        """
        if amount >= 0:
            self.balance += amount

    def withdraw(self, amount=0):
        """
        Withdraws a specified amount from the account.

        Args:
            amount (float): The amount to withdraw. Must be non-negative.
        """
        if amount >= 0:
            self.balance -= amount

    def getBalance(self):
        """
        Prints and returns the current balance.

        Returns:
            float: The current balance in the account.
        """
        print(f"Your balance is {self.balance}")
        return self.balance


# Main program to interact with the Bank class
bank1 = Bank(100)  # Create a Bank instance with an initial balance of 100

active = True
while active:
    ask = input(
        "Would you like to:\n"
        "1) Deposit\n"
        "2) Withdraw\n"
        "3) Check your balance\n"
        "4) Exit\n"
        "Enter the number of your choice: "
    )

    if ask == "1":
        try:
            dep = float(input("How much would you like to deposit? "))
            bank1.deposit(dep)
        except ValueError:
            print("Please enter a valid number.")

    elif ask == "2":
        try:
            wit = float(input("How much would you like to withdraw? "))
            bank1.withdraw(wit)
        except ValueError:
            print("Please enter a valid number.")

    elif ask == "3":
        bank1.getBalance()

    elif ask == "4":
        print("Goodbye!")
        active = False

    else:
        print("Please enter a number within the valid range.")

