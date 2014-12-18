
# ROULLETE
from random import randrange

class Game(object):
    def __init__(self, user):
        self.user = user
        
    def play(self):
        raise NotImplementedError
        
        
class Roulette(Game):
    def __init__(self, user):
        super(Roulette, self).__init__(user)
        self.roll_color = "None"
        self.number = 0
        self.even = False
        
    def roll(self):
        self.color = {0:"black", 1:"white"}[randrange(2)]
        self.number = randrange(38)
        self.even = {0:True, 1:False}[self.number % 2]
        
    def payout(self, bet, win, ratio):
        payout = 0
        if win:
            self.user.change_balance(bet*ratio)
            return bet*ratio
        else:
            return 0
        
    def play(self, bet):
        if self.user.get_balance() < bet.amount:
            return False
        self.user.change_balance(-bet.amount)
        self.roll()
        payout = 0
        if bet.color:
            payout = self.payout(bet.amount, bet.color==self.color, 2)
        if bet.number:
            payout = self.payout(bet.amount, bet.number==self.number, 35)
        if bet.even:
            parout = self.payout(bet.amount, bet.even==self.even, 2)
        return payout
        
        
class User(object):
    def __init__(self, cash):
        self.cash = cash
        
    def get_balance(self):
        return self.cash
        
    def change_balance(self, amount):
        self.cash += amount
    
        
class Bet(object):
    def __init__(self, amount, color=None, number=None, even=None):
        self.__dict__.update(locals())
        
def main():
    new_user = User(100)
    game = Roulette(new_user)
    
    print new_user.get_balance()
    game.play(Bet(new_user.get_balance(), even=True)) #bet all
    print new_user.get_balance()
    

if __name__=="__main__":
    main()