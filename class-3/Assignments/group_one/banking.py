from __future__ import division

class IdManager(object):
    def __init__(self):
        self.cur_id = 0
        
    def get_id(self):
        an_id = self.cur_id
        self.cur_id += 1
        return an_id

class Customer(object):
    def __init__(self, name):
        self.name = name
        self.accounts = []
        
    def __str__(self):
        return self.name + "".join(["\n\t" + str(account) for account in self.accounts])    
 
class Account(object):
    def __init__(self, customer, funds, id_manager):
        self.customer = customer
        self.funds = funds
        self._id_manager = id_manager
        self._id = self._id_manager.get_id()

    def deposit(self, amount):
        self.funds += amount
    
    def withdraw(self, amount):
        self.funds -= amount
    
    def get_balance(self):
        return self.funds
    
    def get_account_number(self):
        return self._id
        
    def update(self):
        pass
    
    def __str__(self):
        return str(self.get_balance()) + ' dollars in ' + type(self).__name__
        
class CurrentAccount(Account):
    def __init__(self, customer, funds, id_manager, overdraft_limit):
        super(CurrentAccount, self).__init__(customer, funds, id_manager)
        self.overdraft_limit = overdraft_limit
        self.overdraft = False
        
    def withdraw(self, amount):
        if (self.get_balance() - amount) > -(self.overdraft_limit):
            super(CurrentAccount, self).withdraw(amount)
        else:
            "Overdrafted to limit"
        self._set_overdraft()
            
    def update(self):
        if self.overdraft:
            print("You're overdrafted!")
            
    def _set_overdraft(self):        
        if self.get_balance() < 0:
            self.overdraft = True
        else:
            self.overdraft = False

class SavingsAccount(Account):
    def __init__(self, customer, funds, id_manager, interest_rate):
        super(SavingsAccount, self).__init__(customer, funds, id_manager)
        self.interest_rate = interest_rate
        
    def add_interest(self, monthly=True):
        if monthly: 
            denominator = 12.0
        else: 
            denominator = 1.0
        self.funds += (self.funds * self.interest_rate) / denominator
        
    def update(self):
        self.add_interest()
        
class Bank(object):
    def __init__(self, name):
        self.accounts = {}
        self.customers = {}
        self.id_manager_acc = IdManager()
        self.name = name
        
    def update(self):
        for account in self.accounts.values():
            account.update()
            
    def add_customer(self, name):
        customer = Customer(name)    
        self.customers[customer.name] = customer
        
    def add_account(self, acc_type, funds, customer_name, od_lim=0, interest=0):
        customer = self.customers[customer_name]
        if acc_type == "checking":
            new_acc = CurrentAccount(customer, funds, self.id_manager_acc, od_lim)
        elif acc_type == "savings":
            new_acc = SavingsAccount(customer, funds, self.id_manager_acc, interest)
        self.accounts[new_acc._id] = new_acc
        customer.accounts.append(new_acc)
            
    def __str__(self):
        return '\n'.join([str(customer) for customer in self.customers.values()])
            