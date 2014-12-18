import math

"""
### Average

Write a function that can either receive a list or different integer arguemnts and computes the Average:
"""
from __future__ import division # see http://stackoverflow.com/questions/17470883/how-to-round-to-two-decimal-places-in-python-2-7

def average(*args):
    if type(args[0]) is list:
        return sum(args[0]) / len(args[0])
    else:
        return sum(args) / len(args)

print average(1, 5, 3, 2)  # 2.75
print average([1, 5, 3, 2]) # 2.75

"""
### Pack

Write a function that receives an arbitrary amount of params and build a list with them
"""
def build_list(*args):
    return [x for x in args]

#def build_list(*args):
#    return list(args)

print build_list(1, 5, "hello") # == [1, 5, "hello"]

"""
### Map squares

Write a function called squares that receives a list and returns the square of the elements. You MUST use the `map()`* function and lambdas.
"""
def squares(input_list):
    return map((lambda x: x**2), input_list)

print squares([1, 2, 3]) # == [1, 4, 9]

"""
### Map pows

Modify your previous function to receive one more argument "power" which should be optional (default to 2) that will be the power to raise each element on the list. Again, you MUST use `map()`* and lambdas.
"""
def exponentiation(input_list, power = 2):
    return map((lambda x: pow(x,power)), input_list)

print exponentiation([1, 2, 3], 3) # == [1, 8, 27]

"""
### Square of evens

Write a function which receives a list of ints and returns a new list with the squares of the even numbers. You MUST use `map()`, `filter()`* and lambdas.
"""
def square_of_evens(input_list):
    return map((lambda x: x**2), filter((lambda x: x % 2 == 0), input_list))

print square_of_evens([1,2,3,4,5,6,7,8,9,10]) # == [4, 16, 36, 64, 100]


""" 
All of the circle, square and NiceShapePrinter functions. (hello)
"""

class Circle:
    def __init__(self, radius):
        self.measurement = radius
        self.shape_type = 'Circle'
        self.line_type = 'Radius'
    
    def area(self):
        return ((self.measurement * self.measurement) * (math.pi))
        
class Square:
    def __init__(self, side):
        self.measurement = side
        self.shape_type = 'Square'
        self.line_type = 'Side'
        
    def area(self):
            return self.measurement * self.measurement
            
class NiceShapePrinter:
    def __init__(self, shape):
        self.shape = shape
        
    def print_area(self):
        return 'Area from ' + self.shape.shape_type + ' of ' + self.shape.line_type + ' ' + str(self.shape.measurement) + ' is equal to ' + str(self.shape.area()) + '.'
		
		
#
# Guys if you have any questions please leave a comment and I will explain what I did.
#


### Books and authors

class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price
    

class Author:
    def __init__(self, name, books):
        self.name = name
        self.books = books
        self.sortBooks()
    
    def addBook(self, book):
        self.books.append(book)
        self.sortBooks()
        
    def get_most_expensive_book(self):
        return self.books[ len(self.books) - 1 ]

    def sortBooks(self):
        self.books = sorted( self.books, key=lambda book: book.price )
        
    def get_total_cost_of_books(self):
        total = 0
        for book in self.books:
            total += book.price
        return total

### Geometry

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, o):
        ab = abs( self.x - o.x )
        ac = abs( self.y - o.y )
        bc = (ab ** 2 + ac ** 2) ** 0.5
        return bc

p1 = Point(1, 1)
p2 = Point(1, 0)

#print p1.distance(p2)


# Modify your Circle class to receive a Point and a radius. Interface:

class Circle2:
    def __init__(self, point, radius):
        self.point = point
        self.radius = radius
    def are_tangent(self, circle):
        distance = self.point.distance(circle.point)
        #if the distance is equal or less with the sum of the radious then they touch
        return distance == self.radius + circle.radius
        
        
c2_1 = Circle2(Point(0, 0), radius=1)
c2_2 = Circle2(Point(2, 0), radius=1)

#shoud be tangent
#print c2_1.are_tangent(c2_2)


### Geometry Triangle


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.ab = a.distance(b)
        self.ac = a.distance(c)
        self.bc = b.distance(c)
    def get_perimeter(self):
        return self.ab + self.ac + self.bc
    def get_type(self):
        if (self.ab + self.bc + self.ac) / 3 == self.ab: #isosceles
            return "equilateral";
        elif self.ab == self.ac or self.ab == self.bc or self.ac  == self.bc:
            return "isosceles";
        else:
            return "scalene"
    def area(self): 
        s = self.get_perimeter() / 2 #semiperimeter
        return (s * ( s - self.ab ) * ( s - self.ac ) * ( s - self.bc ) ) ** 0.5 # Heron's formula

t1 = Triangle(Point(0,0), Point(2,0), Point(1, 1))

#print t1.get_perimeter()
#print t1.get_type()
#print t1.area()




