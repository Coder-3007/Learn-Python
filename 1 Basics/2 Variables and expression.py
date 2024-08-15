# Basic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries
myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, 1, 2)
mydict = {"one" : 1, "two" : 2}

# print(myint)
# print(myfloat)
# print(mystr)
# print(mybool)
# print(mylist)
# print(mytuple)
# print(mydict)

# re-declaring a variable works

# myint = "abc"
# print(myint)

# to access a member of a sequence type, use []

# print(mylist[2])
# print(mytuple[1])

# use slices to get parts of a sequence
# print(mylist[1:5])
# print(mylist[1:5:2])

# you can use slices to reverse a sequence

# print(mylist[:: -1])
# we use to reverse it 

# dictionaries are accessed via keys


# print(mydict["one"])

# ERROR: variables of different types cannot be combined

# combine two datatypes

# print("string type" +123)
# i am getting an error because python is a strong type language there are two different types

# we will use the str function to combine two different variables or datatypes


# print("string type" +str(123) )

# Now it works

# Global vs. local variables in functions

# def someFunction():
#     mystr = "def"
#     print(mystr)


# To use the global variable

def someFunction():
    global mystr
    mystr = "def"
    print(mystr)

someFunction()
print(mystr)


# I have deleted the variable my str with del
del mystr
print(mystr)

    # in python indentation matters
    # In Python, indentation refers to the use of whitespace (usually spaces or tabs) 
    # at the beginning of lines of code to define the structure of the code,
    #  particularly for defining code blocks. Unlike many other programming languages 
    # that use braces ({}) or keywords to define blocks of code, Python relies on indentation 
    # to indicate the grouping of statements.

    # Example

    # if condition:
    # # This block of code is executed if 'condition' is True
    # do_something()
    # do_another_thing()
    