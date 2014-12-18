#import string
from . import string

from decimal import Decimal

shared_global_variable = []

#__all__ = ['my_fun']


def my_fun():
    print("MY FUN")


def my_other_fun():
    print("Shouldn't see me")


__CONST = 1