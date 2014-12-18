1. Class StringConverter.

    sc = StringConverter("MyString")
    print(sc.upper())  # "MYSTRING"
    print(sc.lower())  # "mystring"

2. Shapes. Class Circle, square initialized with their properties. (get area)
Also create a NiceShapePrinter class.

    c = Circle(radius=2)
    print(c.area())

    s = Square(side=3)
    print(s.area())

    pp = NiceShapePrinter(c)
    pp.print_area()
    # Should print:
    # Area from Circle of radius "2" is equal 12.57

    pp = NiceShapePrinter(s)
    pp.print_area()
    # Should print:
    # Area from Square of side "3" is equal 9
    
    
    s.__class__.__name__  # "Square"
    c.__class__.__name__  # "Circle"
    
    isinstance(c, Circle)  # True
    isinstance(c, Squre)  # False
    