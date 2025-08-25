tuplea=(1, "Deepak",95.75,[1,2,3])

print("The Given Data is : ", tuplea)
print("Data Type is : ", type(tuplea))
print("\n")

print("Checking Mutability...")
tuplea [1]="Prince"
tuplea [3][1] = 4
print("Mutation Completed...")
print("\n")

print("The Muted Data is : ", tuplea)
print("Data Type is : ", type(tuplea))
print("\n")
