import sys
print(sys.version)

#Variables
#a variable is created the moment you assign a value to it

x = 5
y = "John"

print(x)
print(y)
print("Hey John!")
print(type("Hey John!"))
print(type(x))
print(type(y))

#they don't need to be declared with any particular type, and you can change them after they have been assigned

x = 4
x = "Sally"

print(x)

#Casting
#if you want to specify the data type of variable , this can be done by casting

x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)

#Variable names
#can have a short name ( x, y ) or a more descriptive name ( age, carname , total_value )
#Rules for Python variables:

#A variable name must start with a letter or the underscore character
#A variable name cannot start with a number
#A variable name can only contain alphanumeric characters and underscores (A-z, 0-9, and _ )
#Variable names are case-sensitive (age, Age and AGE are three different variables)
#A variable name cannot be any of the Python keywords.

# Examples of variables:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Asign multiple values to variables:
# Python allows us to asign values to multiple variables in one line

x , y , z , = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One value to multiple variables:

x = y = z = "Orange"

print(x)
print(y)
print(z)

#Unpack a collection
#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables.
# This is called unpacking.

fruits = ["Apple", "Banana", "Cherry"]
x,y,z = fruits

print(x)
print(y)
print(z)

# Output variables:
# In python print() is often used to output variables:

x = "Python is awesome"
print(x)

# we can output multiple variables separeted by comma:

x = "Python"
y = "is"
z = "awesome"
print(x,y,z)

#we cal also use the operator + for the same@

x = "Python"
y = " is"
z = " awesome"
print(x + y + z)

#Global variables
#that are created outside a function (as in all the examples in the previous pages) are known as global variables.
#Global variables can be used by everyone, both inside of functions and outside.

x = "Awesome"

def myfunc():
    print("Python is " + x)

myfunc()

#If you create a variable with the same name inside a function, this variable will be local,
# and can only be used inside the function.
# The global variable with the same name will remain as it was, global and with the original value.

x = "Awesome"

def myfunc():
    x = "Fantastic"
    print("Python is " + x)

myfunc()
print("Python is " + x)

# Global Keyword
# Normally, when you create a variable inside a function, that variable is local,
# and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.
# Example:

def myfunc():
    global x
    x = "Fantastic!"

myfunc()
print("Python is " + x)

#Also, use the global keyword if you want to change a global variable inside a function.
#To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "Awesome!!"

def myfunc():
    global x
    x = "Double Awesome!!!"

myfunc()

print("Python is " + x)

#Python data types#
#Build in data types:

#Text type: str
x = "Hello World"
print(x)

#Numeric type: int
x = 20
print(x)

#Numeric type: float
x = 21.5
print(x)

#Numeric type : complex
x = 1j
print(x)

#Sequence types: list
x = ["Apple", "Banana", "Cherry"]
print(x)

#Sequence types: tuple
x = ("Apple", "Banana", "Cherry")
print(x)

#Sequence types: range
x = range(6)
print(x)

#Mapping type: dic
x = {"Name": "John", "Age": 34}
print(x)

#set type: set
x = {"Apple", "Banana", "Cherry"}
print(x)

#set type:frozenset
x = frozenset({"apple", "banana", "cherry"})
print(x)

#Boolean type: bool
x = True
print(x)

#Binary type: bytes
x = b"Hello"
print(x)

#Binary type: bytearray
x = bytearray(5)
print(x)

#Binary type: memory
x = memoryview(bytes(5))
print(x)

#None type: NoneType
x = None
print(x)

#Setting the specific data types:

x = str("Hello World")
print(x)
x = int(20)
print(x)
x = float(20.5)
print(x)
x = complex(1j)
print(x)
x = list(("apple", "banana", "cherry"))
print(x)
x = tuple(("apple", "banana", "cherry"))
print(x)
x = range(18)
print(x)
x = dict(name="John", age=36)
print(x)
x = {"apple", "banana", "cherry"}
print(x)
x = frozenset(("apple", "banana", "cherry"))
print(x)
x = bool(5)
print(x)
x = bytes(10)
print(x)
x = bytearray(12)
print(x)
x = memoryview(bytes(5))


