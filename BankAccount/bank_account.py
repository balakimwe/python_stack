class BankAccount:

    accounts = []

    # don't forget to add some default values for these parameters!

    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        # your code here
        self.balance += amount
        print(self.balance)
        return self

    def withdraw(self, amount):
        # your code here
        if self.balance >= amount:
            self.balance -= amount
            print(self.balance)
        else:
            print("NOT ENOUGH CASH, CHARGE $5 FEE")
            self.balance -= 5
            print(self.balance)
        return self

    def display_account_info(self):
        # your code here
        print(self.balance)
        return self

    def yield_interest(self):
        # your code here
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
            print(self.balance, self.int_rate)
        else:
            print("Message Alert")
        return self

    @classmethod
    def display_all_account(cls):
        for account in cls.accounts:
            print("account balance: ", account.balance, "account interest rate: ", account.int_rate)




rose = BankAccount (0.01, 100)
rose.deposit(100).withdraw(50).display_account_info().yield_interest().display_all_account()

jeff = BankAccount (0.01, 100)
jeff.deposit(100).withdraw(350).display_account_info().yield_interest().display_all_account()






