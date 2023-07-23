
''' 8. Write a Python function that takes a list of words and return the longest word and the length of the longest one.
Sample Output:
Longest word: Exercises
Length of the longest word: 9 '''

def longest_word(lst):
    longest_word = ''
    max_length = 0
    for word in lst:
        if len(word) > max_length:
            max_length = len(word)
            longest_word = word
    print("Longest word: ", longest_word)
    print("Length of the longest word: ", max_length)

lst = input("Enter the words: ").split()
longest_word(lst)
