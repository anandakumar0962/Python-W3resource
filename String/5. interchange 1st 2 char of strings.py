

'''5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz' '''

#Using replace() method.
def interchange_chr(str1, str2):

    new_str = str1.replace(str1[:2],str2[:2])+ " " +str2.replace(str2[:2], str1[:2])
    return new_str

str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")
print(interchange_chr(str1, str2))

#Using slice method.
def interchange_chr(str1, str2):

    new_str2 = str1[:2]+str2[2:]
    new_str1 = str2[:2]+str1[2:]
    return new_str1+ " " +new_str2

str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")
print(interchange_chr(str1, str2))
