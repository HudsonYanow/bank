import BL as bl

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
bank1= Bank(100)

active=True
while active:
    # the while loop lets us run the program until the user wants to close it
    # the input function is the menu for the project
    userinput=input("""would you like to:
                1)deposit
                2)withdraw
                3)get your balence
                x)type anything else to exit the program
                """)
    if userinput=="1":
        # this asks the user how much they would like to deposit and deposits it
        depAmount=bl.intInputValidator("how much would you like to deposit: ","please only use numbers: ")
        bank1.deposit(depAmount)
    elif userinput=="2":
        # this asks the user how much they would like to withdraw and withdraws it
        drawAmount=bl.intInputValidator("how much would you like to withdraw: ","please only use numbers: ")
        bank1.withdraw(drawAmount)
    elif userinput=="3":
        # this tells you your curent balance
        balance=bank1.getBalance()
        print(f"your balance is {balance}")
    else:
        # this ends the program
        active=False
