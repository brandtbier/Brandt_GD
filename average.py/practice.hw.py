#Brandt Bier
#HW 1/31
#practice exercizes 

#exersize 1: indentation
from distutils.log import ERROR


if 5 > 2:
    print("five is greather than two!")
if 5 > 2:
    print("five is greather than two!")
    
#exersize 2: variables
x = 5
y = "hello, world"

#exersize 3: comments
#This is a comment
print("hello, world")
print("hello, world") #this is a comment
#print(hello, world)
print("hello, world")

#exersize 4: Multi line comments
#this is a comment 
#written in 
#more than just one line
"""
this is a comment
written in 
more than one line
"""
print("hello, world")

#Exersize 4: Variables
x = 5
y = "John"
print(x)
print(y)
x =4        #x is type of int
x ="Sally"  #x is now type of str

#exersize 5: Casting
x = str(3)     #x will be '3'
y = int(3)     #y will be 3 
z = float(3)   #z will be 3.0

#Exersize 5: Get the Type
print(type(x))
print(type(y))

#exersize 6: Single or Soube Quotes?
x = "john"
#is the same as 
x = 'john'

#exersize 7: Case-Sensitive
a = 4
A = "sally"
#A will not overwrite a

#exersize 8: Variable names
myvar = "john"
my_var = "john"
_my_var = "johm"
myVar = "john"
MYVAR = "john"
myvar2 = "john"


"""
techniques you can use to make one word variables more readable:


 Camel Case: myVariableName-each word eept the first start with a capital letter

 Pascal Case: MyVariableName-each word starts with a capital letter

 Snake Case: my_variable_name-each word is seperated by an underscore
 """


#exersize 9: Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#exersize 10: One Value to Multiple Variables
x = y = z = "Orange"

#exersize 11: Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#exersize 12: Output Variables
    #the "print" statement is often used to output variables
    #to combine both text and a variable use the + character
x = "awesome"
print("Python is " + x)
           x = "Python is"
           y = "awesome"
           z =  x + y
           print(z)
                        x = 5
                        y = 10
                        print(x + y)
#you cant combine a string and a number
x = 5
y = "John"
print(x + y)
    print("ERROR")

#exersize 14: Global Variables
    #global variables are variables outside of a function
    #so we know what they are they just dont really have
    #a purpose besides text/ "print"

    x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

    #If you create a variable with the same name inside a function, this 
    #will be local, and can only be used inside the function. The global 
    #variable with the same name will remain as it was, global and with 
    #the original value

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


#exersize 15: The Global Keyword
     #Normally, when you create a variable inside a function, that variable is local, and 
     #can only be used inside that function. To create a global variable inside a function, 
     #you can use the global keyword. You can also use the global keyword if you want to 
     #change a global variable inside a function.
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
        #To change the value of a global variable inside a function,
        #refer to the variable by using the global keyword
        x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#exersize 16: Built-in Data Types
'test type' str
'numeric types' int, float, complex
'sequence types' list, tuple, range
'mapping type' dict
'set types' set, frozenset
'boolean type' bool
'bianary types' bytes, bytearray, memoryview

#exersize 17: Python Numbers
  -int
  -float
  -complex
 
x = 1    # int
y = 2.8  # float
z = 1j   # complex


#floats: A number, positive or
#negative, containing one or 
# more decimals.
print(type(x))
print(type(y))
print(type(z))

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

import random

print(random.randrange(1, 10))

#exersize 18L Casting

#intigers
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

#floats
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

#strings
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'