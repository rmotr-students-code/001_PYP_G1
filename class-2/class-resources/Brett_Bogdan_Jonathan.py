import math

class StringConverter(string):
    
    print(string.upper())
    print(string.lower())
    
    def __init__(self, string):
        self.s = string
    
    def upper(self):
        return self.s.upper()
        
    def lower(self):
        return self.s.lower()

test1 = StringConverter("hello")

print(test1.upper())

# the init funciton gets the arguments, no?
#




class Circle(object):
        def __init__(self, radius):
            self.radius = radius
        
        def area(self):
            area = (math.pi) * (self.radius**2)
            return round(area, 2)
            

c = Circle(radius = 2)
print (c.area())


class Square():
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
        

class NiceShapePrinter(object):
    def __init__(self, shape):
        self.shape = shape
        
    def print_area(shape, variable):
        if shape.__class__.__name__ == 'Circle':
            return 
        
        if shape.__class__.__name__ == 'Square'