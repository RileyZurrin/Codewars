# Prompt: Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
# The first word within the output should be capitalized only if the original word was capitalized 
# (known as Upper Camel Case, also often referred to as Pascal case). 
# The next words should be always capitalized.

def to_camel_case(text):
    s = text.replace("-","_").split("_")
    a = [x.capitalize() for x in s[1:]]
    return s[0] + "".join(a)
