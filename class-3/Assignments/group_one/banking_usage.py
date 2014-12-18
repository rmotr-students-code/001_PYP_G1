import banking as bn

if __name__ == '__main__':
    bank = bn.Bank("SUPERBANK")
    bank.add_customer("Bobby")
    bank.add_customer("JACK")
    bank.add_account("checking", 100, "Bobby", od_lim=50)
    bank.add_account("savings", 100, "Bobby", interest=.20)
    bank.add_account("checking", 100, "JACK", od_lim=50)
    bank.add_account("savings", 100, "JACK", interest=.20)
    bank.update()
    print(bank)