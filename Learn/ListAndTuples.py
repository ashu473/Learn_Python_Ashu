# Lists -> A built-in data type that stores set of values.
#          It can store elements of different types(integer,float,string,etc)
#          List are muttable in Python
#          Slicing of List is same as Slicing String in Python

marks=["ashu","kumar",23,50.00] # list
print(marks) # ['ashu', 'kumar', 23, 50.0]
print(type(marks)) # <class 'list'>
print(marks[2]) # 23
print(len(marks)) # 4
marks[0]="Ashutosh" # ashu will be replaced by Ashutosh, as list is muttable
print(marks) # ['Ashutosh', 'kumar', 23, 50.0]
print(marks[1:3]) # ['kumar', 23], this is slicing

# List Methods
list=[2,1,3]
list.append(4) # adds one element to the end -> [2,1,3,4]
list.sort() # sort the list in ascending order -> [1,2,3] 
list.sort(reverse=True) # sort in descending order -> [3,2,1]
list.reverse() # reverse the list -> [3,1,2]
list.insert(0,7) # insert element at the index -> [7, 2, 1, 3]
list.remove(1) # removes 1st occurence element if contain duplicates [2,3],
list.pop(0) # removes element at idx 0 -> [1,3]


# Tuples -> A built in data type that lets us create IMMUTABLE sequences of values

tup=(12,23,45,56)
print(type(tup)) # <class 'tuple'>
tup[0]=34 # It is not allowed, we can't manipulate
tup1=(1,) # write , if you write single value otherwise interpreter treat as int

# Tuple Methods
tup2=(1,2,3,2,4,6,7)
tup2.index(2) # returns idx of 1st occurence -> 1 
tup2.count(2) # counts total occurences -> 2 