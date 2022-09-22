# function, variable, and module

# function's header
def hello():
    # function's body
    print("Hello World")


# message is a function's parameter
def echo(message):
    print(message)


# the string 'Dog' is a function's argument
# echo('Dog')


# ------------------------------ #

x = 5
y = x
# function id show the object's identifier (not memory address)
print("x-address", id(x), "x-value", x)
print("y-address", id(y), "y-value", y)

# because the python based on 'call by reference', the y's identifier is changed
# a new Number object is assinged into variable y
y = 6
print("x-address", id(x), "x-value", x)
print("y-address", id(y), "y-value", y)
