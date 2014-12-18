class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __mul__(self, other):
        if isinstance(other, type(self)):
            return Point(self.x * other.x, self.y * other.y)
        else:            
            return Point(self.x * other, self.y * other)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
        
    def __str__(self):
        return "Point ({}, {})".format(str(self.x), str(self.y))


print(Point(1, 2) + Point(5, 2))
print(Point(1, 2) * 3)
print(Point(3, 2) - Point(1, 1))


class IdManager(object):
    def __init__(self):
        self.cur_id = 0
        
    def get_id(self):
        an_id = self.cur_id
        self.cur_id += 1
        return an_id