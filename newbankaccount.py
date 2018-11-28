class User:
    def __init__(self, username, account, interest, amount):
        self.name = username
        self.account = BankAccount(username, account, interest, amount)
    
    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
        return self
    
    def make_deposit(self,amount):
        self.account.deposit(amount)
        return self
    
    def display_user_balance(self):
        self.account.display_account_info()
    
    def transfer_money(self,other_user,amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self     

class BankAccount:
    def __init__(self, name, account,  interest, amount):
        self.name= name
        self.account= account
        self.balance= amount
        self.interest = interest
    
    def deposit(self,amount):
        self.balance += amount
        return self
    
    def withdraw(self,amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(self.name)

        print(self.balance)
    
    def yield_interest(self):
        if(self.balance > 0):
            self.balance += (self.interest*self.balance)
            return self

