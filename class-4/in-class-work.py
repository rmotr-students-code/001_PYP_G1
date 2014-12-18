from package_A.subpackage_B.module_C import __CONST


print(__CONST)

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point({x}, {y})".format(x=self.x, y=self.y)


Point(1, 2) + Point(5, 2) == Point(6, 4)
Point(1, 2).__add__(Point(5, 2))
#   ^self             ^other

import random


class User(object):
    GENERATED_IDS = []

    @classmethod
    def generate_unique_id(cls, _max=1000):
        while True:
            _id = random.randint(0, _max)
            if _id not in cls.GENERATED_IDS:
                cls.GENERATED_IDS.append(_id)
                return _id

    @staticmethod
    def email_is_valid(email):
        pass

    def __init__(self, name, email):
        if not User.email_is_valid(email):
            raise AttributeError("The email you provided is not valid")

        self.id = User.generate_unique_id(100)
        self.name = name
        self.email = email


User.email_is_valid("tom@gmail.com")
usr = User("Tom", "tom@gmail.com")





"""
Interface:

Point(1, 2) + Point(5, 2) == Point(6, 4)

Point(1, 2) * 3 == Point(3, 6)

Point(3, 2) - Point(1, 1) == Point(2, 1)
"""