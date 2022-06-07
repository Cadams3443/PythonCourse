class BankAccount:
    
    all_accounts = []

    def __init__(self, first_name, int_rate, balance): 
        self.int_rate = int_rate
        self.first_name = first_name
        self.balance = balance
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
        print(self.balance )
        return self

    def yield_interest(self):
        interest = self.balance * self.int_rate
        self.balance += interest
        print("Interest accrued:", interest)
        return self

    @classmethod
    def Accounts(cls):
        for account in cls.all_accounts:
            print(account.first_name+ "'s total funds are: ", account.balance)
            
class User:
    def __init__(self, first_name, s_start_balance, c_start_balance):
        self.first_name = first_name
        self.account = { 
            "Savings Account": BankAccount(first_name=first_name, int_rate=0.02, balance=s_start_balance),
            "Checking Account": BankAccount(first_name=first_name, int_rate=0.02, balance=c_start_balance)
        }

    def account_display(self):
        temp = ""
        print(self.first_name+"'s Account Balances\n --------------------")
        for key,val in self.account.items():
            temp += (f"{key} : ${val.balance} \n")

        print(temp)


john = User("John", 700, 500)
lisa = User("Lisa", 800, 300)

john.account["Savings Account"].deposit(400).withdraw(200)
john.account["Checking Account"].deposit(200)
john.account_display()


lisa.account["Savings Account"].deposit(400).withdraw(200)
lisa.account["Checking Account"].deposit(200)
lisa.account_display()

BankAccount.Accounts()