class Animal(object):
    TYPE = "Animal"

    def __init__(self, name, color, height):
        self.name = name
        
    def speak(self):
        print("I'm a " + self.TYPE)


class Duck(Animal):
    TYPE = "Duck"
    
    def __init__(self, name, spec):
        super(Duck, self).__init__(name, "red", height)
        
        self.color = color
    
    def speak(self):
        super(Duck, self).speak()
        print("Quack!")


donald = Duck("Donald")
donald.speak()
# I'm a Duck
# Quack!