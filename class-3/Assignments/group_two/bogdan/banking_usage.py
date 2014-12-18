from banking import Bank, Account, SavingsAccount, CurrentAccount, Client


bank1 = Bank("Bogdan's Bank")

bogdan = Client("bogdan")

account1 = SavingsAccount(bogdan)
account1.deposit(2000)
assert account1.get_balance() == 2000

account1.withdraw(1000)
assert account1.get_balance() == 1000

#trying negative balance
assert account1.withdraw(1050) == False
assert account1.get_balance() == 1000

# add some interest
account1.calculate_interest()
account1.add_interest()

assert account1.get_balance() > 1000

account1_money_after_fisrt_interest = account1.get_balance()

account2 = CurrentAccount(bogdan)
account2.deposit(2000)
assert account2.get_balance() == 2000

account2.withdraw(1000)
assert account2.get_balance() == 1000

#shoud have something printed
account2.withdraw(2051421)

#get some negative balance for the bank test
account2.withdraw(1500)


superBank = Bank("Big bad bank", [account1, account2])

superBank.update()
#should get a letter to current account, cause it has negative balance
#and the account 1 shoud have more money

assert account1_money_after_fisrt_interest < account1.get_balance()

