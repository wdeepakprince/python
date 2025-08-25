print("\n")
print("Finding Biggest of the given 4 numbers!")
print("\n")
a=int(input("Enter 1st number : "))
b=int(input("Enter 2nd number : "))
c=int(input("Enter 3rd number : "))
d=int(input("Enter 4th number : "))
print("\n")

def biggest():
    if (a>b and a>c and a>d):
        print("Biggest of the 4 numbers is the 1st number : ",a)
    elif (b>a and b>c and b>d):
        print("Biggest of the 4 numbers is the 2nd number : ",b)
    elif (c>a and c>b and b>d):
        print("Biggest of the 4 numbers is the 3rd number : ",c)
    else:
        print("Biggest of the 4 numbers is the 4th number : ",d)

biggest()
