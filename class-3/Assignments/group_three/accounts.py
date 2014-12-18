#accounts.py

import abc

class Account(object):
    __metaclass__ = abc.ABCMeta
    _rate = 0.0
    def __init__(self, name, acctnum, bal):
        self.name = name
        self.acctnum = acctnum
        self.balance = bal
    def deposit(self, amount):
        self.balance += abs(amount)
    def withdrawl(self, amount):
        if amount <= self.balance:
            self.balance -= abs(amount)
            return True
        else:
            print "Current balance (${}) is insufficient to withdraw ${}".format(self.balance, amount)
            return False
    def apply_interest(self):
        raise NotImplementedError("apply_interest() method isn't implemented.")
  
class CurrentAcct(Account):
    _rate = .03
    def apply_interest(self):
        self.balance += self.balance*self._rate
  
class SavingsAcct(Account):
    _rate = .05    
    def withdrawl(self, amount):
        if self.balance - amount  < 50:
            self.balance -= abs(amount)
            return True
        else:
            return False
    def apply_interest(self):
        self.balance += self.balance*self._rate