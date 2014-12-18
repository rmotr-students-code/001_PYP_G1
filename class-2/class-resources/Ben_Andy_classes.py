class StringConverter(object):
    def __init__(self, st):
        self.st = st

    def upper(self):
        return self.st.upper()
        
    def lower(self):
        return self.st.lower()

sc = StringConverter("MyString")
    
print(sc.upper())  # "MYSTRING"
print(sc.lower())  # "mystring"

import math

class Circle(object):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        """Returns circle's area"""
        return math.pi*self.radius**2
        
c = Circle(radius=2)
print(c.area())


class Square(object):
    def __init__(self, side):
        self.side = side
        
    def area(self):
        """Returns circle's area"""
        return self.side**2

s = Square(side=3)
print(s.area())


class NiceShapePrinter(object):
    def __init__(self, shape):
        self.shape = shape


    def print_area(shape,size):
        """docstring for print_area"""
        if shape #isinstance
        
pp = NiceShapePrinter(c)
pp.print_area()
# Should print:
# Area from Circle of radius "2" is equal 12.57

pp = NiceShapePrinter(s)
pp.print_area()
# Should print:
# Area from Square of side "3" is equal 9