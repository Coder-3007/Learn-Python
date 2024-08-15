# We will learn about the os paths 


import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():

    # > Print the name of the OS
    
#     print(os.name)
    
#     #  > Check for item existence and type

#     # we will check if the textfile.txt exists or not
    
#     print("Item exists" , str(path.exists("textfile.txt")))
    
#     # whether is a file or not
   
#     print("Item is a file: " , path.isfile("textfile.txt"))

#     # to whether it is directory or not

#     print("Item is a directory/folder: " , path.isdir("textfile.txt"))

    
#     # >  Work with file paths
   
#     print("Item's path" , path.realpath("textfile.txt"))

#    # using the split function to seperate the filename from the path

#     print("Item's path" ,path.split(path.realpath("textfile.txt")))    
    
    # > Get the modification time
     
#    getmtime means get modification time

     t = time.ctime(path.getmtime("textfile.txt"))
     print(t)

    #  Getting the readible time

     print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

    # > Calculate how long ago the item was modified
 

#  taking the current time and subtracting the modification time

     td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
     print("It has been" ,td , "since the file was modified")
    #  it will create the amount of time 
     print("or,",td.total_seconds(),"seconds")

  
if __name__ == "__main__":
    main()