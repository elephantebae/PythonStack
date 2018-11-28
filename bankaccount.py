class BankAccount:
    def __init__(self, name_account, interest, amount):
        self.name_account= name_account
        self.balance= amount
        self.interest = interest
    
    def deposit(self,amount):
        self.balance += amount
        return self
    
    def withdraw(self,amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(self.name_account)
        print(self.balance)
    
    def yield_interest(self):
        if(self.balance > 0):
            self.balance += (self.interest*self.balance)
            return self

pauls_account= BankAccount("Paul", .01, 1000)
rods_account= BankAccount("Rod",.01, 1002)

pauls_account.deposit(12).deposit(100).deposit(15).yield_interest().display_account_info()
rods_account.deposit(123123).deposit(1000).withdraw(1234).withdraw(2123).yield_interest().display_account_info()