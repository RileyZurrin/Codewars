# Prompt: The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. 
Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

# Define a function that converts a single number into hexadecimal
def dectohex(n):
    hex = list(map(str,list(range(10)))) + ['A','B','C','D','E','F']
    return hex[min(max(0,n),255)//16] + hex[min(max(0,n),255)%16]

# Apply the dectohex function to each of the rgb numbers.
def rgb(r, g, b):
    return dectohex(r) + dectohex(g) + dectohex(b)
