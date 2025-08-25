studentcount=int(input("Enter the number of students to be enrolled : "))

for i in range(1, studentcount+1):
    print("\n")
    print("Please provide details for Student #",i)
    print("\n")
    studname=input("Enter the Student Name : ")
    studage=int(input("Enter the Student Age : "))
    studrollno=input("Enter the Student Roll No : ")
    print("\n")
    studmarkseng=float(input("Enter the Marks for English : "))
    studmarkstam=float(input("Enter the Marks for Tamil : "))
    studmarksmat=float(input("Enter the Marks for Maths : "))
    studmarkssci=float(input("Enter the Marks for Science : "))
    studmarkssoc=float(input("Enter the Marks for Social : "))

    if(studmarkseng>90):
        studgradeeng = "A"
    elif(studmarkseng>80):
        studgradeeng = "B"
    elif(studmarkseng>70):
        studgradeeng = "C"
    else: studgradeeng = "D"

    if(studmarkstam>90):
        studgradetam = "A"
    elif(studmarkstam>80):
        studgradetam = "B"
    elif(studmarkstam>70):
        studgradetam = "C"
    else: studgradetam = "D"

    if(studmarksmat>90):
        studgrademat = "A"
    elif(studmarksmat>80):
        studgrademat = "B"
    elif(studmarksmat>70):
        studgrademat = "C"
    else: studgrademat = "D"

    if(studmarkssci>90):
        studgradesci = "A"
    elif(studmarkssci>80):
        studgradesci = "B"
    elif(studmarkssci>70):
        studgradesci = "C"
    else: studgradesci = "D"

    if(studmarkssoc>90):
        studgradesoc = "A"
    elif(studmarkssoc>80):
        studgradesoc = "B"
    elif(studmarkssoc>70):
        studgradesoc = "C"
    else: studgradesoc = "D"
    
    print("\n")
    print("Student Details Provided")
    print("---------------------------------")
    print("Student Name : ",studname)
    print("Student Age : ",studage)
    print("Student Roll No : ",studrollno)
    print("\n")
    print("Subject Name | Marks | Grade")
    print("----------------------------------------")
    print("English | Marks : ", studmarkseng, " | Grade : ",studgradeeng)
    print("Tamil   | Marks : ", studmarkstam, " | Grade : ",studgradetam)
    print("Maths   | Marks : ", studmarksmat, " | Grade : ",studgrademat)
    print("Science | Marks : ", studmarkssci, " | Grade : ",studgradesci)
    print("Social   | Marks : ", studmarkssoc, " | Grade : ",studgradesoc)
    print("\n")
    studtotalmark=studmarkseng+studmarkstam+studmarksmat+studmarkssci+studmarkssoc
    studavgmark=studtotalmark/5
    if(studavgmark>90):
        studavggrade= "A"
    elif(studavgmark>80):
        studavggrade = "B"
    elif(studavgmark>70):
        studavggrade = "C"
    else: studavggrade = "D"
    
    print("Total Marks : ",studtotalmark)
    print("Average Marks : ", studavgmark)
    print("Cumulative Grade : ",studavggrade)
