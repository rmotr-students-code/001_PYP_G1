# functions as first class objects
def my_sum(x, y):
    return x + y
    
def subtract(x, y):
    return x - y
    
# write operation function

operation(my_sum, 2, 1)  # 3
operation(subtract, 7, 2)  # 5

"""
x. Code a function that can receive either a list itself, or diferetn integer arguemnts and computes the Average:

average(1, 5, 3, 2)  # 2.75
average([1, 5, 3, 2]) # 2.75

---

x. Build a function that receives a list and returns a tuple with the first and last element on that list

---

x. Build a function that returns a arbitrary amount of params and build a list with them.

build_list(1, 5, "hello")  # [1, 5, "hello"]

---

x. Identify the max num in a list and:
  a. Return a new list with that max number repeated the same amount of times as the original list lenght
  b. Modify the list and set all the other elements to be that max value.
  
l = [1, 11, 5, 13]

max_repeated_a(l)  # [13, 13, 13, 13]
print(l)  # [1, 11, 5, 13]

max_repeated_a(l)  # None
print(l)  # [13, 13, 13, 13]

---

x. Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal
same_first_last([1, 2, 3]) → False
same_first_last([1, 2, 3, 1]) → True
same_first_last([1, 2, 1]) → True


x. Class StringConverter.

sc = StringConverter("MyString")
print(sc.upper())
print(sc.lower())

---

x. Shapes. Class Circle, square initialized with their properties. (get area)
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

---

x. Author and Book Classes. Book has title, price. Author has name and books. Think about the design. What should I ask to connect the classes?
  a. Get most expensive book from author
  b. Get sum of total cost from author.

---

x. Point class. Point initiated with x and y. Point has the method "distance".

"""
