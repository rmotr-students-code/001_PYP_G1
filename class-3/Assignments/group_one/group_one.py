from __future__ import division

### Shapes hierarchy
'''Modify our previous Shapes as follow:
    The `Shape` class should be abstract
        only one parameter, `name`
        abstract method named `area`
        method named `print_area` which would print the area message'''
        
class Shape(object):
    def __init__(self, name):
        self.name = name
    
    def area(self):
        raise NotImplementedError
        
    def print_area(self):
        print("The area of the " + type(self).__name__ + " is " + str(self.area()))
        

### Second take on our Banking program
# SEE banking.py FILE

### NamePrinter class
class NamePrinter(object):
    def __init__(self, other_obj):
        self.other_obj = other_obj
        
    def print_name(self, obj=None):
        if obj:
            print(type(obj).__name__)
        else
            print(type(self.other_obj).__name__)