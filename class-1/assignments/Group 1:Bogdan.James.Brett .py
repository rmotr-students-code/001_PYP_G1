# Hey guys, I hope I got your names right.

# I can take care of "PowPow", "Every n insert", "First 2 characters" if that's OK?
# I'll work on it later tonight hopefully - Jim D

# Sounds good. I can take a stab at Count occurances and next_prime - Brett


# 10/10/14 12:19AM EST
# Finished up the ones I mentioned, let me know what you guys think (still very new with this)
# Let me know if you want me to grab another few examples. - Jim D 

# All done mine. We still need someone to complete Charly's scam which we basically just need to explain so should be easy - Brett

###  Ex. 1
#mutable 
def mutable_append( collection, element ):
    collection.append( element )
    pass

test1 = [1, 2, 3]
mutable_append(test1, 4)

assert test1 == [1, 2, 3, 4] 

#imutable
def imutable_append( collection, element ):
    copy = collection[:]
    copy.append( element )
    return copy
    

test2 = [1, 2, 3]
test2_2 = imutable_append(test2, 4)

assert test2 == [1, 2, 3]
assert test2_2 == [1, 2, 3, 4]

### Ex. 2
# Camel case
def camel_case(text):
        return text.title()

### Ex. 3
# All uppercase
def uppercase(text):
    return text.upper()
    
assert uppercase("hello") == "HELLO"


### Ex. 4
# First 2 characters <-- Jim D
def first_2_characters( str ):
    return str[0:2]
    
def first_n_characters( str, n = None):
    if n == None:
        return str[0:2]
    else:
        return str[0:n]
        
#print first_2_characters("Hello")
#print first_n_characters("Hello")
#print first_n_characters("Hello", 3)

### Ex. 5
# Every n insert <-- Jim D
def every_3_chars_insert( str, div, every=3):
    return div.join(str[i:i+every] for i in xrange(0, len(str), every))
    
#print "Chrs insert 3 :" + every_3_chars_insert("+", "hello world") 
    
# I am trying to figure out this part:
#
#       str[i:i+every] for i in xrange(0, len(str), every)
#
# Could you please explain what is happening here?
# I understand that:
# .join, concatenates elemens in a collection with a given separator 
# str[i:i+every] gives you a portion of the string from i to i+n
# and xrange() creates a immutable collection with a step of every
# but how do you connect them?



### Ex. 6
# PowPow <-- Jim D

def pow_pow(num):
    numstore = {}
    for i in range(1, num+1):
        numstore[i] = i*i #MS: in python two multiplication symbols (i.e., "**") are used for pow.  * just multiplies
    return numstore

#print pow_pow(5)  # Should return {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

### Ex. 7 
# Count Occurrences

def count_occurance(list):
    count = {}
    i=0
    for i in range(len(list)):
        if list[i] in count:
            count[list[i]] += 1
        else:
            count[list[i]] = 1
    return count

#list = [1,1,1,"e","b"]
#print(count_occurance(list))


### Ex. 8
# Our beloved next_prime

def next_prime(n):
    while True:
        n += 1
        if n < 2:
            return "The next prime number will be: 2"
        else:
            for i in (2, n):
                if n%i == 0:
                    continue
                else:
                    return "The next prime number will be: " + str(n)

### Ex. 9
# Charly's scam
# I think we need to maintain state of the remainder,
# first split the ammount in 3, floor the value, substract from total
# return the floored value, next value is half of the remaider ( the floor is repeated )
# I hope you dont' mind I give it a try ( with the python doc opened :)

class Charly():
    
    def __init__(self, n):
        self.ammount = n
        self.payment = 3
        
    
    def pay(self):
        # there are 3 payments
        # devide by 3, return value
        # next time by 2, return value
        # last what is left (by 1)
        if self.payment == 0:
            return 0
        pay = int( self.ammount / self.payment )
        self.ammount = self.ammount - pay
        self.payment -= 1
        return pay
    
        
CharlyTest = Charly(10)

assert CharlyTest.pay() + CharlyTest.pay() + CharlyTest.pay() == 10
assert CharlyTest.pay() == 0

# Cool it works :) 