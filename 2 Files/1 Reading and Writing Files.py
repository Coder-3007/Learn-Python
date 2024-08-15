# We will learn about files in Python



def main():  
 
    # Open a file for writing and create it if it doesn't exist
   
#    myfile = open("textfile.txt" , "w+")
    
    
    # Open the file for appending text to the end
    

    # to add new thing to the existing file we use "a+"
#    myfile = open("textfile.txt" , "a+")

#     # write some lines of data to the file
    
#    for i in range(10):
#        myfile.write("this is some text\n")
    
#     # close the file when done
     
#    myfile.close()
    
    # Open the file back up and read the contents
   

#    to read the file in the terminal we use r for it
    # myfile = open("textfile.txt" , "r")
    # if myfile.mode == 'r':
    #     contents = myfile.read()
    #     print(contents)



#  To read the line in an array or list we use the same code but its the same output as the other one adds much space
# but the code is different

    myfile = open("textfile.txt" , "r")
    if myfile.mode == 'r':
        fl = myfile.readlines()
        for x in fl:
         print(x)

if __name__ == "__main__":
    main()