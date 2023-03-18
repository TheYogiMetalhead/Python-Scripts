# A data type is an attribute associated with a piece of data that tells a computer system how to interpret its value.

# Python offers raw data types to allow data to be assigned to variables or constants. The five main types which are classed as literals consist of:

# 1. Numeric

# when working with currency, you're most likely going to use the numeric type of float as it allows decimal places to be counted.

# -  Integer

# The integer class represents any non-fractional number, that is whole numbers with no decimal places. These numbers can be positive or negative, for example, 10 or -10.

# -  Float

# Floats are numbers that contain decimal places and are represented by the floats class, examples are 33.3 or 66.6.

# -  Complex number

# The complex class is used to represent complex numbers which are made up of both real and imaginary numbers, a = 10 + 10j.

# 2. Sequence

# Sequence types are classed as container types that contain one or more of the same type in an ordered list. They can also be accessed based on the index in the sequence.
List = [10, 15, 20, 25]

# -  String

# A string is a sequence of characters that is enclosed in either a single or double quotes. Strings are represented by the string class or str for short.
name = "The God-King"
type (name)
# <class 'str'>

# -  List

# Lists are a sequence of one or more different or similar types. They are essentially an array and hold any type inside square brackets. Each item can be accessed by its index.
example_list = [1, 'Howdy', 4.5, "A"]
type (example_list)
# <class 'list'>
print (example_list [1])
Howdy

# -  Tuples

# Tuples are similar to lists in many ways. They contain an ordered sequence of one or more types, but the main difference is that they are immutable. 
# This means that the values inside the tuple cannot be modified or changed. Tuples are represented by the tuple class and hold datatypes wrapped in parentheses.
example_tuple = (1, 'Howdy', 4.5, "A")
print(example_tuple[1])
Howdy

# 3. Dictionary

# Dictionary store data in a key value object structure. Each value can be accessed directly by its key. Dictionaries can also store any data type. 
# For example, suppose you declare a variable named ed and assign a dictionary to it, the dictionary contains a grouping of key value pairs. 
# The first pair is a: 22, where a is the key and 22 is a value. The second pair is b: 44.4, where b is a key and 44.4 is the value. 
# You can then output the value of 22 by accessing its key, which is a.
ed = {'a':22, 'b':44.4}
ed['a']


# 4. Boolean

# Combined with logical operators, Booleans are used to check whether a condition is true or false. In this example, I'm checking the underlying data type of the values true and false. 
# The class bool is returned, meaning it is Boolean.
type (True)
# <class 'bool'>
type (False)
# <class 'bool'>

# 5. Set

# Set  is an unordered and non-indexed collection of non-repeated values. Let me demonstrate an example of this data type. Suppose I assign a set of four items to the variable named example set. 
# I then check the type of the value stored in the example set variable by passing it to the type function. Python reports that the underlying data type that the example set variable holds is a set.
example_set = {1, 'hello', 4.5, "A"}
type(example_set)
# <class 'set'>

# Whenever you declare a variable in Python, the datatype is automatically assigned for you based on the value of that variable. Let me demonstrate this by typing a variable called a and assigning it to a value of 10. 
# To check the data type that has been assigned by Python, I select Print and use the type function. I then pass in the variable a as the parameter and click on "Run". 
a = 10.0
print(type(a))
# # <class 'float'>
# From the output on the terminal, I can see a class of floats was assigned because there was a decimal place.

# Another
a = 10
print (type(a))
# <class 'int'>

# Another
c = 'asdf'
print (type (c))
# <class 'str'>
