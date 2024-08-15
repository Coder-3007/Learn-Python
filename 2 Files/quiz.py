# Python code​​​​​​‌​‌‌‌​​‌​​‌‌​‌​‌​​​​​‌​​​ below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False



import os

def file_info():
    totalbytes = 0
    folder = "deps"

    # Get the list of files and directories
    dirlist = os.listdir(folder)
    for entry in dirlist:
        # Construct the full path
        filepath = os.path.join(folder, entry)
        
        # Check if it's a file and if it ends with .txt
        if os.path.isfile(filepath) and entry.endswith(".txt"):
            # Add the file size to totalbytes
            filesize = os.path.getsize(filepath)
            totalbytes += filesize
            
    return totalbytes
