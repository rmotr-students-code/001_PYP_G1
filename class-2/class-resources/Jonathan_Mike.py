
def my_sum(x, y):
    return x + y
    
def subtract(x, y):
    return x - y

def operation(func, x, y):
    return func(x, y)
    
operation(my_sum, 4, 3)

#Do you know how to do it with the *args system?
#For example my_sum taking an unlimited number of variables. Okay sounds good
#let me try in my console. it could be very simple, cuz *args is a tuple and a tuple can call the func object.  one sec.
#I've got it working but it breaks the original.  I will paste below.  If users want to sum, two numbers then
#they will need to pass in a collection

'''
def my_sum(nums):
    num = 0
    for item in nums:
        num += item
    return num
    
def subtract(x, y):
    return x - y

def operation(func, *args):
    print args
    return func(args)   
print operation(my_sum, 4, 3, 5, 6) # == 18
'''