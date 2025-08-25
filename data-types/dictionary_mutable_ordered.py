dicta={1:10, "Deepak":"Prince",95.75:10.25}

print("The Given Data is : ", dicta)
print("Data Type is : ", type(dicta))
print("\n")

print("Checking Mutability...")
dicta [1]= 20
dicta ["Deepak"] = "Oliver"
print("Mutation Completed...")
print("\n")

print("The Muted Data is : ", dicta)
print("Data Type is : ", type(dicta))
print("\n")
