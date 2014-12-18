import accounts
from random import randrange, choice


class Bank(object):
    def __init__(self, bankname):
        self.bank = bankname
        self.checkingaccts = {}
        self.savingsaccts = {}
        self.counter = 0
    def _countgen(self):
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        x = lambda num: randrange(1, 1100)
        y = lambda let: choice(letters)
        return "{}{}{}{}{}".format(x(0), y(1), x(0), y(1), x(0))
        
    def open_checking_acct(self, name, deposit):
        """Open a checking account.
        """
        acctnum = self._countgen()
        if acctnum not in self.checkingaccts:
            checking_acct = accounts.CurrentAcct(name, acctnum, deposit)
            self.checkingaccts[checking_acct.acctnum] = checking_acct
        else:
            self.open_checking_acct(name, deposit)
    #    return self.bankaccts
    def open_savings_acct(self, name, deposit):
        acctnum = self._countgen()
        if acctnum not in self.savingsaccts:
            savings_acct = accounts.SavingsAcct(name, acctnum, deposit)
            self.savingsaccts[savings_acct.acctnum] = savings_acct
        else:
            self.open_checking_acct(name, deposit)
    #    return self.bankaccts
    def acct_update(self):
        savings_rate = accounts.SavingsAcct._rate
        for x, y in self.savingsaccts.items():
            y.balance += y.balance*savings_rate
    
    
x = Bank("Zions")
x.open_savings_acct("mike", 80000000)
print x.acct_update()