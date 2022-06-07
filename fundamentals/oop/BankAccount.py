class BankAccount:
    
    all_accounts = []

    def __init__(self, first_name, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        self.first_name = first_name
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(amount < self.balance):
            self.balance -= amount
            return self
        else:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
            print("Balance after fee", self.balance)
            return self

    def display_account_info(self):
        print(self.first_name+ "'s balance is", self.balance )
        return self

    def yield_interest(self):
        interest = self.balance * self.int_rate
        self.balance += interest
        print("Interest accrued:", interest)
        return self

    @classmethod
    def Accounts(cls):
        for account in cls.all_accounts:
            print(account.first_name+ "'s balance is: ", account.balance)
            


john = BankAccount("John", 0.02, 1000)

john.display_account_info().deposit(50).deposit(150).deposit(70).withdraw(50).yield_interest().display_account_info()

lisa = BankAccount("Lisa", 0.01, 700)

lisa.display_account_info().deposit(50).deposit(10).withdraw(50).withdraw(750).withdraw(600).withdraw(20).yield_interest().display_account_info()

BankAccount.Accounts()