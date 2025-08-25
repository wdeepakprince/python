studName =[]

studcount=int(input("Enter the number of students : "))

for i in range(0,studcount):
    print("Enter the name of Student# : ",i+1)
    studName.append(input())
print("Student names saved to list!")
print("\n")

for i in range(0,studcount):
    print(studName [i])
print("Student names retrieved from list!")
print("\n")
