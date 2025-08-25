a='Hello'
print("The Data used is : ", a)
print("Data Type is : ", type(a))
print("\n")

for i in range(0,len(a)):
    print("Printing Positive Index : ", i," : ",a[i])

print("\n")

for i in range(-len(a),0):
    print("Printing Negative Index : ", i," : ",a[i])

print("\n")

print("Printing Slice Index : 1 to 3 : ",a[1:3])
print("Printing Slice Index :-4 to 4 : ",a[-4:4])
print("Printing Slice Index : 3 to -1 : ",a[3:-1])

'''
#slice index
print(a[1:3])
print(a[-4:4])
print(a[3:-1])
'''
