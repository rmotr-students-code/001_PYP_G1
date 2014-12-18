

def getavg(*args):
    '''Returns the average of args.
    
    @param args args can be n integers or a list or both.
    '''
    numlist = []
    for item in args:
        if type(item) is int:
            numlist.append(item)  
        elif type(item) is list:
            numlist += item
        else:
            raise TypeError("Attempting to Add Unknown Type to numlist list")
    return float(sum(numlist))/float(len(numlist))
    
def pack(*args):
    return [_ for _ in args]
    

def squares(lst):
    return map(lambda x: x*x, lst)
    
def expo(lst, n=2):
    return map(lambda x: x**n, lst)

def square_of_evens(lst):
    return map(lambda x: x*x, filter(lambda x: x%2==0, lst))
    


### Books and authors
#Hey have you had any luck with this question? I started, but am kind of stuck. -Brett
#yeah, I hate how we have to design it.  I don't understand OOD well (it's def composition, 
#not inheritance), but it feels really forced and could be many-to-many OOD, so I'm struggling with that.  
#I will have it done, tho.  I just don't know that I'll do it correctly. -Mike

'''
Not crazy about the following solution, but I think for right now it's all I have.  
Hopefully Santiago can clarify some elements of this assignment, and I'll def return to fix
some problems b/w now and Sat if I have time.  Please feel free to comment/improve.
'''
class Author(object):
    def __init__(self, author, books):
        self.author = author
        self.books = books #books is a list of tuples, where tuple[0] == "author" and tuple[1] == price. this structure may be cheating, but it seems implied by the assignment.
    def oeuvre(self):
        return [tup[0] for tup in self.books]
    def get_books(self):
        return self.books

class Books(object):
    def __init__(self, instance):
        self.books = instance.get_books()
    def most_expensive(self):
        return max([tup[1] for tup in self.books])
    def total_cost(self):
        return sum([tup[1] for tup in self.books])
    def least_expensive(self):
        return min(tup[1] for tup in self.books)


'''
Create a class Point which models a 2D point with x and y coordinates. 
The Point class should have a method "distance" which receives other point and computes the distance:
'''
from math import sqrt
class Point(object):
    def __init__(self, xpoint, ypoint):
        self.point_one = xpoint
        self.point_two = ypoint
    def distance_calc(self, ref_point):
        return sqrt((self.point_one - ref_point.point_one)**2 + (self.point_two - ref_point.point_two)**2)

#p1 = Point(1,1)
#p2 = Point(1,0)
#print p1.distance_calc(p2) #== 1.0









