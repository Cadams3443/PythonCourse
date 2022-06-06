class User:

    def __init__(self):
        self.name = "name"
        self.balance = 0

    def display_user_balance(self):
        print(self.balance)
        return self
    
    def make_withdrawl(self, amount):
        self.balance -= amount
        return self

    def make_deposit(self, amount):
        self.balance += amount
        return self
    
    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount
        return self

User()

guido = User()
guido.name = "Guido"
guido.balance = 500

monty = User()
monty.name = "Monty"
monty.balance = 10000

jessica = User()
jessica.name = "Jessica"
jessica.balance = 2000


guido.make_deposit(100).make_deposit(300).make_deposit(400).make_withdrawl(400).transfer_money(jessica, 100).display_user_balance()


monty.make_deposit(200).make_deposit(400).make_withdrawl(500).make_withdrawl(300).display_user_balance()


jessica.make_deposit(90).make_withdrawl(60).make_withdrawl(40).make_withdrawl(30).display_user_balance()
