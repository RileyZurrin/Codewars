# Write an algorithm that cuts a given "true" rectangle 
# into squares ("true" rectangle meaning that the two dimensions are different).
# Can you translate this drawing into an algorithm?

# You will be given two dimensions

#    a positive integer length
#    a positive integer width

#You will return a collection or a string 
#(depending on the language; Shell bash, PowerShell, Pascal and Fortran return a string) with the size of each of the squares.

def sq_in_rect(lng, wdth):
    if lng == wdth:
        return None
    else:
        final = []
        d = [lng, wdth]
        mn, notmn = min(d), d.index(max(d))
        while mn > 0:
            final.append(mn)
            d[notmn] -= mn
            mn, notmn = min(d), d.index(max(d))
        return final
