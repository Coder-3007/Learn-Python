# Python code​​​​​​‌​‌‌‌​​‌​​‌​‌​‌‌‌‌‌‌‌‌​‌‌ below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

def is_palindrome(teststr):
    # Convert the string to lowercase
    temp = teststr.lower()

    # Strip non-alphanumeric characters
    newstr = ""
    for c in temp:
        if c.isalnum():
            newstr += c

    # Reverse the string
    reversestrn = ""
    strind = len(newstr) - 1
    while strind >= 0:
        reversestrn += newstr[strind]
        strind -= 1

    # Check if the original string is equal to the reversed string
    if newstr == reversestrn:
        return True
    else:
        return False
