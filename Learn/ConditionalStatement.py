# if-elif-else
"""
if(condition):
    Statement1
elif(condition):
    Statement2
else:
    Statement3
"""
# Traffic Light
color=input("Enter the color: ")
num=int(input("Enter number: "))
if(color=="Red" and num==5):
    print("Stop")
elif(color=="Green"):
    print("Go")
else:
    print("Enter valid color")

# Ternary Operator (if true, statement before if will be executed)
food=input("Enter the food name: ")
eat="yes" if food=="Dosa" else "no"
print(eat)

print("I will eat") if food=="Dosa" else print("Not interested")

# clever if/ Ternary operator
myAge=int(input("Enter your age: "))
vote=("yes","no")[myAge<18]
print(vote)