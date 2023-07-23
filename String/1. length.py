

'''Write a Python program to calculate the length of a string.'''

#Method 1 Using For loop.
def string_length(s):
    l = 0
    for i in s:
        l += 1
    return l

s = input("Enter a string: ")
print("Length of a string:", string_length(s))

#Method 2 Using builtin method.

def string_length(s):

    l = len(s)
    return l

s = input("Enter a string: ")
print("Length of a string:", string_length(s))
