
def say_hello(name):
    print("Hello " + name)


def say_hello_named_params(name=None):
    if name:
        print("Hello " + name)
    else:
        print("Hello stranger")


def say_hello_named_params_mixed(times, name=None):
    if name:
        print("Hello " + name + ("!" * times))
    else:
        print("Hello stranger" + ("!" * times))


def say_hello_variable_args(*args):
    print("Hello " + ", ".join(args))
    
print("Hello world")