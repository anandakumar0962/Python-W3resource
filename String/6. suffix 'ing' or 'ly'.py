
''' 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly' '''

def suffix_adder(s):
    
    if len(s) > 2:
        if s.endswith('ing'):
            s += 'ly'
        else:
            s += 'ing'
    return s
string = input("Enter a string: ")
print(suffix_adder(string))
