

'''Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1} '''

#Using counter() method.

from collections import Counter
def count_char(s):
    counts = Counter(s)
    print(dict(counts))
s = input("Enter a string:")
count_char(s)

#Using for loop.

def count_char(s):

    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    print(d)

s = input("Enter a string:")
count_char(s)
