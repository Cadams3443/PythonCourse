class User:

    def __init__(self):
        self.name = "name"
        self.balance = 0

    def display_user_balance(self):
        print(self.balance)
    
    def make_withdrawl(self, amount):
        self.balance -= amount

    def make_deposit(self, amount):
        self.balance += amount
    
    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount

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

guido.make_deposit(100)
guido.make_deposit(300)
guido.make_deposit(400)
guido.make_withdrawl(400)
guido.display_user_balance()

monty.make_deposit(200)
monty.make_deposit(400)
monty.make_withdrawl(500)
monty.make_withdrawl(300)
monty.display_user_balance()


jessica.make_deposit(90)
jessica.make_withdrawl(60)
jessica.make_withdrawl(40)
jessica.make_withdrawl(30)
jessica.display_user_balance()

# print(guido.balance)
guido.transfer_money(jessica, 100)
jessica.display_user_balance()
guido.display_user_balance()