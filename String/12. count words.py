
'''
12. Write a Python program to count the occurrences of each word in a given sentence.'''

def count_word(sentence):
    list_words = sentence.split(' ')
    d = {}
    for word in list_words:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
    for word, count in d.items():
        print(word, count)

sentence = input("Enter your sentence: ")
count_word(sentence)
