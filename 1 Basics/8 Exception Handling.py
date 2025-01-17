# we will about exception handling in Python




# Exceptions provide a way of catching errors and then handling them in 
# a separate section of the code to group them together
try:
    x = 10 / 0
except:
    print("Well that didn't work!")

# You can also catch specific exceptions
try:
    answer = input("What should I divide 10 by?")
    num = int(answer)
    print(10 / num)
except ZeroDivisionError as e:
    print("You can't divide by zero!")
except ValueError as e:
    print("You didn't give me a valid number!")
    print(e)
finally:
    print("The code always runs")