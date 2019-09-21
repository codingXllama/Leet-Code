#if a string is a palindrome

def reverse(s):
    return s[::-1]

def isPalin(s):
    rev=reverse(s)

    if s==rev:
        return True
    return False



soln=isPalin('boba')
print(soln)