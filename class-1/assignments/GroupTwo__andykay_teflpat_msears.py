#Hey guys, just thought I'd try this thing out, so I created this file and
#did one of the assignments (was it allowed to use the built-in title()
#method?). Anyway -- be back later, and I hope we will discuss other
#assignments and finish them all. --Andy K.
import copy

# Thu 9 Oct 2014

### *mutability
def mutable_append(sequence, element):
    return sequence.append(element)
    

def immutable_append(sequence, element):
    # Here we should create a copy of the sequence
    # How to copy objects:
    # http://effbot.org/pyfaq/how-do-i-copy-an-object-in-python.htm
    # ?? What's the difference between shallow and deep copies?
    new_sequence = copy.copy(sequence) #why not a tuple, since it's a mutable type? dunno that I understand this question, tho.
    new_sequence.append(element)
    '''
    newsequence = tuple(sequence) #to change the type to an immutable type.
    newsequence = sequence[:]   #this will make a copy of the entire sequence without associating the two, so you can change newsqequence
                                #without changing sequence.  this is what I assume prof wants,
                                #in which case we should append to return newsequence.append(element)
    '''
    return new_sequence
    #Andy: honestly I'm not sure I understand the purpose of this task; I guess
    #it's just supposed to check your knowledge about (im)mutable types.
    #You're welcome to change it to the tuple thing.

#Example mutable:

l = [1, 2, 3]
mutable_append(l, 'a')
print(l)  # Should print [1, 2, 3, 'a']
    
#Example immutable:

l = [1, 2, 3]
new_l = immutable_append(l, 'a')
print(l)  # Should print [1, 2, 3]
print(new_l)  

### Camel case
def camel_case(st):
    """Returns camel case of a string."""
    return st.title() #brilliant
    
print camel_case("hello world")

### All uppercase
def uppercase(st):
    return st.upper()

print uppercase("hello")  # Should return "HELLO"

### First 2 characters
def first_2_characters(st):
    if len(st) >= 2: 
        return st[:2]
    else:
        return st #we could of course specify that the "string was empty"

def first_n_characters(st, n = None):
    if n == None:
        return first_2_characters(st)
    else:
        return st[:n]

print first_2_characters("Hello")  # Should return "He"

print first_n_characters("Hello")  # Should return "He"
print first_n_characters("Hello", 3)  # Should return "Hel"

### Every n insert
def every_3_chars_insert(a, b, n = 3):
    """receives two strings `a` and `b` and returns a new string equals to the
    string `a` plus occurences of the string `b` every 3 characters"""
    # Important note: strings are immutable -- http://stackoverflow.com/a/4023434
    # Therefore, it's impossible to insert smth. in the SAME string in loop
    # If we were to insert b just once, we could write:
    # result_str = a[:pos] + b + a[pos:] -- but we can't use it in loop
    pos = 0
    substring_list = []
    while pos < len(a):
        pos += n
        substring_list.append(a[pos-n:pos])
    return b.join(substring_list) #brilliant.
    '''
    def nchars(string, addstr, n):
        """Returns a new string with a new character (addstr) inserted every n characters of the string.
        @param string str that we iterate
        @param addstr str that we insert
        @param n int that we use to determine when to inster addstr into string.
        
        """
        return addstr.join([string[i:i+n] for i in range(0, len(string), n)])
        #I don't love my code.  It's not terribly readable without understanding slicing and iterating, 
        #but it's compact, well-abstracted, and fairly pythonic.
    '''
    # Yeah, I was amazed with my idea myself :) However, it's more of a workaround;
    # so ideas on how to do it more traditionally are welcome (say you can't
    # use this method for removing every 3rd symbol...so it's all worth a 
    # discussion)
    
print every_3_chars_insert('Hello World', '-')  # Should return "Hel-lo -Wor-ld"

### PowPow
def pow_pow(n):
    """receives an integer and returns a dictionary with the element and
    the result of the multiplication by itself, with the form `{i: (i*i)}`"""
    result_dic = {}
    i = 1
    while i <= n:
        result_dic[i] = i*i
        i += 1
    return result_dic
    #return {item: item**2 for item in range(1, n+5)} ##this would also work.  one line and a more optimized for instead of while.
    #Andy: awesome! this is something I've learnt from you today. Cheers

print pow_pow(5)  # Should return {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

def count_occurrences(seq):
    '''Returns dictionary with sequence items' respective counts.  Could also use Counter -- likely better performance.
    '''
    return {i: seq.count(i) for i in seq}

def nxtprime(n):
    '''Returns the next prime number.
    ''' #note this code isn't necessarily optomized and can potentially throw a recursion error in some corner cases.
    num = n+1
    while len([n for n in range(1,num) if num%n==0]) > 1:
        return nxtprime(num)
    return num
    # Works fine for me, I'd like to see some comments on how you got the len()
    # argument though. I'm not so experienced (solved this task a much longer way)
    #Mike: I've created a list and I'm checking the len() of that list.  List comprehensions are one of Python's
    #most powerful features IMO.  I use them everywhere (probably too much :)).  Note that we use a dictionary comprehension
    #in the count_occurrences
    # Andy: Thanks a lot! Yep, lists and dictionaries seem powerful.

def firstpayment(debt):
    '''problem: returns less than one-third the debt, so *if* the three payments were meant to be eqaul 
    installments, then it's not going to work.  Will return later to review.
    '''
    ##return debt/3 #dude's getting ripped off.
    return debt*.3333 #this gets us closer to equal payments.
    # Andy: If I got it right, the dude pays 3 bucks 30 cents 3 times, so he's fooling his mate
    # :) Or 3.33? Still not equals to 10, so there's a little "scam"

