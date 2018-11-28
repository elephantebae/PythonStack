class User:
    def __init__(self, username):
        self.name = username
        self.account_balance = 0
    
    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self
    
    def make_deposit(self,amount):
        self.account_balance += amount
        return self
    
    def display_user_balance(self):
        print(self.name)
        print(self.account_balance)
    
    def transfer_money(self,other_user,amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self        



pauluser= User("Paul")
pauluser.make_deposit(20).make_deposit(45).make_deposit(30).make_withdrawal(20).display_user_balance()


robuser= User("Rob")
robuser.make_deposit(20).make_deposit(30).make_withdrawal(10).make_withdrawal(11).display_user_balance()

roduser= User("Rod")
roduser.make_deposit(1000).make_withdrawal(10).make_withdrawal(11).make_withdrawal(1).display_user_balance()

pauluser.transfer_money(roduser, 30).display_user_balance()
roduser.display_user_balance()

    