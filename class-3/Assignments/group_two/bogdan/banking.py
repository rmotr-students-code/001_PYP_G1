##
## Defining accounts
## 
class Account(object):
    ID = 0
    def __init__(self, customer):
        self.id = Account.ID
        Account.ID += 1

        self.customer_name = customer.name
        self.total_money = 0

    def deposit(self, ammount_of_money):
        self.total_money += ammount_of_money

    def withdraw(self, ammount_of_money):
        self.total_money -= ammount_of_money
        return ammount_of_money
 
    def get_balance(self):
        return self.total_money
   
    def get_account_number(self):
        return self.id


class SavingsAccount(Account):
    def __init__(self, customer_name):
        super(SavingsAccount, self).__init__(customer_name)

    def calculate_interest(self):
        # to be calculated per month
        self.interest_rate = self.total_money * 0.06 / 12 
    
    def add_interest(self):
        self.total_money += self.interest_rate
    
    #extend the deposit
    def deposit(self, ammount_of_money):
        super(SavingsAccount, self).deposit(ammount_of_money)
        self.calculate_interest()

    def withdraw(self, ammount_of_money):
        if self.total_money - ammount_of_money < 0:
            return False
        else:
            super(SavingsAccount, self).withdraw(ammount_of_money)
            
    # I will define an update method to be easy to acces
    def update(self):
        self.calculate_interest()
        self.add_interest()
    
    
class CurrentAccount(Account):
    def __init__(self, customer_name):
        super(CurrentAccount, self).__init__(customer_name)
        # lets say the overdraft limit is - 1000 units
        self.limit = 1000
    def withdraw(self, ammount_of_money):
        if self.total_money - ammount_of_money < -  self.limit:
            message = "I am sorry you passed the limit by "
            message += str( self.total_money - ammount_of_money +   self.limit )
            message += ", you can withdraw maximum " + str( self.total_money + self.limit) + "."
            print message
        else:
            super(CurrentAccount, self).withdraw(ammount_of_money)
        
    def update(self):
        # cannot be in overdraft caouse there is a limit, but I will send a notification if is negative balance
        if self.total_money < 0:
            print "I am writing to announce you that your balance is negative, please add some founds"
            
            

class Client():
    def __init__(self, name, accounts = []):
        self.name = name
        self.accounts = accounts
        
    def add_account(self, account):
        self.accounts.append(account)
        
    def how_much_do_i_have(self):
        ammount = 0
        for account in self.accounts:
            ammount += account.get_balance()


class Bank():
    def __init__(self, name, accounts = []):
        self.name = name
        self.accounts = accounts
    
    def add_account(self, account):
        self.accounts.append(account)
    
    def update(self):
        # get every object and call update on them
        for account in self.accounts:
            account.update()
            
            