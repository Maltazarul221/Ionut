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


