# # while loop
# num=1
# while(num<5): # it will print 1 to 4
#     print(num)
#     num+=1

# # Break -> used to terminate the loop when encountered
# # Continue -> terminates execution in the current iteration 
# #             $ continues execution of the loop with the next iteration
    
# # For Loops -> used for sequential traversal
# veg=["potato","tomato","carrot"]
# for i in veg:
#     print(i)

# str="Ashutosh"
# for i in str:
#     print(i)

# range() -> Range function returns a sequence of numbers, starting from 0 by default
#            and increments by 1 by default, and stops before a specified number
for i in range(5):       # range(0,5)
    print(i)
for i in range(1,5):     # range(start,stop)
    print(i)
for i in range(1,5,2):   # range(start?,stop,step?)
    print(i)