 # We learn that how a file retrieve data from the internet in Python

import urllib.request

def main():

   weburl = urllib.request.urlopen("http://www.google.com")
   print("Result code: ", weburl.getcode())
   # assigning read 

   data = weburl.read()
   # this is the html for google home page 
   print(data)

if __name__ == "__main__":
    main()