table=int(input("Enter the Division Table you want : "))
startrowcount=int(input("Enter the starting row for the Table : "))
endrowcount=int(input("Enter the ending row for the Table : "))

i=startrowcount
while(i<endrowcount+1):
    print(table, " / ", i, " = ",table/i)
    i+=1
