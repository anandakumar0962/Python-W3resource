
'''Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'  '''
#Using for loop
def change_char(s):
    lst = list(s)
    for i in range(1, len(s)):
        if s[i] == s[0]:
            lst[i] = "$"
    return ''.join(lst)

s = input("Enter a string: ")
print(change_char(s))

#Using replace() method

def change_char(s):
    result = s[0] + s[1:].replace(s[0], '$')
    return result

s = input("Enter a string: ")
print(change_char(s))
