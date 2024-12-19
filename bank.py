class Bank:
    # this initializes the bank class
    def __init__(self, balance):
        self.balance=balance
    def deposit(self, amount=0):
        """
        deposits money to the acount

        Args:
        amount(int): amount being deposited
        """
        if amount>=0:
            self.balance+=amount
    def withdraw(self, amount=0):
        """
        withdraws money from the account

        Args:
        amount(int): amount being withdrawed
        """
        if amount>=0:
            self.balance-=amount
    def getBalance(self):
        """
        returns the current balance of your account

        Returns:
        self.balance(int): returns the balance of account
        """
        return self.balance
