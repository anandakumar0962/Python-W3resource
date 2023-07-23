
''' 7. Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!' '''

def review_edit(review):
    index_not = review.find('not')
    index_poor = review.find('poor')
    
    if (index_not > 0 and index_poor > 0) and index_poor > index_not:
        review = review[:index_not]+'good!'

    return review

review = input("Enter the review: ")
print(review_edit(review))
