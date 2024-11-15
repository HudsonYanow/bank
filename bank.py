class Bank:
    def __init__(self, balance):
        self.balance=balance
    def deposit(self, amount=0):
        if amount>=0:
            self.balance+=amount
    def withdraw(self, amount=0):
        if amount>=0:
            self.balance-=amount
    def getBalance(self):
        print(self.balance)
        return self.balance
bank1= Bank(100)
bank1.deposit(100)
bank1.withdraw(50)
bank1.getBalance()