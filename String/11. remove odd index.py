'''
11. Write a Python program to remove characters that have odd index values in a given string. '''



def remove_odd_chr(s):
    new_s = ''
    for i in range(0, len(s), 2):
        new_s += s[i]
    return new_s

s = input("Enter a string: ")
print(remove_odd_chr(s))
