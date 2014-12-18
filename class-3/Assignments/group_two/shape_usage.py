from group_two import Shape, NamePrinter

shape1 = Shape('Oddly strange shape')
#shape1.print_area()
np = NamePrinter(shape1)
#    ^--- why does this print the class's name even without np.print_name() called?

