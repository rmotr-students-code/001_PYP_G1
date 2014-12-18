### Shapes hierarchy
import math



class NamePrinter(object):
    def __init__(self, name="No name"):
        self.name = name
    def print_name(self):
        print self.name




class Shape(NamePrinter):
    def __init__(self, name):
        self.name = name
    def area(self):
        return self.area # shoud have implemented
    def print_area(self):
        print "I am " + self.name + " and I have an area of " + str(self.area)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.area = radius ** 2 * math.pi
        super(Circle, self).__init__("Circle")
        
class Square(Shape):
    def __init__(self, side):
        self.side = side
        self.area = side ** 2
        super(Square, self).__init__("Square")
    
        

# t1 = Circle(10)
# t1.print_area()

# t2 = Square(5)
# t2.print_area()



### Second take on our Banking program


##
## Defining accounts
## 
class Account(NamePrinter):
    ID = 0
    def __init__(self, customer):
        self.id = Account.ID
        Account.ID += 1

        self.name = customer.name
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
    def __init__(self, customer):
        super(SavingsAccount, self).__init__(customer)

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
    def __init__(self, customer):
        super(CurrentAccount, self).__init__(customer)
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
    def __init__(self, name, accounts):
        self.name = name
        self.accounts = accounts
    
    def add_account(self, account):
        self.accounts.append(account)
    
    def update(self):
        # get every object and call update on them
        for account in self.accounts:
            account.update()
            
            
            
            
#Lets test:


#create a customer
bogdan = Client("bogdan")
#should be called bogdan
assert bogdan.name == "bogdan"

#create 1 account
account1 = CurrentAccount(bogdan)

#add 1000
account1.deposit(1000)
assert account1.get_balance() == 1000

#get 500
account1.withdraw(500)
assert account1.get_balance() == 500

#get more than allowed ( > -1000 )
account1.withdraw(2000)
assert account1.get_balance() == 500, account1.get_balance()
#got the good message

#get a negative balance for the bank test
account1.withdraw(1000)
assert account1.get_balance() == -500

# Current account works as expected
##########################################################

#create account2 ( a savings account ) 

account2 = SavingsAccount(bogdan)

#add 1000
account2.deposit(1000)
assert account2.get_balance() == 1000

#get 500
account2.withdraw(500)
assert account2.get_balance() == 500

#banalce cannot be negative
assert account2.withdraw(501) == False

# test add calculate + add interest
account2.calculate_interest()
assert account2.interest_rate > 0 

# see if it adds the interest
account2.add_interest()
# the interest rate is about 2.5
assert account2.get_balance() > 500


## Savings account works as expected
#########################################################

#testing bank

bank1 = Bank(bogdan, [account1, account2])

# should have some accounts
assert len(bank1.accounts) == 2

# test update method
bank1.update()
#should have a message from current account cause is negative
#account2 should have about more than 505 ( cause the interest rate last time was 2.5)
assert account2.get_balance() > 505




### Teting the Nmae
#######################

c1 = Circle(2)
c1.print_name()

bogdan2 = Client("bogdan")
account3 = SavingsAccount(bogdan2)
account3.print_name()