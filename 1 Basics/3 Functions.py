# we will be Python functions here 




# TODO: define a basic function

def func1():
    print("I am function")

# TODO: function that takes arguments

def func2(arg1,arg2):
    print(arg1,"",arg2)

# TODO: function that returns a value

def cube(x):
    return x * x * x 
# TODO: function with default value for an argument

def power(num, x=1):
    result = 1;
    # Using for loop
    # we will loop over 
    for i in range(x):
        result = result * num
    return result


# TODO: function with variable number of arguments

def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result    

# or 

#  *args is always has to be last because it is the variable argument
def multi_add(arg1, *args):
    result = 0
    for x in args:
        result = result + x
    return result  

# func1()  it is called directly
# print(func1()) it is called in print statement
# print(func1) It dosnt print the return value so its none because function is with func1() 
# and there is no  parenthesis () in it



# func2(10,20)
# print(func2(10,20))
# print(cube(3))



# print(power(2))
# print(power(2,3))

# # I am reversing the orders
# print(power(x=3,num = 2))

# we can combine the variable in function witn different arguments
print(multi_add(4,5,6,7,8))