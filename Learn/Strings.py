# String is a data type that stores a sequence of characters.
 
str1='Hello Ashutos'
str2="This is Ashutosh's pen. It's red in color."
str3=""" This type is used to print sentence in next line
         Like this. If we not use this type, it will
         show error as in python we have to keep
         identation. """
print(str1)
print(str2)
print(str3) # as it is printed with space,nextline

# Concatenation
str4="Ashutosh "
str5="Kumar"
str6=str4+str5
print(str6) # Ashutosh Kumar
print("The length of str6 is",len(str6)) # The length of str6 is 14

# Indexing -> Only we can access by indexing, can not manipulate
str="Java Developer"
print(str[2])

# Slicing -> Accessing parts of a string
print(str[2:12]) # va Develop
print(str[ :4]) # is same as str[0:4]
print(str[1: ]) # is same as str[1:len(str)]
print(str[-3:-1]) # av -> as APPLE idexing in -ve is -5 -4 -3 -2 -1 

# Functions
print(str.endswith("er")) # True
print(str.replace("e","m")) # replace all occurence (old,new) Java Dmvmlopmr
print(str.replace("m","e"))
print(str.find("lop")) # returns 1st indexof the 1st occurence
print(str.count("Dev")) # counts the occurence of substrings