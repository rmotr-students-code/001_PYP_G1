





class Shape(object):
    def __init__(self, name):
        self.name = name
        self.area = 0
    def calculate_area(self, base_width = 0, height = 0, radius = 0):
        '''
        NOTES: If this is a base class, should we remove all functionality and, instead, have it merely
        set the area attribute by setting the children classes' calculate_area()?
        '''
        if self.name == "Square" or self.name == "Rectangle" or self.name == "Parallelogram":
            self.area = base_width * height
    #        return self.area
        elif self.name == "Triangle":
            self.area = .5 * (base_width*height)
    #        return self.area
        elif self.name == "Circle":
            self.area = 3.14 * radius**2
    #        return self.area
        else:
            self.area = "The Shape Was Unrecognized"
            raise NameError("self.name {} is not defined".format(self.name))
    def print_area(self):
        print self.area


