# Prompt: Write a function toWeirdCase (weirdcase in Ruby) that 
# accepts a string, and returns the same string with all even 
# indexed characters in each word upper cased, and all odd indexed 
# characters in each word lower cased. The indexing just 
# explained is zero based, so the zero-ith index is even, therefore that 
# character should be upper cased and you need to start over for each word.

def to_weird_case_word(word):
    return "".join([j.upper() if i%2 == 0 else j.lower() for i,j in enumerate(word)])

def to_weird_case(words):
    return " ".join([to_weird_case_word(x) for x in words.split(" ")])
