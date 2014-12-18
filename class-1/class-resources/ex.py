import math

def factorial(n):
    # return math.factorial(n)
    assert(type(n)) == int
    num = abs(n)
    result = 1
    while num > 0:
        result *= num
        num -= 1
    return result

print(factorial("hello"))  # Should print 120

