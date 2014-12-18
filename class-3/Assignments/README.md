# Assignments

### Shapes hierarchy


Modify our previous Shapes exercise to include a class hierarchy as follow:

The `Shape` class should be abstract. It should have an initialization method (constructor) that
take only one parameter, `name`. All its child classes should invoke the `Shape.__init__` method
when they're initialized. The Shape class should have an abstract method
named `area` that would compute the area of the actual shape. The `Shape` class needs to implement
a method named `print_area` which would print the area of the shape along with some message.
`print_area` is only defined on the `Shape` class and should use the `area` method to print the result.

### Second take on our Banking program

Create an abstact `Account` class with the following methods:
 * `deposit`
 * `withdraw`
 * `get_balance`
 * `get_account_number`

An `Account` should have a `Customer` associated, and a `Customer` can have several accounts.

The concrete classes that we'll be using will be: `CurrentAccount` and `SavingsAccount`.
A SavingsAccount object, in addition to the attributes of an Account object, should have an
interest variable and a method which adds interest to the account. A CurrentAccount object,
in addition to the attributes of an Account object, should have an overdraft limit variable.
Ensure that you have overridden methods of the Account class as necessary in both derived classes.

Write a `Bank` class which can store instances of `CurrentAccount` and `SavingsAccount`.
A `Bank` can also have a name.

Write an `update` method in the `Bank` class. It iterates through each account, updating it
in the following ways: `SavingsAccount`s get interest added (via the method you already wrote);
`CurrentAccount`s get a letter sent if they are in overdraft.

IMPORTANT: The balance of an account may only be modified through the `deposit` and `withdraw` methods.
And both child classes can't modify them or override them.

(This exercise was delivered on class. I want you guys to take a second stab and make it really well.)

### Banking module

Create a module `banking.py` which should contain all your previous classes. The module must contain only classes,
and nothing more.
Create a second module, called `banking_usage.py` which import the classes from the `banking.py` module and:

 * Creates a `Bank`
 * Creates several accounts (both types).
 * Creates some employees
 * Perform a series of `Bank.update`s.

Again, all this work must be done on `banking_usage.py`. The only code contained in `banking.py` should be
class definitions.


### NamePrinter class

From our previous exercise, `Shape` and `Bank` have names. Write a class named `NamePrinter` which has one
method called `print_name` that will print the name of the class.
Make Shape and Bank extend from it.