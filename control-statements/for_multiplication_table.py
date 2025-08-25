table=int(input("Enter the Table you want : "))
startrowcount=int(input("Enter the starting row for the Table : "))
endrowcount=int(input("Enter the ending row for the Table : "))

for i in range(startrowcount, endrowcount+1):
    print(table, " * ", i, " = ",table*i)
