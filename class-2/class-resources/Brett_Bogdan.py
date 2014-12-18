#Hi
def my_sum(x, y):
    return x + y
    
def subtract(x, y):
    return x - y
    
def multi(x, y):
    return x * y
    
def div(x, y):
    return x / y
    

def operation(oper, n1, n2):
    return oper(n1,n2)



assert operation(my_sum, 2, 3) == 5