def times(string, times):
    # Return the `string` str a certain amount of `times`
    # times("Hello", 2) == "HelloHello"}
    # How to have a default value for times?
    word = string
    for i in range(0, times):
        print(word)
    pass


def count_evens(collection):
    # Return the number of even ints in the given collection
    
    evenNumbers = []
    for number in range(0, collection):
        if(number % 2 == 0):
            evenNumbers.append(collection[number])
    return len(evenNumbers)
    

def big_diff(collection):
    # Return the difference between the largest and
    # smallest values in the collection
    sml = 9999999
    lrg = -9999999
    for i in range(0, collection):
        if collection[i] > lrg:
            lrg = collection[i]
        elif collection[i] < sml:
            sml = collection[i]
        else:
            pass
            
    dif = lrg-sml
    print("The difference between the largest and the smallest values is: " + dif) 
    pass


def factorial(n):
    pass

