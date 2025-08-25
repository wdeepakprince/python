start=int(input("Enter the Start value : "))
end=int(input("Enter the End value : "))
threshold=int(input("Enter the Threshold value : "))

print("\n")
print("Break initiated successfully!")
print("\n")
i=start
while i < end+1:
    if(i==threshold+1):
        break
    print(i)
    i+=1
print("\n")
print("Break executed successfully!")
print("\n")

print("\n")
print("Continue initiated successfully!")
print("\n")
i=start
while i < end+1:
    if(i==threshold):
        print("Skipping ",i," and continuing")
        i+=1
        continue
    print(i)
    i+=1
print("\n")
print("Continue executed successfully!")
print("\n")
