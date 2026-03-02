class Bank:
    def __init__(self):
        self.balance = 5000
        self.transaction = []

    def deposit(self):
        self.amount = int(input("Enter The Amount"))
        self.balance
        self.balance = self.balance+self.amount
        self.transaction.append(self.amount)
        print("amount deposited")

    def withdraw(self):
        self.amount = int(input("Enter the withdraw amount"))
        self.balance
        if(self.balance>self.amount):
            self.balance = self.balance-self.amount
            print("Your Current Balance is:",self.balance)
        else:
            print("Insufficient Balance")

    def check_bal(self):
        print("Your current balance is", self.balance)
    def ext(self):
        exit()


x = Bank()
choice = int(input("Enter the choice"))
while True:
    if choice == 1:
        x.deposit()
        break
    elif choice == 2:
        x.withdraw()
        break
    elif choice == 3:
        x.check_bal()
        break
    elif choice == 4:
        x.ext()
        