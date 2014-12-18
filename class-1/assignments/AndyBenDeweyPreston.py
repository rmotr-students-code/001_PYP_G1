from __future__ import division

### *mutability
'''def mutability(text, item):
    text.append(item)


def immutability(text, item):
    return text + [item]

list_of_things=[1,2,3]
print list_of_things
print type(list_of_things)
mutability(list_of_things,2)


print immutability(list_of_things, 488)
print type(immutability(list_of_things, 488))
print list_of_things'''

### Camel case
'''def camel_case(text):
    # list_of_words = [word[0].upper() + word[1:] for word in text.split(' ')]
    # return ' '.join(list_of_words)
    # list_of_words = [word.capitalize() for word in text.split()]
    # return ' '.join(list_of_words)
    return text.title()
    
print camel_case("test  function  and  testing  a  sentence")'''

### All uppercase
'''def uppercase(text):
    return text.upper()
    
print uppercase("this is lowercase")'''

### First 2 characters
# "slicer"[2:] = "icer"
# "live"[:2] = "li"
'''def two_char(text):
    return text[:2]
    
def n_char(text, n):
    return text[:n]    
    
print two_char("this is a string")
print n_char("this is a string", 5)'''

### Every n insert

'''def every_3_chars_insert(string, char): ##'This is a thing', '-') ## thi-s i-s a- th-ing
    static_list = list(string)
    dynamic_list = []
    # 'this is a thing'
    #'thi-' 's is a thing'
    # loop through static list        
        # add loop_element to dynamic
        # at each element, see if we're at an index that's % 3        
        # if we are % 3 add `char` to dynamic_list
    i = 0
    while i < len(static_list):
        dynamic_list += static_list[i]
        test = i+ 1
        if not test%3:
            dynamic_list += char
        i += 1    
    return ''.join(dynamic_list)     
            
print every_3_chars_insert('this is a thing', '-')  '''          

### PowPow
'''def pow_pow(num):
    num_dict = {}
    for n in range(1, num+1):
        #num_dict[n] = n**2
        num_dict.update({n:n**2})
    return num_dict
    
print pow_pow(5)'''

###  Count occurences
'''def count_occurences(new_list):
    dynamic_dict = {}
    i = 0
    for i in range(len(new_list)):
        if new_list[i] in dynamic_dict.keys():
            dynamic_dict[new_list[i]] += 1
        else: #add new_list[i] to dynamic_dict
            dynamic_dict.update({new_list[i]: 1})
    return dynamic_dict        

print count_occurences([1, 5, 'a', 3, 1, 1, 'a'])'''

### Our beloved next_prime
'''def prime(n):
    for x in range(2, n):
        if n % x == 0:
            return False
    return True

def next_prime(n):
    i = n + 1
    while True:
        if prime(i):
            return i
        i += 1 
            
print next_prime(15)'''

### Charly's scam
'''

We determined that the issue here is that $10.00/3 payments = $3.33 per payment
locally 1/3 * 3 = 1, so, programmically we can get the payments to equal 10 however...
in a real life event the lender would be losing a penny ( 3 payments $3.33 = $9.99 )

Alternatively, if we rounded up to $3.34, the person lending the money would gain 2 pennys
because 3.34 *3 = 10.02. To correct both cases to make it an even 10 we need to have a way to 
break the total amount into as equal payments as possible, but keep a running total of how much
is left over so the last payment can be 3.34. That way it's $3.33 + $3.33 + $3.34 = $10.00

'''
class loan(object):
    
    def __init__(self, amount):
        self.initial = amount
        self.balance = amount
        
    def pay(self,amount):
        self.balance -= amount
        
    
    def amount_left(self):
        return self.balance


jimmysloan = loan(10.00)

jimmysloan.pay(3.33)
jimmysloan.pay(3.33)
jimmysloan.pay(3.33)
print jimmysloan.amount_left()

