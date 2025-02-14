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
# Setting the Data Type
# string
x = "Hello World
# int
x=20
# float
x = 20.5
# complex
x = 1j	
# list
x = ["apple","banana","cherry"]
# tuple
x =("apple","banana","cherry")
# range
x = range(6)
# dict
x = {"name":"John","age":36}
# set
x = {"apple","banana","cherry"}
# frozenset
x = frozenset({"apple", "banana", "cherry"})	
# bool
x = True
#bytes
x = b"Hello"
# bytearray
x = bytearray(5)	
# memoryview
x = memoryview(bytes(5))	
# x = None	
x = None	
# Setting the Specific Data Type
x = str("Hello World")	
x = int(20)	
x = float(20.5)	
x = complex(1j)	
x = list(("apple", "banana", "cherry"))	
x = tuple(("apple", "banana", "cherry"))	
x = range(6)	
x = dict(name="John", age=36)	
x = set(("apple", "banana", "cherry"))	
x = frozenset(("apple", "banana", "cherry"))	
x = bool(5)	
x = bytes(5)	
x = bytearray(5)	
x = memoryview(bytes(5))	