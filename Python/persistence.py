# Prompt: Write a function, persistence, that takes in a positive parameter num and returns 
# its multiplicative persistence, which is the number of times you must multiply the digits 
# in num until you reach a single digit.

def persistence(n):
    if n < 10:
        return 0
    else:
        count = 0
        product = 1
        s = list(str(n))
        while len(s) > 1:
            count += 1
            product = 1
            for num in s:
                product = product*int(num)
            s = list(str(product))
        return count
