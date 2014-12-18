class Account(object):
    def __init__(self, ID, money, customer):
        self.ID = ID
        self.money = money
        self.customer = customer
        
    def deposit(self, deposit):
        self.money += deposit
        
    def withdraw(self, withdraw_amount):
        self.money -= withdraw_amount
        
    def get_balance(self):
        return self.money
        
    def get_account_number(self):
        return self.ID
        
    def update(self):
        raise NotImplementedError

class CurrentAccount(Account):
    def __init__(self, ID, money, customer, ODlim):
        super(CurrentAccount, self).__init__(ID, money, customer)
        self.ODlim = ODlim
        self.overdraft = False
        
    def withdraw(self, withdraw_amount):
        if self.overdraft == True:
            print("You are overdrafting.")
        if withdraw_amount > self.money:
            if (self.money + self.ODlim) < withdraw_amount:
                print("Cannot withdraw that much.")
                return
            self.money -= withdraw_amount
            self.overdrafted = True
            print("Withdraw successful. Overdrafted account. Balance: " + self.money)
            return
        self.money -= withdraw_amount
        print("Withdraw successful. Balance: " + self.money)
    
    def deposit(self, deposit):
        if self.overdraft == True:
            if (self.money + deposit) >= 0:
                self.money += deposit
                self.overdrafted = False
                print("Deposit successful. No longer overdrafted.")
                return
            self.money += deposit
            print("Warning: overdrafted.")
            return
        self.money += deposit
        print("Deposit successful.")
        return
    
    def update(self):
        if self.overdraft == True:
            print("GET YER REAR IN GEAR")
    
class SavingsAccount(Account):
    def __init__(self, ID, money, customer, interest):
        super(SavingsAccount, self).__init__(ID, money, customer)
        self.interest = interest
        
    def create_interest(self):
        self.money += (self.interest * self.money)
        
    def update(self):
        self.create_interest()
        
class Bank(object):
    def __init__(self, name_of_bank):
        self.name = name_of_bank
        self.sav_accs = {}
        self.curr_accs = {}
        self.customer_list = []
        self.ID = 0
        
    def update(self):
        for account in self.sav_accs.values():
            account.update()
            
        for account in self.curr_accs.values():
            account.update()
            
    def add_customer(self, customer):
        self.customer_list.append(customer)
            
    def create_account(self, account_type, name, money, OD_lim=500, interest=1):
        if account_type == 'Savings':
            for customer in self.customer_list:
                if customer.name == name:
                    account = SavingsAccount(self.ID, money, customer, interest)
                    self.ID += 1
                    self.sav_accs[account.ID] = account
        if account_type == 'Current':
            for customer in self.customer_list:
                if customer.name == name:
                    account = CurrentAccount(self.ID, money, customer, OD_lim)
                    self.ID += 1
                    self.curr_accs[account.ID] = account
            
class Customer(object):
    def __init__(self, name):
        self.name = name