# Prompt: ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
# If the function is passed a valid PIN string, return true, else return false.

def validate_pin(pin):
    l = list(pin)
    try:
        list(map(int,l))
    except:
        return False
    else:
        return True if len(l) == 4 or len(l) == 6 else False
