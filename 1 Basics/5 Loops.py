# we cover the loops part of Python 



def main():
    x = 0

    # TODO: define a while loop
     
    # while(x < 5):
    #    print(x)
    #    x = x + 1

    # TODO: define a for loop
    
    # for x in range(5,10):
    #     print(x)

    # TODO: use a for loop over a collection

#     days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

# #   its looping over the context
#     for d in days :
#         print(d)


    # TODO: use the break and continue statements

    # the break statment is used to break the execution of a loop 
    #  if a condition is met of some reason
     
    # for x in range(5,10):
    #     if x == 7:
    #         break
    #     # it is terminating at the 7
    #     print(x)


        # for continue statement
    
    # for x in range(5,10):
    #     # for even no
    #     if x % 2 == 0:
    #         continue
    #     print(x)


    # TODO: using the enumerate() function to get index 
    
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    for i,d in enumerate(days):
        # it will return index(number) and the item(days)
        print(i , d)

if __name__ == "__main__":
    main()