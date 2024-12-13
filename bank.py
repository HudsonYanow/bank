class Bank:
    # this initializes the bank class
    def __init__(self, balance):
        self.balance=balance
    def deposit(self, amount=0):
        # this function deposits money to the bank acount
        if amount>=0:
            self.balance+=amount
    def withdraw(self, amount=0):
        # this function withdraws money from the bank acount
        if amount>=0:
            self.balance-=amount
    def getBalance(self):
        # this function tells you your curent balance
        return self.balance
