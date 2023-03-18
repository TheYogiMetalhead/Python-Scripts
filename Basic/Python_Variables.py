# Variables allow you to work with and manipulate data.
# Variables are easy enough (It would seem) as you just need to define a name and assign it a value.

# In its simplest form, it is just this:

x = 666
print(x)

# Another form of naming is called camelCase, which looks like this:

myName = 'The God-King'
print(myName)

# Alternatively there is snakeCase, which looks like this:

my_name = 'The God-King 2.0'
print(my_name)

# You can declare multiple variables and assign them to a single value as well, such as:

a = b = c = 10
print(a)
print (b)
print(c)

# Another option one has is to do multiple assignments, such as:

d,e,f = 20,30,40
print(d)
print (e)
print (f)

# A variable is subject to change. Throughout the life cycle of a program, you will make changes to the value or the assignment of the variable itself, such as:

g = 50
print(g)
g = 60
print(g)

# Deleting a variable. My variable, with a value, has been printed, under that add a delete command, or del, followed by printing the variable. The value is first given us 70 because the variable still existed, but after the deletion, it shows an error saying that a is not defined.

h = 70
print(h)
del h
print(h)
