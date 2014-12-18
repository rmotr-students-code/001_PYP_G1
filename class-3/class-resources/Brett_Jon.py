class Account(object):
    def __init__(self, ID, money, ODlim):
        self.ID = ID
        self.money = money
        self.transactions = []
        self.is_overdrafted = False
        self.ODlim = ODlim
        
    def show_balance(self):
        return self.money
    
    def deposit(self, deposit_amount):
        self.money += deposit_amount
        self.transactions.append(deposit_amount)
        if self.money >= 0:
            self.is_overdrafted = False
        
    def withdraw(self, withdraw_amount):
        if self.is_overdrafted == False:
            if self.money >= withdraw_amount:
                self.money -= withdraw_amount
                self.transactions.append(-withdraw_amount)
            elif (self.money + self.ODlim) >= withdraw_amount:
                self.money -= withdraw_amount
                self.transactions.append(-withdraw_amount)
                self.is_overdrafted = True
                print('Account is overdrafted. Balance: ' +self.money)
            else:
                print('Unable to withdraw that much. Current balance: ' + self.money)
        if self.is_overdrafted == True:
            print('Cannot withdraw from overdrafted account.')
    
    def transaction_log(self):
        print('All transactions: ' + self.transactions)
    '''
    This class will need a deposit function and a withdraw function as well as a function to print the current amount of 
    money in the account. Additionally, it will need to log all previous transactions as well as a function to print those
    transactions.
    '''
    
        
class SavingsAccount(Account):
    def __init__(self, ID, money, interest_rate):
        super(Account, self).__init__(ID, money)
    
    self.interest_rate = interest_rate
    
    
    def add_int(self, interest_rate, num):        #interest is percentage of interest and num is number of months to get the interest for.
        int_amount = (self.money * interest_rate) * num
        self.money += int_amount
        
        print("the amount to be deposited from interest will be:" + int_amount)
        
    '''
    This class will need to pass the ID and money variables into the super class "Account".
    It will also need a variable to that has what the current interest rate is in the account.
    Lastly it will need a function to add the interest received in a set number of months.
    '''


class CurrectAccount(Account):
    def __init__(self, ID, money, ODlim):
        super(Account, self).__init__(ID, money)
        self.ID = ID
        self.money = money
        self.ODlim = ODlim
    
    
    
    def overdraft_lim(self):
        print('Overdraft limit is: ' + self.ODlim)
    '''
    This class will also pass the ID and money variables into the super class "Account".
    It will need a function to show what the overdraft limit is.
    '''
