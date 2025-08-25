print("The biggest of the two numbers! \n")
a=int(input("Enter a number : "))
b=int(input("Enter another number : "))

if (a>b):
    biggest = a
else:
    biggest = b
    
print("The biggest of the two numbers is : ", biggest)
print("\n")

print("Age eligibility check for Voting!\n")
age=int(input("Enter your age to check eligibility for voting : "))
if (age>=18):
    print("You are eligible for voting!")
else:
    print("You are NOT eligible for voting!")

print("\n")

print("Number Category check!\n")
num1=int(input("Enter a number : "))
if (num1>0):
    print("You have entered a Positive Number!")
elif (num1==0):
    print("You have entered Zero!")
else:
    print("You have entered a Negative Number!")
print("\n")

print("Greatest of 4 numbers!\n")
number1=int(input("Enter 1st number : "))
number2=int(input("Enter 2nd number : "))
number3=int(input("Enter 3rd number : "))
number4=int(input("Enter 4th number : "))
if (number1>number2):
    if(number1>number3):
        if(number1>number4):
            print("1st number is the greatest of the 4 given numbers!")
        else:
            print("4th number is the greatest of the 4 given numbers!")
    elif(number3>number4):
        print("3rd number is the greatest of the 4 given numbers!")
    else:
        print("4th number is the greatest of the 4 given numbers!")
elif(number2>number3):
    if(number2>number4):
        print("2nd number is the greatest of the 4 given numbers!")
    else:
        print("4th number is the greatest of the 4 given numbers!")
else:
    print("3rd number is the greatest of the 4 given numbers!")

print("\n")
