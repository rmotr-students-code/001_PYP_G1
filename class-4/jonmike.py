
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        #Do we have to return both x and y then?
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
        #return self.x + other #just a guess.  one sec.
    def __radd__(self, other):
        return other + self.x
        
    def __str__(self):
        return "this is the point: ({},{})".format(self.x, self.y)


#print(Point(1, 2) + Point(5, 2))

#Point(1, 2) * 3 == Point(3, 6)

#Point(3, 2) - Point(1, 1) == Point(2, 1)


with open('names.txt', 'r') as r:
    names = []
    for line in r:
        names.append(line.split()[0])
    repeatnames = [x for x in names if names.count(x) > 1]
    return repeatnames #or if we want to print each one, we would loop this list with a for loop.

    