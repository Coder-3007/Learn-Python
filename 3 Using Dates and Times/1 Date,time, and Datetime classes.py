#  In this lesson we will learn about Dates and time in Python


from datetime import date
from datetime import time
from datetime import datetime

def main():
    ## DATE OBJECTS
    # TODO: Get today's date from the simple today() method from the date class
    
    # it gives us todays date
    # today = date.today()
    # print("Today's date is ", today)

    # # TODO: print out the date's individual components
    
    # # Today object is assosiated with day, month , year
    # print("Date components:" ,today.day,today.month,today.year)
    
    # # TODO: retrieve today's weekday (0=Monday, 6=Sunday)
     
    # print("Today's weekday is " ,today.weekday())
    # days=["mon","tue","wed","thur","fri","sat","sun"]
    # print("Which is",days[today.weekday()])

    ## DATETIME OBJECTS
    # TODO: Get today's date from the datetime class
    
    today=datetime.now()
    print("The current date and time is",today)
    
    # TODO: Get the current time
    
    t = datetime.time(datetime.now())
    print ("the current time is ",t)
 

  
if __name__ == "__main__":
    main()