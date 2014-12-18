#interface:
    #Account = abstract class, 
        #__init__ args
            #takes ID and total money?
        #add money "deposit"
        #retrieve money "withdraw"
        #history [{date, ammount, id}, ..]
        
    #Savings = child class
        #__init__ args:
            # total money (passed to Account)
            # interest rate
            # calculate interest for (e.g 6 months for xxx money)
        
    #CurrentAccount = child class
        #__init__ args:
            #overdraft limit
            #total money (passed to Account)
            #negative interest?

class Account(object):
    def __init__(self, _id, total_money):
        self._id = _id
        self.total_money = total_money
    
    def deposit(self, amount):
        self.total_money += amount
        
    def withdraw(self, amount):
        self.total_money -= amount
        return amount
        
        
class SavingsAccount(Account):
    ID = 0
    def __init__(self, total_money, interest_rate):
        self._id = CurrentAccount.ID
    #    CurrentAccount.ID += 1
        SavingsAccount.ID +=1
        super(SavingsAccount, self).__init__(self._id, total_money)
        self.interest_rate = interest_rate
        
    def calculate_interest(self, months=6):
        return (self.interest_rate * self.total_money)/(months/12)

    def withdraw(self, amount):
        if amount > self.total_money:
            print "not enough funds" #use raise? 
            return 0
        else:
            return super(SavingsAccount, self).withdraw(amount)


class CurrentAccount(Account):
    ID = 0
    def __init__(self, _money, _overdraft_limit):
        # I think you need to use super here to call the parent __init__
        self._id = ID
        CurrentAccount.ID += 1
        self._money = _money
        self._overdraft_limit = _overdraft_limit
        self.negative_interest = 0 # initial is 0
        
    def calculate_negative_interest(self):
        if self._money < 0:
            self.negative_interest = self._money * 2 #some kind of math to figure out the interest 
 
    def withdraw(self, ammount):
        """
        """
        
        # This one?
        if self._money - ammount <= self._overdraft_limit: # is ok
            super(Account, self)__init__.withdraw(amount)
        else:
            print "Sorry you went over your limit"
            
        if self._money < 0:
            self.calculate_negative_interest()
    
    def add_money(self, money):
        self._money += money