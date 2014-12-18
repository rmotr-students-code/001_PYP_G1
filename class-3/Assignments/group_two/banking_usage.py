import banking

if __name__ == '__main__':
    bank_of_austria = banking.Bank('Bank of Austria')
    Bob = banking.Customer('Bob')
    Jim = banking.Customer('Jim')
    bank_of_austria.add_customer(Bob)
    bank_of_austria.add_customer(Jim)
    bank_of_austria.create_account('Savings', 'Bob', 5000, 5, 2)
    bank_of_austria.create_account('Current', 'Jim', 123, 1234)
    bank_of_austria.update()