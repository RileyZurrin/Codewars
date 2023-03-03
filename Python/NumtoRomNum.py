# Prompt: Create a function taking a positive integer between 1 and 3999 (both included) 
# as its parameter and returning a string containing the Roman Numeral representation of that integer.

def solution(n):
    map = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    multipliers = []
    for m in map:
        multipliers.append(n//m)
        n = n%m
    return "".join([multipliers[i]*roman[i] for i in range(len(roman))])
