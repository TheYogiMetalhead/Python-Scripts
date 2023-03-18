# Functions

# A function is a piece of code that performs a unit of work, so far I have encountered the print() function, which outputs a message to the screen.

# Keywords

# A keyword is a reserved word in a programming language that performs a specific purpose, examples are:
# Values: True, False, None
# Conditions: if, elif, else
# Logical operators: and, or, not
# Loops: for, in, while, break, continue
# Functions: def, return  

# Arithmetic operators

# Python can calculate numbers using common mathematical operators, along with some special operators, such as:
# x + y           Addition + operator returns the sum of x plus y
# x - y           Subtraction - operator returns the difference of x minus y
# x * y           Multiplication * operator returns the product of x times y
# x / y           Division / operator returns the quotient of x divided by y
# x**e            Exponent ** operator returns the result of raising x to the power of e 
# x**2            Square expression returns x squared
# x**3            Cube expression returns x cubed
# x**(1/2)        Square root (½) or (0.5) fractional exponent operator returns the square root of x
# x // y          Floor division operator returns the integer part of the integer division of x by y
# x % y           Modulo operator returns the remainder part of the integer division of x by y

# Order of operations

# The order of operations are to be calculated from left to right in the following order: 

# Parentheses ( ), { }, [ ]
# Exponents xe   (x**e)
# Multiplication * and Division /  
# Addition + and Subtraction -    

# The PEMDAS mnemonic device may be helpful in remembering the order.

# Syntax for printing a string of text
print("I love Python!")


# Syntax for printing numeric values
print(360)
print(32*45)


# Syntax for printing the value of a variable
value = 8*6
print(value)

# Multiplication, division, addition, and subtraction
print(3*8/2+5-1)
 
# Exponents
print(4**6) # Syntax means 4 to the power of 6
print(4**2) # To square a number
print(4**3) # To cube a number
print(4**0.5) # To find the square root of a number

# To calculate how many different possible combinations can be
# formed using a set of "x" characters with each character in "x"
# having "y" number of possible values, you will need to use an 
# exponent for the calculation:
x = 4
y = 26
print(y**x)

# Assignment of values to the variables:
years = 10
weeks_in_a_year = 52
# This variable is assigned an arithmetic calculation:
weeks_in_a_decade = years * weeks_in_a_year
# Prints the calculation stored in the "weeks_in_a_decade" variable:
print(weeks_in_a_decade)

# In Python, text in between quotes -- either single or double quotes -- is a string data type. An integer is a whole number, without a fraction, 
# while a float is a real number that can contain a fractional part. For example, 1, 7, 342 are all integers, while 5.3, 3.14159 and 6.0 are all floats. 
# When attempting to mix incompatible data types, you may encounter a TypeError. You can always check the data type of something using the type() function.

# Terms

# expression - a combination of numbers, symbols, or other values that produce a result when evaluated

# data types - classes of data (e.g., string, int, float, Boolean, etc.), which include the properties and behaviors of instances of the data type (variables)

# variable - an instance of a data type class, represented by a unique name within the code, that stores changeable values of the specific data type

# implicit conversion - when the Python interpreter automatically converts one data type to another

# explicit conversion - when code is written to manually convert one data type to another using a data type conversion function:

# str() - converts a value (often numeric) to a string data type

# int() - converts a value (usually a float) to an integer data type

# The following lines assign the variable to the left of the = 
# assignment operator with the values and arithmetic expressions 
# on the right side of the = assignment operator.
hotel_room = 100
tax = hotel_room * 0.08
total = hotel_room + tax
room_guests = 4
share_per_person = total/room_guests 
 
# This line outputs the result of the final calculation stored
# in the variable "share_per_person"
print("Each person needs to pay: " + str(share_per_person)) # change a data type

# The following 5 lines assign strings to a list of variables.
salutation = "Dr."
first_name = "Prisha"
middle_name = "Jai"
last_name = "Agarwal"
suffix = "Ph.D."
 
print(salutation + " " + first_name + " " + middle_name + " " + last_name + ", " + suffix) 
# The comma as a string ", " adds the conventional use of a comma plus a 
# space to separate the last name from the suffix.
 
# Alternatively, you could use commas in place of the + connector:
print(salutation, first_name, middle_name, last_name,",", suffix)
# However, you will find that this produces a space before a comma within a string.

print("5 * 3 = " + (5*3)) 
 
# Resolution: 
# print("5 * 3 = " + str(5*3))
#
# To avoid a type error between the string and the integer within the
# print() function, you can make an explicit data type conversion by
# using the str() function to convert the integer to a string.  

numerator = 7
denominator = 0   # Possible resolution: Change the denominator value 
result = numerator / denominator
print(result)
 
# One possible assumption for a number divided by zero error might
# include the issue of a null value as a denominator (could happen when
# using a loop to iterate over values in a database). In such cases, the
# desired outcome may be to leave the numerator value intact. The
# numerator value can be preserved by reassigning the denominator with 
# the integer value of 1. The result would then equal the numerator.


float() - converts a value (usually an integer) to a float data type
