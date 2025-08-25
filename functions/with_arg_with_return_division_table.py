print("\n")
print("Division Table!")
print("\n")

table=int(input("Enter the Division Table you want : "))
startrowcount=int(input("Enter the starting row for the Table : "))
endrowcount=int(input("Enter the ending row for the Table : "))

def printdivrow(table,row):
    return (table/i)

i=startrowcount
while(i<endrowcount+1):
    print(table, " / ", i, " = ",printdivrow(table,i))
    i+=1
