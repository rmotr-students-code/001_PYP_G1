import math
import random

#I don't really know how to play roulette, so it's probably pretty messed up.
#Choose the type when you instantiate the roulette table.
#When you bet, the money you get if you win is: your money + modifier * bet money

class user:
    def __init__(self, name, money):
        user.name = name
        user.money = money
        
    def bet(self, amount):
        if self.money >= amount:
            print('Bet ' + str(amount))
            return amount
        else:
            print('Invalid bet')
            return 0
    
class roulette:
    def __init__(self, roulette_type):
        self.value = 1.0
        self.roulette_type = roulette_type
        
    def all_types(self):
        #A bunch of repeats for now, as we would need a large list otherwise. Red and black don't work.
        if self.roulette_type == 'first':
            self.value = 2.0
            return [1, 12]
        if self.roulette_type == 'second':
            self.value = 2.0
            return [13, 24]
        if self.roulette_type == 'third':
            self.value = 2.0
            return [25, 36]
        if self.roulette_type == 'low':
            self.value = 1.0
            return [1, 18]
        if self.roulette_type == 'even':
            self.value = 1.0
            return [1, 18]
        if self.roulette_type == 'red':
            pass
        if self.roulette_type == 'black':
            pass
        if self.roulette_type == 'odd':
            self.value = 1.0
            return [1, 18]
        if self.roulette_type == 'high':
            self.value = 1.0
            return [19, 36]
        if self.roulette_type == 'col1':
            self.value = 2.0
            return [1, 12]
        if self.roulette_type == 'col2':
            self.value = 2.0
            return [13, 24]
        if self.roulette_type == 'col3':
            self.value = 2.0
            return [25, 36]
        
    def run_roulette(self, amount):
        print('Type of roulette: ' + self.roulette_type)
        roulette_type_final = self.all_types()
        landed_on = random.randrange(0, 37)
        if (roulette_type_final[0] <= landed_on <= roulette_type_final[1]) == True:
            print('A winrar is you!')
            return amount * self.value
        else:
            print('You lost!')
            return -amount

name = raw_input('Enter name: ')
gambler = user(name, 100)
casino_roulette = roulette('low')
running = True

while running == True:
    print('Your current money: ' + str(gambler.money))
    bet_amount = float(raw_input('How much do you want to bet? '))
    if bet_amount > 0:
        if gambler.money >= bet_amount:
            gambler.money += casino_roulette.run_roulette(gambler.bet(bet_amount))
    else:
        print('invalid bet')
    if gambler.money <= 0:
        print('You have gone broke!')
        running = False
    