import math

def average(*args):
    if type(args[0]) is list:
        return sum(args[0]) / len(args[0])
    else:
        return sum(args) / len(args)
        
        
print average(1,2,3)
print average([1,2,3,4,5])

def pack(*args):
    return [args]
    
print pack(2,3,5,6)

def squares(nums_list):
    return [x**2 for x in nums_list]
    
print squares([1,2,4])

def powers(nums_list, power=2):
    def power_func(x):
        for n in range(power-1):
            x *= x
        return x
    return map(power_func, nums_list)
    
print powers([3,4,5], 2)

def even_powers(num_list, power=2):
    the_powers = powers(num_list, power)
    return filter(lambda x: x%2==0, the_powers)
    
print even_powers([1,2,3,4,5,6], 2)


class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi*(self.radius**2)

class Square:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return self.radius**2

class NiceShapePrinter:
    def __init__(self, shape):
        self.shape = shape
        
    def area(self):
        return "the area is " + str(self.shape.area())

print NiceShapePrinter(Circle(4)).area()


class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

class Author:
    def __init__(self, name, books):
        self.name = name
        self.books = books
    
    def get_most_expensive_book(self):
        return sorted(self.books, key = lambda x: x.price)[0]
    
    def get_total_cost_of_books(self):
        return sum([book.price for book in self.books])
        
poe = Author(name="Edgar Allan Poe", books=[Book("The Raven", 9.99), Book("The Black Cat", 2.95)])
poe.get_most_expensive_book() 
poe.get_most_expensive_book().title
poe.get_total_cost_of_books()

class Point:
    def __init__(self, *coords):
        self.coords = coords
        self.x = coords[0]
        self.y = coords[1]
        
    def distance(self, p2):
        return math.sqrt((p2.y-self.y)**2 + (p2.x-self.x)**2)
        
p1 = Point(1, 1)
p2 = Point(1, 0)
print (p1.distance(p2)) 


class Circle2:
    def __init__(self, point, radius):
        self.point = point
        self.radius = radius
        
    def area(self):
        return math.pi*(self.radius**2)
        
    def are_tangent(self, c2):
        radius_1 = c2.radius + self.radius
        radius_2 = c2.raius - self.radius
        check = (c2.point.y-self.point.y)**2 + (c2.point.x-self.point.x)**2
        if check == radius_1 or check == radius_2:
            return True
        else:
            return False
            
            
class Triangle:
    def __init__(self, points):
        self.point1 = points[0]
        self.point2 = points[1]
        self.point3 = points[2]
        
    def perimeter(self):
        sum(self._get_distances())
        
    def get_type(self):
        dists = self._get_distances()
        if all([dist == dists[0] for dist in dists]):
            return "equalateral"
            
        if max(set(dists), key=dists.count) > 1:
            return "isosceles"
        
        return "scalene"
    
    def get_area(self):
        dists = self._get_distances()
        s = (dists[0]+dists[1]+dists[2])/2
        return math.sqrt(s*(s-dists[0])*(s-dists[1])*(s-dists[2]))
    
    def _get_distances(self):
        first = self.point1.distance(self.point2)
        second = self.point1.distance(self.point3)
        third = self.point2.distance(self.point3)
        return (first, second, third)