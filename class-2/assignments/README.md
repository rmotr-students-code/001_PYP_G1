# Assignments

### Average

Write a function that can either receive a list or different integer arguemnts and computes the Average:

Example:

    average(1, 5, 3, 2)  # 2.75
    average([1, 5, 3, 2]) # 2.75

### Pack

Write a function that receives an arbitrary amount of params and build a list with them.

Example:

    build_list(1, 5, "hello") == [1, 5, "hello"]

### Map squares

Write a function called squares that receives a list and returns the square of the elements. You MUST use the `map()`* function and lambdas.

Example:
    
    squares([1, 2, 3]) == [1, 4, 9]

### Map pows

Modify your previous function to receive one more argument "power" which should be optional (default to 2) that will be the power to raise each element on the list. Again, you MUST use `map()`* and lambdas.

    exponentiation([1, 2, 3], power=3) == [1, 8, 27]
    
### Square of evens

Write a function which receives a list of ints and returns a new list with the squares of the even numbers. You MUST use `map()`, `filter()`* and lambdas.

Example:

    square_of_evens([1,2,3,4,5,6,7,8,9,10]) == [4, 16, 36, 64, 100]

(*) map and filter are key functions in the functional paradigm. The Well known model MapReduce(http://en.wikipedia.org/wiki/MapReduce) invented by Google uses those function as foundational parts.

### Shapes again

Continue our previous assignment. Finish the Shapes exercise. This is the interface:

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

Hint:

    s.__class__.__name__  # "Square"
    c.__class__.__name__  # "Circle"
    isinstance(c, Circle)  # True
    isinstance(c, Squre)  # False

### Books and authors

Create Author and Book classes. A Book has title and price. An Author has name and a list of books. Think about the design. How would both classes relate?
  a. Get most expensive book from author
  b. Get sum of total cost from author.

    poe = Author(name="Edgar Allan Poe", books=[Book("The Raven", 9.99), Book("The Black Cat", 2.95)])
    poe.get_most_expensive_book()  == Book("The Raven", 9.99)
    poe.get_most_expensive_book().title == "The Raven"
    poe.get_total_cost_of_books() == 12.94
    
### Geometry

Create a class Point which models a 2D point with x and y coordinates. The Point class should have a method "distance" which receives other point and computes the distance:

    p1 = Point(1, 1)
    p2 = Point(1, 0)
    p1.distance(p2) == 1
    
### Geometry circle

Modify your Circle class to receive a Point and a radius. Interface:

    c1 = Circle(Point(2, 3), radius=2)
    c2 = Circle(Point(3, 2), radius=2)

Add a method `are_tangent` that receives other cirlce and computes if the circles are tangent (http://en.wikipedia.org/wiki/Tangent_circles).

### Geometry Triangle

Create a class Triangle which models a triangle with 3 vertices. It should also use your Point class. The class should implement the following methods:

* `get_perimeter` method that returns the length of the perimeter.
* `get_type`, which returns "equilateral" if all the three sides are equal, "isosceles" if any two of the three sides are equal, or "scalene" if the three sides are different
* `get_area` that computes the area of the triangle.

Example:

    t = Triangle(Point(1, 0), Point(3, 0), Point(2, 2))
    t.get_type() == 'isosceles'

