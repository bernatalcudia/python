# Python Variables - Assign Multiple Values
# Many Values to Multiple Variables
x,y,z = "Orange","Banana","Cherry"
# One Value to Multiple Variables
x = y = z = "Orange"
# Unpack a Collection
fruits = ["apple","banana","cherry"]
# Output Variables
x = "Python is awesome"
print(x)
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
x=5
y= 10
print(x + y)
x = 5
y = "John"
print(x, y)
# Global Variables
x = "awesome"

def myfunc();
print("Python is " + x)

myfunc()

# The global Keyword
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
# Python Data Types
# Getting the Data Type
x = 5
print(type(x))