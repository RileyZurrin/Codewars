# Prompt: Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.


def create_phone_number(n):
    s = "".join(map(str,n))
    return "(" + s[0:3] + ") " + s[3:6] + "-" + s[6:10]
