studName =["Deepak","Prince","Walter","Peter","Oliver","Testing"]
studMarks = [98,88,91,68,77,86]

#Built-in Functions
print("Length of the list is : ",len(studName))
print("Max of the list is : ",max(studName))
print("Min of the list is : ",min(studName))
print("Sum of the list is : ",sum(studMarks))
print("Sorted list is : ",sorted(studName))
print("Actual list is : ",studName)

#List Functions
print("\n")
print("Current list is : ",studName)
studName.append(input("Enter the Student name to be added : "))
print("Updated list after append is : ",studName)

print("\n")
print("Current list is : ",studName)
studName.remove("Testing")
print("Updated list after removal is : ",studName)
