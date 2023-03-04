# creating variables
x = 4
y = "good morning"
print(x)
print(y)

# data types of variables
x = 4  # x is of type int
x = "good morning"  # x is now of type str
print(x)

# specify the data type of a variable (casting)
x = str(4)  # x will be '4'
y = int(4)  # y will be 4
z = float(4)  # z will be 4.0


# get the data type of a variable
x = 4
y = "good morning"
print(type(x))  # x is int
print(type(y))  # y is str

# single or double quotes
x = "good morning"
# is the same as
x = 'good morning'

# case sensitive
a = 4
A = 'good morning'
# A will not overwrite a

# variable names
name = 'Annie'
_name = 'Annie'
na_me = 'Annie'
Na_mE = 'Annie'

# assign multiple values
x, y, z = 'hi', 'hello', 'goodbye'

# one value to multiple variables
x = y = z = 'hello'
print(x)
print(y)
print(z)

# unpack a collection
fruits = ['apple', 'banana', 'cherry']  # list of fruits
x, y, z = fruits  # x is apple, y is banana, z is cherry
print(x)
print(y)
print(z)

# output variables
x = 'good morning'
print(x)
x = 'good'
y = 'morning'
print(x, y)  # prints good morning
# is the same as
print(x + y)

# + as a mathematical operator
x = 5
y = 10
print(x + y)  # prints 15
# cannot print a string and a number with the + operator

x = 4
y = 'good morning'
print(x, y)  # prints 4 good morninng

# global variables
x = 'morning'
def myfunc():
  print('good ' + x)
myfunc()
# prints good morning

# variable inside a function
x = 'morning'
def myfunc():
  x = 'night'
  print('good ' + x)  # prints good morning
myfunc()
print('good ' + x) # prints good night

# global keyword
def myfunc():
  global x
  x = 'morning'
myfunc()
print('good ' + x)
# and
x = 'morning'
def myfunc():
  global x
  x = 'night'
myfunc()
print('good ' + x) # prints good night only
