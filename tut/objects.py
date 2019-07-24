import tut.pluralsight


def banner(border='-'):
    message = input("Type stuff: ")
    line = border * len(message)
    print(line)
    print(message)
    print(line)


def get_type():
    print(tut.pluralsight.__name__)


def get_type(arg):
    print(type(arg))


if __name__ == "__main__":
    banner("-")
    get_type()


# variabilele sunt referinte catre objects
# scopes:
#   Local - inside the current function
#   Enclosing - any and all enclosing functions
#   Global - top level of module
#   built-in

'''
named references to objects
id() returns unique constant identifier
is determines equality
== determines equivalence
function arguments are passed by reference
reference is lost if a formal function argument is rebound
default arguments evaluated ones when def is executed
dynamic typing
global references ca be read from local scome - global keyword
everything is an object
import and def result in binding to maned references
type() can be used to determine object tyoe
dir() - introspect an object and get its attributes

'''