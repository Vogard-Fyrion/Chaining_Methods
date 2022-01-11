class User:
    bank_name = "First National Dojo"
    def __init__(self , name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self

    def transfer_money(self, amount, reciever):
        self.account_balance -= amount
        reciever.account_balance += amount
        return self


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
vogard = User("Vogard Fyrion", "vogard@python.com")

print(guido.name)	# output: Guido van Rossum
print(monty.name)	# output: Monty Python

guido.make_deposit(100).make_deposit(200).make_deposit(423).make_withdrawal(50).display_user_balance()

monty.make_deposit(50).make_deposit(127).make_withdrawal(62).make_withdrawal(12).display_user_balance()

vogard.make_deposit(400).make_withdrawal(147).make_withdrawal(23).make_withdrawal(176).display_user_balance()

guido.transfer_money(300, vogard).display_user_balance()

vogard.display_user_balance()