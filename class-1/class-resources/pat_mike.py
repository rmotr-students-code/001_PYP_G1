from math import factorial

def times(string, times):
    # Return the `string` str a certain amount of `times`
    # times("Hello", 2) == "HelloHello"}
    # How to have a default value for times?
    return string*times


def count_evens(collection):
    # Return the number of even ints in the given collection
    return len([_ for _ in collection if _ % 2 == 0])


def big_diff(collection):
    # Return the difference between the largest and
    # smallest values in the collection
    return max(collection) - min(collection)


def derp_factorial(n):
    return factorial(n) #note that b/c of the name overlap, this is an infinite loop, as it will recursively call itself.

