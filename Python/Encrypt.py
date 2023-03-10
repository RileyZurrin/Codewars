# Implement a pseudo-encryption algorithm which given a string S and an
# integer N concatenates all the odd-indexed characters of S with all 
# the even-indexed characters of S, this process should be repeated N times.

# Together with the encryption function, you should also implement a decryption function which reverses the process.

# If the string S is an empty value or the integer N is not positive, return the first argument without changes.


def decrypt(encrypted_text, n):
    if n < 1:
        return encrypted_text
    else:
        l = len(encrypted_text)
        s = ""
        for i in range(l//2):
            s += encrypted_text[l//2 + i] + encrypted_text[i]
    encrypted_text = s + encrypted_text[-1] if l%2 == 1 else s
    return decrypt(encrypted_text, n-1)


def encrypt(text, n):
    if n < 1:
        return text
    else:
        even = "".join(j if i%2 == 0 else "" for i,j in enumerate(text))
        odd = "".join(j if i%2 == 1 else "" for i,j in enumerate(text))
        return encrypt(odd + even, n-1)
