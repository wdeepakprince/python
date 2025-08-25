print("\n")
print("Voting Eligibility Check!")
print("\n")
age=int(input("Enter your age : "))
print("\n")

def eligibility_check(age):
    if (age>=18):
        print("Eligible for Voting!")
    else:
        print("NOT Eligible for Voting!")

eligibility_check(age)
