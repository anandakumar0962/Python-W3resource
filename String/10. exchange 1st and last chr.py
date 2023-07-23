'''
10. Write a Python program to change a given string to a newly string where the first and last chars have been exchanged. '''

def exchange_chr(s):
    new_str = s[-1]+s[1:-1]+s[0]
    return new_str

string = input("Enter a string: ")
print(exchange_chr(string))
