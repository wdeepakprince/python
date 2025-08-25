start=int(input("Enter the Start value : "))
end=int(input("Enter the End value : "))
threshold=int(input("Enter the Threshold value : "))

print("\n")
print("Break initiated successfully!")
print("\n")
for i in range(start,end+1):
    if(i==threshold+1):
        break
    print(i)
print("\n")
print("Break executed successfully!")
print("\n")

print("\n")
print("Continue initiated successfully!")
print("\n")
for i in range(start,end+1):
    if(i==threshold):
        print("Skipping ",i," and continuing")
        continue
    print(i)
print("\n")
print("Continue executed successfully!")
print("\n")
