#Class User
class User:	
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {
            'checkings': BankAccount(int_rate = 0.08, balance = 0),
            'savings': BankAccount(int_rate=0.04, balance = 0)
        }

    def make_deposit(self, account_type, amount):  
        self.account[account_type].deposit(amount)
        return self
    
    def make_withdrawl(self, account_type, amount):
        self.account[account_type].withdrawl(amount)
        return self
    
    def display_user_balance(self):
        for key , value in self.account.items():
            # print(key,value)
            print(f"User : {self.name} {key} Balance: $ {value.balance}") #if you want to see both without calling which
        # print(f"User: {self.name} {account_type} Balance: $ {self.account[account_type].balance}") #if you want to choose which account
        return self
    
    def transfer_money(self,other_user,account_type,amount):
        self.account[account_type].balance -= amount
        other_user.account[account_type].balance += amount
        return self

#Class Bank

class BankAccount:	
    def __init__(self, int_rate = 0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):  
        self.balance += amount
        return self
    
    def withdrawl(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print("Insufficient funds : Charging a $5 fee")
        return self
    
    def display_account_info(self):
        print(f"Balance: $ {self.balance} ")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self


# chris.make_deposit(100).display_user_balance()
chris = User("Christian Rovet", "Christian@python.com")
micah = User("Micah Wendorf", "Micah@python.com")
# chris.make_deposit('checkings', 1000).display_user_balance('checkings')
# chris.make_deposit('savings', 6000).display_user_balance('savings')
# chris.transfer_money(micah,'checkings',1000)
# micah.display_user_balance('checkings')
chris.display_user_balance()













# #Users or Attributes
# christian = User("Christian Rovet", "christian@python.com")
# scotty = User("Scotty 2 Hottie", "scotty@python.com")
# bob = User("Bob Barker", "bob@python.com")

# #Actions or Methods
# #user Christian
# christian.make_deposit(200).make_deposit(50).make_deposit(2040).make_withdrawl(1500).transfer_money(bob, 110).display_user_balance()

# #user scotty
# scotty.make_deposit(50).make_deposit(50).make_withdrawl(20).make_withdrawl(10).display_user_balance()

# #user bob
# bob.make_deposit(500).make_withdrawl(200).make_withdrawl(80).make_withdrawl(330).display_user_balance()


# checkings = BankAccount(.06,0)
# savings = BankAccount()

# checkings.deposit(50).deposit(90).deposit(122).withdrawl(67).yield_interest().display_account_info()
# savings.deposit(1230).deposit(2230).withdrawl(122).withdrawl(67).withdrawl(73).withdrawl(34).yield_interest().display_account_info()
